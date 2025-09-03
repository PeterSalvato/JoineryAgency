<?php
require_once 'assets/components/header.php';
require_once 'assets/components/nav.php';

$PageData = [
    'Title' => 'Blog',
    'Description' => 'Design & Development Insights',
    'Classes' => 'BlogPage'
];

// Function to parse frontmatter from markdown file
function parseFrontmatter($content) {
    if (!preg_match('/^---\s*\n(.*?)\n---\s*\n(.*)$/s', $content, $matches)) {
        return ['metadata' => [], 'content' => $content];
    }
    
    $frontmatter = $matches[1];
    $content = $matches[2];
    $metadata = [];
    
    // Simple YAML parsing for basic key: value pairs
    $lines = explode("\n", $frontmatter);
    foreach ($lines as $line) {
        $line = trim($line);
        if (empty($line)) continue;
        
        if (preg_match('/^(\w+):\s*(.+)$/', $line, $match)) {
            $key = $match[1];
            $value = trim($match[2]);
            
            // Handle arrays (tags)
            if (preg_match('/^\[(.*)\]$/', $value, $arrayMatch)) {
                $tags = explode(',', $arrayMatch[1]);
                $metadata[$key] = array_map(function($tag) {
                    return trim($tag, ' "');
                }, $tags);
            } else {
                // Remove quotes from strings
                $metadata[$key] = trim($value, '"');
            }
        }
    }
    
    return ['metadata' => $metadata, 'content' => $content];
}

// Function to get blog data from markdown files
function getBlogData() {
    $postsDir = __DIR__ . '/assets/blog/posts/';
    $posts = [];
    
    if (!is_dir($postsDir)) {
        return ['posts' => []];
    }
    
    $files = glob($postsDir . '*.md');
    
    foreach ($files as $file) {
        $content = file_get_contents($file);
        $parsed = parseFrontmatter($content);
        
        if (!empty($parsed['metadata'])) {
            $post = $parsed['metadata'];
            $post['content'] = $parsed['content'];
            $post['id'] = basename($file, '.md');
            
            // Generate slug from filename if not provided
            if (empty($post['slug'])) {
                $post['slug'] = preg_replace('/^\d{4}-\d{2}-\d{2}-/', '', $post['id']);
            }
            
            $posts[] = $post;
        }
    }
    
    // Sort posts by date (newest first)
    usort($posts, function($a, $b) {
        return strtotime($b['date']) - strtotime($a['date']);
    });
    
    return ['posts' => $posts];
}

// Function to render a single blog post
function renderBlogPost($post) {
    $date = date('F j, Y', strtotime($post['date']));
    $tags = isset($post['tags']) && is_array($post['tags']) ? implode(', ', $post['tags']) : '';
    
    // Convert markdown-style content to basic HTML
    $content = htmlspecialchars($post['content']);
    $content = preg_replace('/^# (.+)$/m', '<h1>$1</h1>', $content);
    $content = preg_replace('/^## (.+)$/m', '<h2>$1</h2>', $content);
    $content = preg_replace('/^### (.+)$/m', '<h3>$1</h3>', $content);
    $content = preg_replace('/^\*\*(.+)\*\*:/m', '<strong>$1</strong>:', $content);
    $content = preg_replace('/^- (.+)$/m', '<li>$1</li>', $content);
    $content = str_replace("\n\n", '</p><p>', $content);
    $content = '<p>' . $content . '</p>';
    $content = str_replace('<p><h', '<h', $content);
    $content = str_replace('</h1></p>', '</h1>', $content);
    $content = str_replace('</h2></p>', '</h2>', $content);
    $content = str_replace('</h3></p>', '</h3>', $content);
    $content = str_replace('<p><li>', '<ul><li>', $content);
    $content = str_replace('</li></p>', '</li></ul>', $content);
    
    return "
    <article class='BlogPost'>
        <header class='BlogPost-Header'>
            <h2 class='BlogPost-Title'>
                <a href='post.php?slug={$post['slug']}'>{$post['title']}</a>
            </h2>
            <div class='BlogPost-Meta'>
                <time datetime='{$post['date']}'>{$date}</time>
                <span class='BlogPost-Author'>by {$post['author']}</span>
                <div class='BlogPost-Tags'>{$tags}</div>
            </div>
        </header>
        <div class='BlogPost-Excerpt'>
            <p>{$post['excerpt']}</p>
            <a href='post.php?slug={$post['slug']}' class='ReadMore'>Read More →</a>
        </div>
    </article>";
}

$blogData = getBlogData();
?>

<main class="Main BlogPage">
    <section class="BlogContent">
        <div class="Container">
            <header class="BlogHeader">
                <h1>Blog</h1>
                <p>Design & Development Insights</p>
            </header>
            <div class="BlogPosts">
                <?php 
                if ($blogData && isset($blogData['posts'])) {
                    foreach ($blogData['posts'] as $post) {
                        echo renderBlogPost($post);
                    }
                } else {
                    echo '<p>No blog posts available at this time.</p>';
                }
                ?>
            </div>
        </div>
    </section>
</main>

<?php require_once 'assets/components/footer.php'; ?>
<?php
require_once 'assets/components/header.php';
require_once 'assets/components/nav.php';

// Get post slug from URL parameter
$postSlug = $_GET['slug'] ?? '';

if (!$postSlug) {
    header('Location: blog.php');
    exit;
}

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

// Function to find post by slug
function findPostBySlug($slug) {
    $postsDir = __DIR__ . '/assets/blog/posts/';
    
    if (!is_dir($postsDir)) {
        return null;
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
            
            if ($post['slug'] === $slug) {
                return $post;
            }
        }
    }
    
    return null;
}

// Function to convert markdown-style content to HTML
function convertMarkdownToHtml($content) {
    $content = htmlspecialchars($content);
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
    
    return $content;
}

$post = findPostBySlug($postSlug);

if (!$post) {
    header('HTTP/1.0 404 Not Found');
    $PageData = [
        'Title' => 'Post Not Found',
        'Description' => 'The requested blog post could not be found',
        'Classes' => 'BlogPage PostNotFound'
    ];
} else {
    $PageData = [
        'Title' => $post['title'] . ' - Joinery Blog',
        'Description' => $post['excerpt'],
        'Classes' => 'BlogPage SinglePost'
    ];
}
?>

<?php if (!$post): ?>
    <main class="Main BlogPage PostNotFound">
        <section class="BlogContent">
            <div class="Container">
                <h1>Post Not Found</h1>
                <p>The requested blog post could not be found.</p>
                <a href="blog.php" class="BackLink">← Back to Blog</a>
            </div>
        </section>
    </main>
<?php else: ?>
    <main class="Main BlogPage SinglePost">
        <section class="BlogContent">
            <div class="Container">
                <nav class="PostNavigation">
                    <a href="blog.php" class="BackLink">← Back to Blog</a>
                </nav>
                
                <article class="BlogPost SingleBlogPost">
                    <header class="BlogPost-Header">
                        <h1 class="BlogPost-Title"><?php echo htmlspecialchars($post['title']); ?></h1>
                        <div class="BlogPost-Meta">
                            <time datetime="<?php echo $post['date']; ?>">
                                <?php echo date('F j, Y', strtotime($post['date'])); ?>
                            </time>
                            <span class="BlogPost-Author">by <?php echo htmlspecialchars($post['author']); ?></span>
                            <?php if (!empty($post['tags'])): ?>
                                <div class="BlogPost-Tags">
                                    <?php foreach ($post['tags'] as $tag): ?>
                                        <span class="Tag"><?php echo htmlspecialchars($tag); ?></span>
                                    <?php endforeach; ?>
                                </div>
                            <?php endif; ?>
                        </div>
                    </header>
                    
                    <div class="BlogPost-Content">
                        <?php echo convertMarkdownToHtml($post['content']); ?>
                    </div>
                    
                    <footer class="BlogPost-Footer">
                        <nav class="PostNavigation">
                            <a href="blog.php" class="BackLink">← Back to Blog</a>
                        </nav>
                    </footer>
                </article>
            </div>
        </section>
    </main>
<?php endif; ?>

<?php require_once 'assets/components/footer.php'; ?>
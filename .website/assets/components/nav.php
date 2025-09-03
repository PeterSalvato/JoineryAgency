<?php
// Helper function to determine if current page matches link
function isCurrentPage($href) {
    $currentPage = basename($_SERVER['PHP_SELF']);
    $linkPage = basename($href);
    return $currentPage === $linkPage;
}

// Helper function to get breadcrumb for current page
function getCurrentPageInfo() {
    $currentPage = basename($_SERVER['PHP_SELF'], '.php');
    
    $pages = [
        'index' => ['title' => 'Home', 'parent' => null],
        'about' => ['title' => 'About', 'parent' => 'index'],
        'portfolio' => ['title' => 'Portfolio', 'parent' => 'index'],
        'contact' => ['title' => 'Contact', 'parent' => 'index'],
        'blog' => ['title' => 'Blog', 'parent' => 'index'],
        'post' => ['title' => 'Article', 'parent' => 'blog']
    ];
    
    return $pages[$currentPage] ?? ['title' => 'Page', 'parent' => 'index'];
}

$currentPageInfo = getCurrentPageInfo();
?>

<nav class="Navigation">
    <div class="Container">
        <a href="index.php" class="Logo <?php echo isCurrentPage('index.php') ? 'Logo--active' : ''; ?>">
            <img src="assets/images/logo.svg" alt="Joinery SystemWorks">
            <!-- <span class="Logo__Text">Joinery SystemWorks</span> -->
        </a>
        
        <ul class="Navigation__Menu" id="navigation-menu">
            <li><a href="index.php" class="Navigation__Link <?php echo isCurrentPage('index.php') ? 'Navigation__Link--active' : ''; ?>" <?php echo isCurrentPage('index.php') ? 'aria-current="page"' : ''; ?>>
                <?php $IconData = ['name' => 'home', 'semantic' => 'home-page', 'decorative' => true]; include 'assets/components/icon.php'; ?>
                <span class="Navigation__LinkText">Home</span>
            </a></li>
            <li><a href="about.php" class="Navigation__Link <?php echo isCurrentPage('about.php') ? 'Navigation__Link--active' : ''; ?>" <?php echo isCurrentPage('about.php') ? 'aria-current="page"' : ''; ?>>
                <?php $IconData = ['name' => 'info', 'semantic' => 'about-info', 'decorative' => true]; include 'assets/components/icon.php'; ?>
                <span class="Navigation__LinkText">About</span>
            </a></li>
            <li><a href="portfolio.php" class="Navigation__Link <?php echo isCurrentPage('portfolio.php') ? 'Navigation__Link--active' : ''; ?>" <?php echo isCurrentPage('portfolio.php') ? 'aria-current="page"' : ''; ?>>
                <?php $IconData = ['name' => 'work', 'semantic' => 'portfolio-showcase', 'decorative' => true]; include 'assets/components/icon.php'; ?>
                <span class="Navigation__LinkText">Portfolio</span>
            </a></li>
            <li><a href="contact.php" class="Navigation__Link <?php echo isCurrentPage('contact.php') ? 'Navigation__Link--active' : ''; ?>" <?php echo isCurrentPage('contact.php') ? 'aria-current="page"' : ''; ?>>
                <?php $IconData = ['name' => 'mail', 'semantic' => 'contact-form', 'decorative' => true]; include 'assets/components/icon.php'; ?>
                <span class="Navigation__LinkText">Contact</span>
            </a></li>
            <li><a href="blog.php" class="Navigation__Link <?php echo isCurrentPage('blog.php') ? 'Navigation__Link--active' : ''; ?>" <?php echo isCurrentPage('blog.php') ? 'aria-current="page"' : ''; ?>>
                <?php $IconData = ['name' => 'article', 'semantic' => 'blog-articles', 'decorative' => true]; include 'assets/components/icon.php'; ?>
                <span class="Navigation__LinkText">Blog</span>
            </a></li>
        </ul>
        
        <button class="Navigation__Toggle" aria-label="Toggle navigation menu" aria-expanded="false" aria-controls="navigation-menu">
            <span></span>
            <span></span>
            <span></span>
        </button>
    </div>
    
    <?php if ($currentPageInfo['parent']): ?>
    <div class="Navigation__Breadcrumb">
        <div class="Container">
            <nav class="Breadcrumb" aria-label="Breadcrumb">
                <ol class="Breadcrumb__List">
                    <li class="Breadcrumb__Item">
                        <a href="index.php" class="Breadcrumb__Link">Home</a>
                        <span class="Breadcrumb__Separator" aria-hidden="true">
                            <?php $IconData = ['name' => 'chevron_right', 'semantic' => 'breadcrumb-separator', 'decorative' => true]; include 'assets/components/icon.php'; ?>
                        </span>
                    </li>
                    <?php if ($currentPageInfo['parent'] !== 'index'): ?>
                    <li class="Breadcrumb__Item">
                        <a href="<?php echo $currentPageInfo['parent']; ?>.php" class="Breadcrumb__Link"><?php echo ucfirst($currentPageInfo['parent']); ?></a>
                        <span class="Breadcrumb__Separator" aria-hidden="true">
                            <?php $IconData = ['name' => 'chevron_right', 'semantic' => 'breadcrumb-separator', 'decorative' => true]; include 'assets/components/icon.php'; ?>
                        </span>
                    </li>
                    <?php endif; ?>
                    <li class="Breadcrumb__Item Breadcrumb__Item--current" aria-current="page">
                        <?php echo $currentPageInfo['title']; ?>
                    </li>
                </ol>
            </nav>
        </div>
    </div>
    <?php endif; ?>
</nav>
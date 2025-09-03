<?php
require_once 'assets/components/header.php';
require_once 'assets/components/nav.php';

$PageData = [
    'Title' => 'Portfolio - Design & Development Consultancy',
    'Description' => 'View our recent work in visual design, UX, and development',
    'Classes' => 'PortfolioPage'
];

function LoadPortfolioData() {
    $JsonFile = 'assets/data/portfolio.json';
    if (file_exists($JsonFile)) {
        $JsonData = file_get_contents($JsonFile);
        return json_decode($JsonData, true);
    }
    return ['projects' => []];
}

$PortfolioData = LoadPortfolioData();
?>

<main class="Main PortfolioPage">
    <section class="Hero">
        <div class="Container">
            <div class="Hero__Content">
                <h1 class="Hero__Title">Our <span>Work</span></h1>
                <p class="Hero__Subtitle">Case studies showcasing our systematic approach to digital transformation and design excellence.</p>
            </div>
        </div>
    </section>
    
    <section class="Portfolio">
        <div class="Container">
            <div class="PortfolioIndex">
                <?php foreach ($PortfolioData['projects'] as $Project): 
                    // Generate clean URL slug for case study
                    $slug = $Project['id'];
                ?>
                    <article class="PortfolioCard">
                        <div class="PortfolioCard-Image">
                            <?php if (!empty($Project['image'])): ?>
                                <img src="<?php echo htmlspecialchars($Project['image']); ?>" 
                                     alt="<?php echo htmlspecialchars($Project['title']); ?> project preview"
                                     loading="lazy">
                            <?php else: ?>
                                <div class="placeholder-image card" title="Project image placeholder for <?php echo htmlspecialchars($Project['title']); ?>"></div>
                            <?php endif; ?>
                        </div>
                        
                        <div class="PortfolioCard-Content">
                            <div class="PortfolioCard-Meta">
                                <div class="PortfolioCard-Services">
                                    <?php foreach (array_slice($Project['services'], 0, 3) as $service): ?>
                                        <span class="Tag"><?php echo htmlspecialchars($service); ?></span>
                                    <?php endforeach; ?>
                                </div>
                                <div class="PortfolioCard-Client">
                                    <?php 
                                    $IconData = [
                                        'name' => 'business', 
                                        'semantic' => 'client-name',
                                        'size' => 'small',
                                        'decorative' => true
                                    ]; 
                                    include 'assets/components/icon.php'; 
                                    ?>
                                    <?php echo htmlspecialchars($Project['client']); ?>
                                </div>
                            </div>
                            
                            <h2 class="PortfolioCard-Title">
                                <a href="case-study.php?project=<?php echo urlencode($slug); ?>" class="PortfolioCard-Link">
                                    <?php echo htmlspecialchars($Project['title']); ?>
                                </a>
                            </h2>
                            
                            <p class="PortfolioCard-Description">
                                <?php echo htmlspecialchars($Project['description']); ?>
                            </p>
                            
                            <div class="PortfolioCard-Actions">
                                <a href="case-study.php?project=<?php echo urlencode($slug); ?>" class="Button Primary">
                                    <?php 
                                    $IconData = [
                                        'name' => 'arrow_forward', 
                                        'semantic' => 'view-case-study',
                                        'size' => 'small',
                                        'decorative' => true
                                    ]; 
                                    include 'assets/components/icon.php'; 
                                    ?>
                                    View Case Study
                                </a>
                                
                                <?php if (!empty($Project['url'])): ?>
                                    <a href="<?php echo htmlspecialchars($Project['url']); ?>" 
                                       class="Button Secondary" 
                                       target="_blank" 
                                       rel="noopener noreferrer">
                                        <?php 
                                        $IconData = [
                                            'name' => 'open_in_new', 
                                            'semantic' => 'external-link',
                                            'size' => 'small',
                                            'label' => 'Visit ' . $Project['title'] . ' website (opens in new tab)'
                                        ]; 
                                        include 'assets/components/icon.php'; 
                                        ?>
                                        Visit Site
                                    </a>
                                <?php endif; ?>
                            </div>
                        </div>
                    </article>
                <?php endforeach; ?>
            </div>
        </div>
    </section>
</main>

<?php require_once 'assets/components/footer.php'; ?>

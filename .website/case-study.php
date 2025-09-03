<?php
require_once 'assets/components/header.php';
require_once 'assets/components/nav.php';

function LoadPortfolioData() {
    $JsonFile = 'assets/data/portfolio.json';
    if (file_exists($JsonFile)) {
        $JsonData = file_get_contents($JsonFile);
        return json_decode($JsonData, true);
    }
    return ['projects' => []];
}

function FindProjectById($projects, $id) {
    foreach ($projects as $project) {
        if ($project['id'] === $id) {
            return $project;
        }
    }
    return null;
}

// Get project ID from URL parameter
$projectId = $_GET['project'] ?? '';
$portfolioData = LoadPortfolioData();
$project = FindProjectById($portfolioData['projects'], $projectId);

// Handle project not found
if (!$project) {
    $PageData = [
        'Title' => 'Case Study Not Found',
        'Description' => 'The requested case study could not be found',
        'Classes' => 'CaseStudyPage NotFound'
    ];
} else {
    $PageData = [
        'Title' => $project['title'] . ' Case Study - Design & Development',
        'Description' => $project['description'],
        'Classes' => 'CaseStudyPage'
    ];
}
?>

<main class="Main CaseStudyPage">
    <?php if (!$project): ?>
        <!-- 404 Not Found -->
        <section class="Hero">
            <div class="Container">
                <div class="Hero__Content">
                    <h1 class="Hero__Title">Case Study <span>Not Found</span></h1>
                    <p class="Hero__Subtitle">The requested case study could not be found.</p>
                    <div class="Hero__Actions">
                        <a href="portfolio.php" class="Button Primary">
                            <?php 
                            $IconData = [
                                'name' => 'arrow_back', 
                                'semantic' => 'back-to-portfolio',
                                'size' => 'small',
                                'decorative' => true
                            ]; 
                            include 'assets/components/icon.php'; 
                            ?>
                            Back to Portfolio
                        </a>
                    </div>
                </div>
            </div>
        </section>
    <?php else: ?>
        <!-- Project Hero -->
        <section class="CaseStudy-Hero">
            <div class="Container">
                <nav class="CaseStudy-Breadcrumb">
                    <a href="portfolio.php" class="Breadcrumb-Link">
                        <?php 
                        $IconData = [
                            'name' => 'arrow_back', 
                            'semantic' => 'back-to-portfolio',
                            'size' => 'small',
                            'decorative' => true
                        ]; 
                        include 'assets/components/icon.php'; 
                        ?>
                        Portfolio
                    </a>
                </nav>
                
                <div class="CaseStudy-Header">
                    <div class="CaseStudy-Meta">
                        <div class="CaseStudy-Services">
                            <?php foreach ($project['services'] as $service): ?>
                                <span class="Tag"><?php echo htmlspecialchars($service); ?></span>
                            <?php endforeach; ?>
                        </div>
                        <div class="CaseStudy-Client">
                            <?php 
                            $IconData = [
                                'name' => 'business', 
                                'semantic' => 'client-name',
                                'size' => 'small',
                                'decorative' => true
                            ]; 
                            include 'assets/components/icon.php'; 
                            ?>
                            <?php echo htmlspecialchars($project['client']); ?>
                        </div>
                    </div>
                    
                    <h1 class="CaseStudy-Title"><?php echo htmlspecialchars($project['title']); ?></h1>
                    <p class="CaseStudy-Description"><?php echo htmlspecialchars($project['description']); ?></p>
                    
                    <?php if (!empty($project['url'])): ?>
                        <div class="CaseStudy-Actions">
                            <a href="<?php echo htmlspecialchars($project['url']); ?>" 
                               class="Button Primary" 
                               target="_blank" 
                               rel="noopener noreferrer">
                                <?php 
                                $IconData = [
                                    'name' => 'open_in_new', 
                                    'semantic' => 'external-link',
                                    'size' => 'small',
                                    'label' => 'Visit ' . $project['title'] . ' website (opens in new tab)'
                                ]; 
                                include 'assets/components/icon.php'; 
                                ?>
                                Visit Live Site
                            </a>
                        </div>
                    <?php endif; ?>
                </div>
            </div>
        </section>

        <!-- Main Project Image -->
        <section class="CaseStudy-Image">
            <div class="Container">
                <?php if (!empty($project['image'])): ?>
                    <img src="<?php echo htmlspecialchars($project['image']); ?>" 
                         alt="<?php echo htmlspecialchars($project['title']); ?> main project image" 
                         class="CaseStudy-MainImage">
                <?php else: ?>
                    <div class="placeholder-image large" title="Main project image placeholder for <?php echo htmlspecialchars($project['title']); ?>"></div>
                <?php endif; ?>
            </div>
        </section>

        <!-- Project Details -->
        <section class="CaseStudy-Content">
            <div class="Container">
                <div class="CaseStudy-Grid">
                    <!-- Challenge & Solution -->
                    <div class="CaseStudy-Section">
                        <h2>
                            <?php 
                            $IconData = [
                                'name' => 'psychology', 
                                'semantic' => 'challenge-section',
                                'size' => 'small',
                                'color' => 'accent'
                            ]; 
                            include 'assets/components/icon.php'; 
                            ?>
                            The Challenge
                        </h2>
                        <p><?php echo htmlspecialchars($project['challenge'] ?? 'Challenge details not available'); ?></p>
                    </div>
                    
                    <div class="CaseStudy-Section">
                        <h2>
                            <?php 
                            $IconData = [
                                'name' => 'lightbulb', 
                                'semantic' => 'solution-section',
                                'size' => 'small',
                                'color' => 'accent'
                            ]; 
                            include 'assets/components/icon.php'; 
                            ?>
                            Our Solution
                        </h2>
                        <p><?php echo htmlspecialchars($project['solution'] ?? 'Solution details not available'); ?></p>
                    </div>
                    
                    <!-- Results -->
                    <?php if (!empty($project['results'])): ?>
                        <div class="CaseStudy-Section CaseStudy-Results">
                            <h2>
                                <?php 
                                $IconData = [
                                    'name' => 'trending_up', 
                                    'semantic' => 'results-section',
                                    'size' => 'small',
                                    'color' => 'accent'
                                ]; 
                                include 'assets/components/icon.php'; 
                                ?>
                                Results & Impact
                            </h2>
                            <ul class="CaseStudy-ResultsList">
                                <?php foreach ($project['results'] as $result): ?>
                                    <li>
                                        <?php 
                                        $IconData = [
                                            'name' => 'check_circle', 
                                            'semantic' => 'result-achieved',
                                            'size' => 'small',
                                            'color' => 'accent',
                                            'decorative' => true
                                        ]; 
                                        include 'assets/components/icon.php'; 
                                        ?>
                                        <?php echo htmlspecialchars($result); ?>
                                    </li>
                                <?php endforeach; ?>
                            </ul>
                        </div>
                    <?php endif; ?>
                    
                    <!-- Technologies -->
                    <?php if (!empty($project['technologies'])): ?>
                        <div class="CaseStudy-Section CaseStudy-Tech">
                            <h2>
                                <?php 
                                $IconData = [
                                    'name' => 'code', 
                                    'semantic' => 'technologies-section',
                                    'size' => 'small',
                                    'color' => 'accent'
                                ]; 
                                include 'assets/components/icon.php'; 
                                ?>
                                Technologies Used
                            </h2>
                            <div class="TechStack">
                                <?php foreach ($project['technologies'] as $tech): ?>
                                    <span class="TechTag"><?php echo htmlspecialchars($tech); ?></span>
                                <?php endforeach; ?>
                            </div>
                        </div>
                    <?php endif; ?>
                </div>
            </div>
        </section>

        <!-- Gallery -->
        <?php if (!empty($project['gallery'])): ?>
            <section class="CaseStudy-Gallery">
                <div class="Container">
                    <h2>Project Gallery</h2>
                    <div class="Gallery-Grid">
                        <?php foreach ($project['gallery'] as $galleryImage): ?>
                            <?php if (!empty($galleryImage)): ?>
                                <img src="<?php echo htmlspecialchars($galleryImage); ?>" 
                                     alt="<?php echo htmlspecialchars($project['title']); ?> gallery image" 
                                     class="Gallery-Image"
                                     loading="lazy">
                            <?php else: ?>
                                <div class="placeholder-image small Gallery-Image" title="Gallery image placeholder"></div>
                            <?php endif; ?>
                        <?php endforeach; ?>
                    </div>
                </div>
            </section>
        <?php endif; ?>

        <!-- Navigation -->
        <section class="CaseStudy-Navigation">
            <div class="Container">
                <div class="CaseStudy-Nav">
                    <a href="portfolio.php" class="Button Secondary">
                        <?php 
                        $IconData = [
                            'name' => 'grid_view', 
                            'semantic' => 'all-projects',
                            'size' => 'small',
                            'decorative' => true
                        ]; 
                        include 'assets/components/icon.php'; 
                        ?>
                        All Projects
                    </a>
                    
                    <a href="contact.php" class="Button Primary">
                        <?php 
                        $IconData = [
                            'name' => 'arrow_forward', 
                            'semantic' => 'start-project',
                            'size' => 'small',
                            'decorative' => true
                        ]; 
                        include 'assets/components/icon.php'; 
                        ?>
                        Start Your Project
                    </a>
                </div>
            </div>
        </section>
    <?php endif; ?>
</main>

<?php require_once 'assets/components/footer.php'; ?>
<?php
// Portfolio Case Study Template - For detailed project case studies with challenge/solution/results
// Usage: Set $PortfolioData array with project data before including

$Title = $PortfolioData['title'] ?? '';
$Client = $PortfolioData['client'] ?? '';
$Services = $PortfolioData['services'] ?? [];
$Description = $PortfolioData['description'] ?? '';
$Challenge = $PortfolioData['challenge'] ?? '';
$Solution = $PortfolioData['solution'] ?? '';
$Results = $PortfolioData['results'] ?? [];
$Technologies = $PortfolioData['technologies'] ?? [];
$Image = $PortfolioData['image'] ?? '';
$Gallery = $PortfolioData['gallery'] ?? [];
$Url = $PortfolioData['url'] ?? '';
$Date = $PortfolioData['date'] ?? '';
$Classes = $PortfolioData['classes'] ?? 'PortfolioCaseStudy';
?>

<article class="PortfolioItem PortfolioCaseStudy <?php echo htmlspecialchars($Classes); ?>">
    <div class="PortfolioItem__Hero">
        <?php if ($Image): ?>
            <img src="<?php echo htmlspecialchars($Image); ?>" alt="<?php echo htmlspecialchars($Title); ?>">
        <?php else: ?>
            <div class="placeholder-image large" title="Project image placeholder for <?php echo htmlspecialchars($Title); ?>"></div>
        <?php endif; ?>
    </div>
    
    <div class="PortfolioItem__Content">
        <header class="PortfolioItem__Header">
            <?php if ($Title): ?>
                <h1 class="PortfolioItem__Title"><?php echo htmlspecialchars($Title); ?></h1>
            <?php endif; ?>
            
            <div class="PortfolioItem__Meta">
                <?php if ($Client): ?>
                    <p class="PortfolioItem__Client"><strong>Client:</strong> <?php echo htmlspecialchars($Client); ?></p>
                <?php endif; ?>
                
                <?php if (!empty($Services)): ?>
                    <div class="PortfolioItem__Services">
                        <strong>Services:</strong>
                        <?php foreach ($Services as $index => $Service): ?>
                            <span class="PortfolioItem__Service"><?php echo htmlspecialchars($Service); ?></span><?php if ($index < count($Services) - 1): ?>, <?php endif; ?>
                        <?php endforeach; ?>
                    </div>
                <?php endif; ?>
                
                <?php if ($Date): ?>
                    <p class="PortfolioItem__Date"><strong>Date:</strong> <?php echo htmlspecialchars(date('F Y', strtotime($Date))); ?></p>
                <?php endif; ?>
            </div>
        </header>
        
        <?php if ($Description): ?>
            <section class="PortfolioItem__Overview">
                <h2>Project Overview</h2>
                <p><?php echo htmlspecialchars($Description); ?></p>
            </section>
        <?php endif; ?>
        
        <?php if ($Challenge): ?>
            <section class="PortfolioItem__Challenge">
                <h2>The Challenge</h2>
                <p><?php echo htmlspecialchars($Challenge); ?></p>
            </section>
        <?php endif; ?>
        
        <?php if ($Solution): ?>
            <section class="PortfolioItem__Solution">
                <h2>Our Solution</h2>
                <p><?php echo htmlspecialchars($Solution); ?></p>
            </section>
        <?php endif; ?>
        
        <?php if (!empty($Gallery)): ?>
            <section class="PortfolioItem__Gallery">
                <h2>Project Visuals</h2>
                <div class="PortfolioItem__GalleryGrid">
                    <?php foreach ($Gallery as $GalleryImage): ?>
                        <div class="PortfolioItem__GalleryImage">
                            <img src="<?php echo htmlspecialchars($GalleryImage); ?>" alt="<?php echo htmlspecialchars($Title); ?> - Project Visual">
                        </div>
                    <?php endforeach; ?>
                </div>
            </section>
        <?php endif; ?>
        
        <?php if (!empty($Results)): ?>
            <section class="PortfolioItem__Results">
                <h2>Results & Impact</h2>
                <ul class="PortfolioItem__ResultsList">
                    <?php foreach ($Results as $Result): ?>
                        <li><?php echo htmlspecialchars($Result); ?></li>
                    <?php endforeach; ?>
                </ul>
            </section>
        <?php endif; ?>
        
        <?php if (!empty($Technologies)): ?>
            <section class="PortfolioItem__Technologies">
                <h2>Technologies Used</h2>
                <div class="PortfolioItem__TechList">
                    <?php foreach ($Technologies as $Technology): ?>
                        <span class="PortfolioItem__Tech"><?php echo htmlspecialchars($Technology); ?></span>
                    <?php endforeach; ?>
                </div>
            </section>
        <?php endif; ?>
        
        <footer class="PortfolioItem__Actions">
            <?php if ($Url && $Url !== '#'): ?>
                <a href="<?php echo htmlspecialchars($Url); ?>" class="PortfolioItem__Link Button Button--Primary" target="_blank" rel="noopener">
                    View Live Project
                </a>
            <?php endif; ?>
            
            <a href="/portfolio" class="PortfolioItem__Back Button Button--Secondary">
                ← Back to Portfolio
            </a>
        </footer>
    </div>
</article>
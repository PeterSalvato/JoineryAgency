<?php
// Portfolio Gallery Template - For showcasing visual work with image galleries
// Usage: Set $PortfolioData array with project data before including

$Title = $PortfolioData['title'] ?? '';
$Client = $PortfolioData['client'] ?? '';
$Services = $PortfolioData['services'] ?? [];
$Description = $PortfolioData['description'] ?? '';
$Image = $PortfolioData['image'] ?? '';
$Gallery = $PortfolioData['gallery'] ?? [];
$Url = $PortfolioData['url'] ?? '';
$Date = $PortfolioData['date'] ?? '';
$Classes = $PortfolioData['classes'] ?? 'PortfolioGallery';
?>

<article class="PortfolioItem PortfolioGallery <?php echo htmlspecialchars($Classes); ?>">
    <div class="PortfolioItem__Hero">
        <?php if ($Image): ?>
            <img src="<?php echo htmlspecialchars($Image); ?>" alt="<?php echo htmlspecialchars($Title); ?>">
        <?php else: ?>
            <div class="placeholder-image large" title="Project image placeholder for <?php echo htmlspecialchars($Title); ?>"></div>
        <?php endif; ?>
    </div>
    
    <div class="PortfolioItem__Content">
        <div class="PortfolioItem__Meta">
            <?php if ($Title): ?>
                <h2 class="PortfolioItem__Title"><?php echo htmlspecialchars($Title); ?></h2>
            <?php endif; ?>
            
            <?php if ($Client): ?>
                <p class="PortfolioItem__Client">Client: <?php echo htmlspecialchars($Client); ?></p>
            <?php endif; ?>
            
            <?php if (!empty($Services)): ?>
                <div class="PortfolioItem__Services">
                    <span class="PortfolioItem__ServicesLabel">Services:</span>
                    <?php foreach ($Services as $Service): ?>
                        <span class="PortfolioItem__Service"><?php echo htmlspecialchars($Service); ?></span>
                    <?php endforeach; ?>
                </div>
            <?php endif; ?>
        </div>
        
        <?php if ($Description): ?>
            <div class="PortfolioItem__Description">
                <p><?php echo htmlspecialchars($Description); ?></p>
            </div>
        <?php endif; ?>
        
        <?php if (!empty($Gallery)): ?>
            <div class="PortfolioItem__Gallery">
                <h3 class="PortfolioItem__GalleryTitle">Project Gallery</h3>
                <div class="PortfolioItem__GalleryGrid">
                    <?php foreach ($Gallery as $GalleryImage): ?>
                        <div class="PortfolioItem__GalleryImage">
                            <img src="<?php echo htmlspecialchars($GalleryImage); ?>" alt="<?php echo htmlspecialchars($Title); ?> - Gallery Image">
                        </div>
                    <?php endforeach; ?>
                </div>
            </div>
        <?php endif; ?>
        
        <div class="PortfolioItem__Actions">
            <?php if ($Url && $Url !== '#'): ?>
                <a href="<?php echo htmlspecialchars($Url); ?>" class="PortfolioItem__Link Button" target="_blank" rel="noopener">
                    View Live Project
                </a>
            <?php endif; ?>
            
            <?php if ($Date): ?>
                <span class="PortfolioItem__Date"><?php echo htmlspecialchars(date('F Y', strtotime($Date))); ?></span>
            <?php endif; ?>
        </div>
    </div>
</article>
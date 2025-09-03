<?php
// Card component - Renders cards with standardized data structure
// Usage: Set $CardData array with Title, Content, Image, Url, Classes before including

$Title = $CardData['Title'] ?? '';
$Content = $CardData['Content'] ?? '';
$Image = $CardData['Image'] ?? '';
$Url = $CardData['Url'] ?? '#';
$Classes = $CardData['Classes'] ?? 'Card';
?>

<article class="Card <?php echo $Classes; ?>">
    <div class="Card__Image">
        <?php if ($Image && !empty(trim($Image))): ?>
            <img src="<?php echo htmlspecialchars($Image); ?>" alt="<?php echo htmlspecialchars($Title); ?>">
        <?php else: ?>
            <div class="Card__ImagePlaceholder" title="Image placeholder for <?php echo htmlspecialchars($Title); ?>">
                <div class="Card__ImagePlaceholder__Pattern Card__ImagePlaceholder__Pattern--<?php echo rand(1, 4); ?>">
                    <div class="Card__ImagePlaceholder__Geometry">
                        <div class="Card__ImagePlaceholder__Shape Card__ImagePlaceholder__Shape--primary"></div>
                        <div class="Card__ImagePlaceholder__Shape Card__ImagePlaceholder__Shape--secondary"></div>
                        <div class="Card__ImagePlaceholder__Shape Card__ImagePlaceholder__Shape--accent"></div>
                    </div>
                </div>
            </div>
        <?php endif; ?>
    </div>
    
    <div class="Card__Content">
        <?php if ($Title): ?>
            <h3 class="Card__Title"><?php echo htmlspecialchars($Title); ?></h3>
        <?php endif; ?>
        
        <?php if ($Content): ?>
            <p class="Card__Description"><?php echo htmlspecialchars($Content); ?></p>
        <?php endif; ?>
        
        <?php if ($Url !== '#'): ?>
            <a href="<?php echo htmlspecialchars($Url); ?>" class="Card__Link">View Project</a>
        <?php endif; ?>
    </div>
</article>

<?php
// Button Component - Enhanced with professional styling and animations
// Usage: Set $ButtonData array with Text, Url, Type, Size, Icon before including

$Text = $ButtonData['Text'] ?? 'Button';
$Url = $ButtonData['Url'] ?? '#';
$Type = $ButtonData['Type'] ?? 'primary'; // primary, secondary, outline, ghost, subtle
$Size = $ButtonData['Size'] ?? 'medium'; // small, medium, large
$Icon = $ButtonData['Icon'] ?? null; // icon name
$IconPosition = $ButtonData['IconPosition'] ?? 'left'; // left, right, only
$Disabled = $ButtonData['Disabled'] ?? false;
$Classes = $ButtonData['Classes'] ?? '';

// Build button classes
$buttonClasses = "Button Button--{$Type} Button--{$Size}";
if ($Icon && $IconPosition === 'only') {
    $buttonClasses .= " Button--icon-only";
}
if ($Disabled) {
    $buttonClasses .= " Button--disabled";
}
if ($Classes) {
    $buttonClasses .= " {$Classes}";
}

// Determine if this should be an anchor or button element
$isLink = $Url !== '#' && !empty($Url);
$element = $isLink ? 'a' : 'button';
$href = $isLink ? 'href="' . htmlspecialchars($Url) . '"' : '';
$disabled = $Disabled ? 'disabled' : '';
?>

<<?php echo $element; ?> class="<?php echo $buttonClasses; ?>" <?php echo $href; ?> <?php echo $disabled; ?>>
    <?php if ($Icon && ($IconPosition === 'left' || $IconPosition === 'only')): ?>
        <span class="Button__Icon Button__Icon--left">
            <?php 
            $IconData = [
                'name' => $Icon, 
                'semantic' => $Text . '-button-icon', 
                'decorative' => true
            ]; 
            include 'assets/components/icon.php'; 
            ?>
        </span>
    <?php endif; ?>
    
    <?php if ($IconPosition !== 'only'): ?>
        <span class="Button__Text"><?php echo htmlspecialchars($Text); ?></span>
    <?php endif; ?>
    
    <?php if ($Icon && $IconPosition === 'right'): ?>
        <span class="Button__Icon Button__Icon--right">
            <?php 
            $IconData = [
                'name' => $Icon, 
                'semantic' => $Text . '-button-icon', 
                'decorative' => true
            ]; 
            include 'assets/components/icon.php'; 
            ?>
        </span>
    <?php endif; ?>
    
    <span class="Button__Ripple"></span>
</<?php echo $element; ?>>
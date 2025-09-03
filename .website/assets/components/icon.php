<?php
/**
 * Semantic Icon Component
 * Renders Material Symbols icons with proper accessibility and semantic meaning
 * 
 * Required parameters:
 * - $IconData['name'] - The Material Symbol icon name
 * - $IconData['semantic'] - Semantic meaning (e.g., 'external-link', 'contact', 'portfolio')
 * 
 * Optional parameters:
 * - $IconData['label'] - Accessible label (auto-generated if not provided)
 * - $IconData['size'] - 'small', 'medium' (default), 'large'
 * - $IconData['style'] - 'outlined' (default), 'rounded', 'filled'
 * - $IconData['color'] - 'primary', 'accent', 'light', 'dark'
 * - $IconData['decorative'] - true for decorative icons (default: false)
 */

// Set defaults
$IconName = $IconData['name'] ?? '';
$Semantic = $IconData['semantic'] ?? '';
$Label = $IconData['label'] ?? ucwords(str_replace(['-', '_'], ' ', $Semantic));
$Size = $IconData['size'] ?? 'medium';
$Style = $IconData['style'] ?? 'outlined';
$Color = $IconData['color'] ?? 'primary';
$IsDecorative = $IconData['decorative'] ?? false;

// Build CSS classes
$Classes = ['material-symbols-' . $Style];

// Add size class
if ($Size === 'small') {
    $Classes[] = 'small';
} elseif ($Size === 'large') {
    $Classes[] = 'large';
}

// Add color class
if ($Color !== 'primary') {
    $Classes[] = $Color;
}

// Add semantic class for styling contexts
if ($Semantic) {
    $Classes[] = 'icon-' . $Semantic;
}

$ClassString = implode(' ', $Classes);

// Determine accessibility attributes
if ($IsDecorative) {
    $AriaAttributes = 'aria-hidden="true"';
    $Title = '';
} else {
    $AriaAttributes = 'aria-label="' . htmlspecialchars($Label) . '" role="img"';
    $Title = ' title="' . htmlspecialchars($Label) . '"';
}
?>

<span class="<?php echo htmlspecialchars($ClassString); ?>" 
      <?php echo $AriaAttributes; ?><?php echo $Title; ?>><?php echo htmlspecialchars($IconName); ?></span>
<?php
// Form Field Component - Professional form elements with validation
// Usage: Set $FormFieldData array with Type, Name, Label, Value, Required, Validation, etc.

$Type = $FormFieldData['Type'] ?? 'text'; // text, email, textarea, select, checkbox, radio
$Name = $FormFieldData['Name'] ?? '';
$Label = $FormFieldData['Label'] ?? '';
$Placeholder = $FormFieldData['Placeholder'] ?? '';
$Value = $FormFieldData['Value'] ?? '';
$Required = $FormFieldData['Required'] ?? false;
$Error = $FormFieldData['Error'] ?? '';
$Success = $FormFieldData['Success'] ?? '';
$Help = $FormFieldData['Help'] ?? '';
$Options = $FormFieldData['Options'] ?? []; // For select/radio
$Icon = $FormFieldData['Icon'] ?? '';
$Classes = $FormFieldData['Classes'] ?? '';
$Attributes = $FormFieldData['Attributes'] ?? [];

// Build field classes
$fieldClasses = "FormField FormField--{$Type}";
if ($Required) $fieldClasses .= " FormField--required";
if ($Error) $fieldClasses .= " FormField--error";
if ($Success) $fieldClasses .= " FormField--success";
if ($Classes) $fieldClasses .= " {$Classes}";

// Build attributes
$attributeString = '';
foreach ($Attributes as $key => $value) {
    $attributeString .= ' ' . htmlspecialchars($key) . '="' . htmlspecialchars($value) . '"';
}

// Generate unique ID
$fieldId = 'field_' . htmlspecialchars($Name) . '_' . uniqid();
?>

<div class="<?php echo $fieldClasses; ?>">
    <?php if ($Label): ?>
        <label for="<?php echo $fieldId; ?>" class="FormField__Label">
            <?php echo htmlspecialchars($Label); ?>
            <?php if ($Required): ?>
                <span class="FormField__Required" aria-label="required">*</span>
            <?php endif; ?>
        </label>
    <?php endif; ?>
    
    <div class="FormField__InputContainer">
        <?php if ($Icon): ?>
            <div class="FormField__Icon FormField__Icon--left">
                <?php $IconData = ['name' => $Icon, 'semantic' => $Name . '-field-icon', 'decorative' => true]; include 'assets/components/icon.php'; ?>
            </div>
        <?php endif; ?>
        
        <?php if ($Type === 'textarea'): ?>
            <textarea 
                id="<?php echo $fieldId; ?>"
                name="<?php echo htmlspecialchars($Name); ?>"
                class="FormField__Input FormField__Textarea"
                <?php if ($Placeholder): ?>placeholder="<?php echo htmlspecialchars($Placeholder); ?>"<?php endif; ?>
                <?php if ($Required): ?>required<?php endif; ?>
                <?php echo $attributeString; ?>
            ><?php echo htmlspecialchars($Value); ?></textarea>
            
        <?php elseif ($Type === 'select'): ?>
            <select 
                id="<?php echo $fieldId; ?>"
                name="<?php echo htmlspecialchars($Name); ?>"
                class="FormField__Input FormField__Select"
                <?php if ($Required): ?>required<?php endif; ?>
                <?php echo $attributeString; ?>
            >
                <?php if ($Placeholder): ?>
                    <option value=""><?php echo htmlspecialchars($Placeholder); ?></option>
                <?php endif; ?>
                <?php foreach ($Options as $optionValue => $optionLabel): ?>
                    <option value="<?php echo htmlspecialchars($optionValue); ?>" <?php echo $Value === $optionValue ? 'selected' : ''; ?>>
                        <?php echo htmlspecialchars($optionLabel); ?>
                    </option>
                <?php endforeach; ?>
            </select>
            <div class="FormField__SelectIcon">
                <?php $IconData = ['name' => 'expand_more', 'semantic' => 'select-dropdown', 'decorative' => true]; include 'assets/components/icon.php'; ?>
            </div>
            
        <?php elseif ($Type === 'checkbox'): ?>
            <div class="FormField__Checkbox">
                <input 
                    type="checkbox"
                    id="<?php echo $fieldId; ?>"
                    name="<?php echo htmlspecialchars($Name); ?>"
                    class="FormField__CheckboxInput"
                    value="1"
                    <?php if ($Value): ?>checked<?php endif; ?>
                    <?php if ($Required): ?>required<?php endif; ?>
                    <?php echo $attributeString; ?>
                >
                <div class="FormField__CheckboxBox">
                    <div class="FormField__CheckboxCheck">
                        <?php $IconData = ['name' => 'check', 'semantic' => 'checkbox-check', 'decorative' => true]; include 'assets/components/icon.php'; ?>
                    </div>
                </div>
                <?php if ($Label): ?>
                    <label for="<?php echo $fieldId; ?>" class="FormField__CheckboxLabel">
                        <?php echo htmlspecialchars($Label); ?>
                        <?php if ($Required): ?>
                            <span class="FormField__Required" aria-label="required">*</span>
                        <?php endif; ?>
                    </label>
                <?php endif; ?>
            </div>
            
        <?php else: ?>
            <input 
                type="<?php echo htmlspecialchars($Type); ?>"
                id="<?php echo $fieldId; ?>"
                name="<?php echo htmlspecialchars($Name); ?>"
                class="FormField__Input"
                <?php if ($Placeholder): ?>placeholder="<?php echo htmlspecialchars($Placeholder); ?>"<?php endif; ?>
                <?php if ($Value): ?>value="<?php echo htmlspecialchars($Value); ?>"<?php endif; ?>
                <?php if ($Required): ?>required<?php endif; ?>
                <?php echo $attributeString; ?>
            >
        <?php endif; ?>
        
        <?php if ($Error): ?>
            <div class="FormField__ValidationIcon FormField__ValidationIcon--error">
                <?php $IconData = ['name' => 'error', 'semantic' => 'field-error', 'decorative' => false]; include 'assets/components/icon.php'; ?>
            </div>
        <?php elseif ($Success): ?>
            <div class="FormField__ValidationIcon FormField__ValidationIcon--success">
                <?php $IconData = ['name' => 'check_circle', 'semantic' => 'field-success', 'decorative' => false]; include 'assets/components/icon.php'; ?>
            </div>
        <?php endif; ?>
    </div>
    
    <?php if ($Help): ?>
        <div class="FormField__Help" id="<?php echo $fieldId; ?>_help">
            <?php echo htmlspecialchars($Help); ?>
        </div>
    <?php endif; ?>
    
    <?php if ($Error): ?>
        <div class="FormField__Error" role="alert" id="<?php echo $fieldId; ?>_error">
            <div class="FormField__ErrorIcon">
                <?php $IconData = ['name' => 'warning', 'semantic' => 'error-warning', 'decorative' => true]; include 'assets/components/icon.php'; ?>
            </div>
            <span class="FormField__ErrorText"><?php echo htmlspecialchars($Error); ?></span>
        </div>
    <?php endif; ?>
    
    <?php if ($Success): ?>
        <div class="FormField__Success" id="<?php echo $fieldId; ?>_success">
            <div class="FormField__SuccessIcon">
                <?php $IconData = ['name' => 'check_circle', 'semantic' => 'success-confirmation', 'decorative' => true]; include 'assets/components/icon.php'; ?>
            </div>
            <span class="FormField__SuccessText"><?php echo htmlspecialchars($Success); ?></span>
        </div>
    <?php endif; ?>
</div>
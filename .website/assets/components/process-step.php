<?php
// Process Step Component - Systematic methodology visualization
// Usage: Set $ProcessStepData array with Number, Title, Description, Icon, Duration before including

$Number = $ProcessStepData['Number'] ?? 1;
$Title = $ProcessStepData['Title'] ?? '';
$Description = $ProcessStepData['Description'] ?? '';
$Icon = $ProcessStepData['Icon'] ?? 'settings';
$Duration = $ProcessStepData['Duration'] ?? '';
$Classes = $ProcessStepData['Classes'] ?? '';
$Layout = $ProcessStepData['Layout'] ?? 'standard'; // standard, horizontal, minimal
$IsLast = $ProcessStepData['IsLast'] ?? false;
?>

<div class="ProcessStep ProcessStep--<?php echo $Layout; ?> <?php echo $Classes; ?>">
    <div class="ProcessStep__Number">
        <div class="ProcessStep__NumberCircle">
            <span class="ProcessStep__NumberText"><?php echo str_pad($Number, 2, '0', STR_PAD_LEFT); ?></span>
        </div>
        <?php if (!$IsLast && $Layout !== 'minimal'): ?>
            <div class="ProcessStep__Connector">
                <div class="ProcessStep__ConnectorLine"></div>
            </div>
        <?php endif; ?>
    </div>
    
    <div class="ProcessStep__Content">
        <div class="ProcessStep__Icon">
            <?php $IconData = ['name' => $Icon, 'semantic' => 'process-step-' . $Number, 'decorative' => true]; include 'assets/components/icon.php'; ?>
        </div>
        
        <div class="ProcessStep__Text">
            <h3 class="ProcessStep__Title"><?php echo htmlspecialchars($Title); ?></h3>
            
            <?php if ($Duration): ?>
                <div class="ProcessStep__Duration">
                    <span class="ProcessStep__DurationIcon">
                        <?php $IconData = ['name' => 'schedule', 'semantic' => 'duration-indicator', 'decorative' => true]; include 'assets/components/icon.php'; ?>
                    </span>
                    <span class="ProcessStep__DurationText"><?php echo htmlspecialchars($Duration); ?></span>
                </div>
            <?php endif; ?>
            
            <?php if ($Description): ?>
                <div class="ProcessStep__Description">
                    <p><?php echo htmlspecialchars($Description); ?></p>
                </div>
            <?php endif; ?>
        </div>
    </div>
</div>
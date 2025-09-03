<?php
// Team Member Component - Professional team showcase
// Usage: Set $TeamMemberData array with Name, Role, Bio, Image, Skills, Social before including

$Name = $TeamMemberData['Name'] ?? '';
$Role = $TeamMemberData['Role'] ?? '';
$Bio = $TeamMemberData['Bio'] ?? '';
$Image = $TeamMemberData['Image'] ?? '';
$Skills = $TeamMemberData['Skills'] ?? []; // Array of skill strings
$Social = $TeamMemberData['Social'] ?? []; // Array of social links
$Classes = $TeamMemberData['Classes'] ?? '';
$Layout = $TeamMemberData['Layout'] ?? 'standard'; // standard, featured, compact
?>

<article class="TeamMember TeamMember--<?php echo $Layout; ?> <?php echo $Classes; ?>">
    <div class="TeamMember__Avatar">
        <?php if ($Image): ?>
            <img src="<?php echo htmlspecialchars($Image); ?>" alt="<?php echo htmlspecialchars($Name); ?>">
        <?php else: ?>
            <div class="TeamMember__Avatar__Placeholder">
                <div class="TeamMember__Avatar__Initial"><?php echo strtoupper(substr($Name, 0, 1)); ?></div>
                <div class="TeamMember__Avatar__Pattern TeamMember__Avatar__Pattern--<?php echo (crc32($Name) % 3) + 1; ?>"></div>
            </div>
        <?php endif; ?>
        
        <?php if (!empty($Social)): ?>
            <div class="TeamMember__Social">
                <?php foreach ($Social as $platform => $url): ?>
                    <a href="<?php echo htmlspecialchars($url); ?>" class="TeamMember__SocialLink" target="_blank" rel="noopener" aria-label="<?php echo htmlspecialchars($Name . ' on ' . ucfirst($platform)); ?>">
                        <?php 
                        $iconName = $platform; // linkedin, twitter, github, etc.
                        if ($platform === 'email') $iconName = 'mail';
                        if ($platform === 'website') $iconName = 'language';
                        $IconData = ['name' => $iconName, 'semantic' => $platform . '-profile', 'decorative' => false]; 
                        include 'assets/components/icon.php'; 
                        ?>
                    </a>
                <?php endforeach; ?>
            </div>
        <?php endif; ?>
    </div>
    
    <div class="TeamMember__Content">
        <header class="TeamMember__Header">
            <h3 class="TeamMember__Name"><?php echo htmlspecialchars($Name); ?></h3>
            <?php if ($Role): ?>
                <div class="TeamMember__Role"><?php echo htmlspecialchars($Role); ?></div>
            <?php endif; ?>
        </header>
        
        <?php if ($Bio): ?>
            <div class="TeamMember__Bio">
                <p><?php echo htmlspecialchars($Bio); ?></p>
            </div>
        <?php endif; ?>
        
        <?php if (!empty($Skills)): ?>
            <div class="TeamMember__Skills">
                <div class="TeamMember__SkillsLabel">Expertise</div>
                <div class="TeamMember__SkillsList">
                    <?php foreach ($Skills as $skill): ?>
                        <span class="TeamMember__Skill"><?php echo htmlspecialchars($skill); ?></span>
                    <?php endforeach; ?>
                </div>
            </div>
        <?php endif; ?>
    </div>
</article>
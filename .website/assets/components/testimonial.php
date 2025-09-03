<?php
// Testimonial Component - Professional client testimonials
// Usage: Set $TestimonialData array with Quote, Author, Role, Company, Image before including

$Quote = $TestimonialData['Quote'] ?? '';
$Author = $TestimonialData['Author'] ?? '';
$Role = $TestimonialData['Role'] ?? '';
$Company = $TestimonialData['Company'] ?? '';
$Image = $TestimonialData['Image'] ?? '';
$Rating = $TestimonialData['Rating'] ?? 5; // 1-5 stars
$Classes = $TestimonialData['Classes'] ?? '';
$Layout = $TestimonialData['Layout'] ?? 'standard'; // standard, featured, compact
?>

<blockquote class="Testimonial Testimonial--<?php echo $Layout; ?> <?php echo $Classes; ?>">
    <?php if ($Layout === 'featured'): ?>
        <div class="Testimonial__Quote Testimonial__Quote--featured">
            <div class="Testimonial__QuoteIcon">
                <?php $IconData = ['name' => 'format_quote', 'semantic' => 'testimonial-quote', 'decorative' => true]; include 'assets/components/icon.php'; ?>
            </div>
            
            <div class="Testimonial__Text">
                <p><?php echo htmlspecialchars($Quote); ?></p>
            </div>
        </div>
        
        <footer class="Testimonial__Attribution Testimonial__Attribution--featured">
            <?php if ($Image): ?>
                <div class="Testimonial__Avatar">
                    <img src="<?php echo htmlspecialchars($Image); ?>" alt="<?php echo htmlspecialchars($Author); ?>">
                </div>
            <?php else: ?>
                <div class="Testimonial__Avatar Testimonial__Avatar--placeholder">
                    <div class="Testimonial__Avatar__Initial"><?php echo strtoupper(substr($Author, 0, 1)); ?></div>
                </div>
            <?php endif; ?>
            
            <div class="Testimonial__AuthorInfo">
                <cite class="Testimonial__Author"><?php echo htmlspecialchars($Author); ?></cite>
                <?php if ($Role || $Company): ?>
                    <div class="Testimonial__Role">
                        <?php if ($Role): ?><span><?php echo htmlspecialchars($Role); ?></span><?php endif; ?>
                        <?php if ($Role && $Company): ?><span class="Testimonial__Separator">·</span><?php endif; ?>
                        <?php if ($Company): ?><span><?php echo htmlspecialchars($Company); ?></span><?php endif; ?>
                    </div>
                <?php endif; ?>
                
                <?php if ($Rating): ?>
                    <div class="Testimonial__Rating" aria-label="<?php echo $Rating; ?> out of 5 stars">
                        <?php for ($i = 1; $i <= 5; $i++): ?>
                            <span class="Testimonial__Star <?php echo $i <= $Rating ? 'Testimonial__Star--filled' : 'Testimonial__Star--empty'; ?>" aria-hidden="true">
                                <?php $IconData = ['name' => 'star', 'semantic' => 'rating-star', 'decorative' => true]; include 'assets/components/icon.php'; ?>
                            </span>
                        <?php endfor; ?>
                    </div>
                <?php endif; ?>
            </div>
        </footer>
    <?php else: ?>
        <div class="Testimonial__Quote">
            <div class="Testimonial__QuoteIcon">
                <?php $IconData = ['name' => 'format_quote', 'semantic' => 'testimonial-quote', 'decorative' => true]; include 'assets/components/icon.php'; ?>
            </div>
            
            <div class="Testimonial__Text">
                <p><?php echo htmlspecialchars($Quote); ?></p>
            </div>
        </div>
        
        <footer class="Testimonial__Attribution">
            <div class="Testimonial__AuthorSection">
                <?php if ($Image): ?>
                    <div class="Testimonial__Avatar">
                        <img src="<?php echo htmlspecialchars($Image); ?>" alt="<?php echo htmlspecialchars($Author); ?>">
                    </div>
                <?php endif; ?>
                
                <div class="Testimonial__AuthorInfo">
                    <cite class="Testimonial__Author"><?php echo htmlspecialchars($Author); ?></cite>
                    <?php if ($Role || $Company): ?>
                        <div class="Testimonial__Role">
                            <?php if ($Role): ?><span><?php echo htmlspecialchars($Role); ?></span><?php endif; ?>
                            <?php if ($Role && $Company): ?><span class="Testimonial__Separator">·</span><?php endif; ?>
                            <?php if ($Company): ?><span><?php echo htmlspecialchars($Company); ?></span><?php endif; ?>
                        </div>
                    <?php endif; ?>
                </div>
            </div>
            
            <?php if ($Rating): ?>
                <div class="Testimonial__Rating" aria-label="<?php echo $Rating; ?> out of 5 stars">
                    <?php for ($i = 1; $i <= 5; $i++): ?>
                        <span class="Testimonial__Star <?php echo $i <= $Rating ? 'Testimonial__Star--filled' : 'Testimonial__Star--empty'; ?>" aria-hidden="true">
                            <?php $IconData = ['name' => 'star', 'semantic' => 'rating-star', 'decorative' => true]; include 'assets/components/icon.php'; ?>
                        </span>
                    <?php endfor; ?>
                </div>
            <?php endif; ?>
        </footer>
    <?php endif; ?>
</blockquote>
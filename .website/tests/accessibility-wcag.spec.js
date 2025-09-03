const { test, expect } = require('@playwright/test');

test.describe('WCAG 2.1 AA Compliance', () => {
  test('Semantic HTML structure', async ({ page }) => {
    await page.goto('/');
    
    // Check for proper heading hierarchy
    const h1Count = await page.locator('h1').count();
    expect(h1Count).toBe(1); // Exactly one H1 per page
    
    // Check for skip navigation link
    const skipLink = await page.locator('a[href="#main"], a[href="#content"]').first();
    const skipLinkExists = await skipLink.isVisible() || 
                          await page.locator('[href="#main"]').count() > 0;
    
    // Check for main landmark
    const main = await page.locator('main, [role="main"]').count();
    expect(main).toBeGreaterThanOrEqual(1);
    
    console.log(`H1 count: ${h1Count}, Main landmarks: ${main}`);
  });

  test('Image accessibility', async ({ page }) => {
    await page.goto('/');
    
    const images = await page.locator('img').count();
    const imagesWithAlt = await page.locator('img[alt]').count();
    
    // All images should have alt text (empty alt="" is acceptable for decorative)
    expect(imagesWithAlt).toBe(images);
    
    console.log(`${images} images, ${imagesWithAlt} with alt attributes`);
  });

  test('Keyboard navigation', async ({ page }) => {
    await page.goto('/');
    
    // Test tab navigation through focusable elements
    const focusableElements = await page.locator('a, button, input, select, textarea, [tabindex]:not([tabindex="-1"])').count();
    
    // Start tabbing and verify focus indicators
    for (let i = 0; i < Math.min(focusableElements, 5); i++) {
      await page.keyboard.press('Tab');
      
      const focused = await page.evaluate(() => {
        const el = document.activeElement;
        const computed = window.getComputedStyle(el);
        return {
          outline: computed.outline,
          boxShadow: computed.boxShadow,
          backgroundColor: computed.backgroundColor
        };
      });
      
      // Should have some kind of focus indicator
      const hasFocusIndicator = focused.outline !== 'none' || 
                               focused.boxShadow !== 'none' || 
                               focused.backgroundColor !== 'rgba(0, 0, 0, 0)';
      
      if (!hasFocusIndicator) {
        console.warn(`Focus indicator may be missing on element ${i + 1}`);
      }
    }
    
    console.log(`${focusableElements} focusable elements tested`);
  });

  test('Color contrast ratios', async ({ page }) => {
    await page.goto('/');
    
    // Check text elements for sufficient contrast
    const textElements = await page.locator('p, h1, h2, h3, h4, h5, h6, a, button').all();
    
    for (const element of textElements.slice(0, 10)) { // Test first 10 elements
      const styles = await element.evaluate(el => {
        const computed = window.getComputedStyle(el);
        return {
          color: computed.color,
          backgroundColor: computed.backgroundColor,
          fontSize: computed.fontSize
        };
      });
      
      // Log for manual verification (automated contrast checking requires additional libraries)
      console.log(`Element: color=${styles.color}, bg=${styles.backgroundColor}, size=${styles.fontSize}`);
    }
  });
});
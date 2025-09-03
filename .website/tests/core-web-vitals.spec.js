const { test, expect } = require('@playwright/test');

test.describe('Core Web Vitals - Industry Standards', () => {
  test('Performance benchmarks', async ({ page }) => {
    const startTime = Date.now();
    
    await page.goto('/');
    await page.waitForLoadState('networkidle');
    
    const loadTime = Date.now() - startTime;
    
    // Industry standard: Page load under 3 seconds
    expect(loadTime).toBeLessThan(3000);
    
    // Check for render-blocking resources
    const cssFiles = await page.locator('link[rel="stylesheet"]').count();
    expect(cssFiles).toBeLessThanOrEqual(3); // Minimize CSS files
    
    console.log(`Page loaded in ${loadTime}ms with ${cssFiles} CSS files`);
  });

  test('Cumulative Layout Shift (CLS)', async ({ page }) => {
    await page.goto('/');
    
    // Wait for any layout shifts to settle
    await page.waitForTimeout(2000);
    
    const cls = await page.evaluate(() => {
      return new Promise((resolve) => {
        let clsValue = 0;
        new PerformanceObserver((list) => {
          for (const entry of list.getEntries()) {
            if (!entry.hadRecentInput) {
              clsValue += entry.value;
            }
          }
          resolve(clsValue);
        }).observe({entryTypes: ['layout-shift']});
        
        // Timeout after 3 seconds
        setTimeout(() => resolve(clsValue), 3000);
      });
    });
    
    // Industry standard: CLS < 0.1
    expect(cls).toBeLessThan(0.1);
    console.log(`Cumulative Layout Shift: ${cls}`);
  });
});
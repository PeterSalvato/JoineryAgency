const { test, expect } = require('@playwright/test');

test.describe('Cross-Browser Compatibility', () => {
  test('Basic functionality across browsers', async ({ page, browserName }) => {
    await page.goto('/');
    
    // Test that page loads successfully
    await expect(page).toHaveTitle(/Design & Development Consultancy/);
    
    // Test that CSS is loading
    const hasStyles = await page.evaluate(() => {
      const body = document.body;
      const computed = window.getComputedStyle(body);
      return computed.fontFamily !== '' && computed.fontSize !== '';
    });
    
    expect(hasStyles).toBe(true);
    
    // Test responsive design
    await page.setViewportSize({ width: 375, height: 667 }); // Mobile
    const mobileWidth = await page.evaluate(() => document.body.offsetWidth);
    expect(mobileWidth).toBeLessThanOrEqual(375);
    
    await page.setViewportSize({ width: 1920, height: 1080 }); // Desktop
    const desktopWidth = await page.evaluate(() => document.body.offsetWidth);
    expect(desktopWidth).toBeGreaterThan(375);
    
    console.log(`${browserName}: Mobile width=${mobileWidth}px, Desktop width=${desktopWidth}px`);
  });

  test('Navigation functionality', async ({ page }) => {
    await page.goto('/');
    
    // Find navigation links
    const navLinks = await page.locator('nav a, .nav a, [role="navigation"] a').count();
    expect(navLinks).toBeGreaterThan(0);
    
    // Test that links are clickable (not testing actual navigation to avoid 404s)
    const firstLink = page.locator('nav a, .nav a, [role="navigation"] a').first();
    const href = await firstLink.getAttribute('href');
    
    expect(href).toBeTruthy();
    console.log(`Found ${navLinks} navigation links, first href: ${href}`);
  });
});
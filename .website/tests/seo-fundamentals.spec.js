const { test, expect } = require('@playwright/test');

test.describe('SEO Fundamentals', () => {
  test('Meta tags and structured data', async ({ page }) => {
    await page.goto('/');
    
    // Title tag
    const title = await page.title();
    expect(title.length).toBeGreaterThan(10);
    expect(title.length).toBeLessThan(70); // Google's recommended length
    
    // Meta description
    const description = await page.locator('meta[name="description"]').getAttribute('content');
    expect(description).toBeTruthy();
    expect(description.length).toBeGreaterThan(50);
    expect(description.length).toBeLessThan(160);
    
    // Language declaration
    const lang = await page.locator('html').getAttribute('lang');
    expect(lang).toBeTruthy();
    
    // Open Graph tags (social sharing)
    const ogTitle = await page.locator('meta[property="og:title"]').getAttribute('content');
    const ogDescription = await page.locator('meta[property="og:description"]').getAttribute('content');
    
    expect(ogTitle || title).toBeTruthy();
    expect(ogDescription || description).toBeTruthy();
    
    console.log(`Title: "${title}" (${title.length} chars)`);
    console.log(`Description: "${description}" (${description?.length || 0} chars)`);
    console.log(`Language: ${lang}`);
  });

  test('Heading structure and content hierarchy', async ({ page }) => {
    await page.goto('/');
    
    // Check heading hierarchy
    const headings = await page.evaluate(() => {
      const headingElements = Array.from(document.querySelectorAll('h1, h2, h3, h4, h5, h6'));
      return headingElements.map(h => ({
        level: parseInt(h.tagName.substring(1)),
        text: h.textContent.trim().substring(0, 50)
      }));
    });
    
    // Should have exactly one H1
    const h1Count = headings.filter(h => h.level === 1).length;
    expect(h1Count).toBe(1);
    
    // Headings should follow logical order (no skipping levels)
    let previousLevel = 0;
    for (const heading of headings) {
      if (heading.level > previousLevel + 1 && previousLevel > 0) {
        console.warn(`Heading hierarchy skip: H${previousLevel} to H${heading.level}`);
      }
      previousLevel = Math.min(heading.level, previousLevel + 1);
    }
    
    console.log(`Found ${headings.length} headings, ${h1Count} H1 tags`);
    headings.forEach(h => console.log(`  H${h.level}: ${h.text}`));
  });

  test('Page loading and technical SEO', async ({ page }) => {
    await page.goto('/');
    
    // Check for robots meta tag
    const robots = await page.locator('meta[name="robots"]').getAttribute('content');
    
    // Check for canonical URL
    const canonical = await page.locator('link[rel="canonical"]').getAttribute('href');
    
    // Check for favicon
    const favicon = await page.locator('link[rel="icon"], link[rel="shortcut icon"]').count();
    expect(favicon).toBeGreaterThan(0);
    
    // Verify HTTPS (if applicable)
    const url = page.url();
    if (url.includes('localhost')) {
      console.log('Local development - HTTPS check skipped');
    } else {
      expect(url).toMatch(/^https:/);
    }
    
    console.log(`Robots: ${robots || 'Not specified'}`);
    console.log(`Canonical: ${canonical || 'Not specified'}`);
    console.log(`Favicon: ${favicon > 0 ? 'Present' : 'Missing'}`);
  });
});
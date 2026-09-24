import { createRequire } from 'node:module';
const puppeteer = createRequire('C:/Users/DELL/site-to-pdf/package.json')('puppeteer');
import fs from 'node:fs';
fs.mkdirSync('shots/t', { recursive: true });
const browser = await puppeteer.launch({ headless: 'new', args: ['--no-sandbox'] });
for (const [name, vp] of [['desk', { width: 1440, height: 900 }], ['mob', { width: 390, height: 844, deviceScaleFactor: 2, isMobile: true, hasTouch: true }]]) {
  const page = await browser.newPage(); await page.setViewport(vp);
  await page.goto('http://localhost:5412/index.html', { waitUntil: 'networkidle0' });
  await page.addStyleTag({ content: '.rv,.blk{opacity:1!important;transform:none!important;filter:none!important}.w i{transform:none!important;opacity:1!important;transition:none!important}.comp .it{opacity:1!important;transform:none!important}' });
  const n = await page.evaluate(() => document.querySelectorAll('h1,h2,h3,.quote,.big,.abra,.plans-key,.ou').length);
  for (let i = 0; i < n; i++) {
    await page.evaluate(i => { const el = document.querySelectorAll('h1,h2,h3,.quote,.big,.abra,.plans-key,.ou')[i]; const y = el.getBoundingClientRect().top + scrollY - 140; scrollTo({ top: y, behavior: 'instant' }); }, i);
    await new Promise(r => setTimeout(r, 400));
    const box = await page.evaluate(i => { const r = document.querySelectorAll('h1,h2,h3,.quote,.big,.abra,.plans-key,.ou')[i].getBoundingClientRect(); return { x: Math.max(0, r.x - 16), y: Math.max(0, r.y + scrollY - 30), w: Math.min(innerWidth - Math.max(0, r.x - 16), r.width + 32), h: r.height + 60 }; }, i);
    if (box.h < 20 || box.w < 20) continue;
    await page.screenshot({ path: `shots/t/${name}-${String(i).padStart(2, '0')}.png`, clip: { x: box.x, y: box.y, width: box.w, height: box.h }, captureBeyondViewport: true });
  }
  await page.close();
}
await browser.close();

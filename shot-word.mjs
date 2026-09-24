import { createRequire } from 'node:module';
const puppeteer = createRequire('C:/Users/DELL/site-to-pdf/package.json')('puppeteer');
const browser = await puppeteer.launch({ headless: 'new', args: ['--no-sandbox'] });
const page = await browser.newPage(); await page.setViewport({ width: 1440, height: 900, deviceScaleFactor: 2 });
await page.goto('http://localhost:5412/index.html', { waitUntil: 'networkidle0' });
await page.evaluate(() => document.fonts.ready);
// 1) título dos planos ainda escondido (antes de entrar): nada pode vazar
await page.evaluate(() => { const el = document.querySelector('#planos h2'); scrollTo({ top: el.getBoundingClientRect().top + scrollY - 1500, behavior: 'instant' }); });
await new Promise(r => setTimeout(r, 300));
let b = await page.evaluate(() => { const r = document.querySelector('#planos h2').getBoundingClientRect(); return { x: r.x - 20, y: r.y + scrollY - 40, width: r.width + 40, height: r.height + 80 }; });
await page.screenshot({ path: 'shots/t/word-hidden.png', clip: b, captureBeyondViewport: true });
// 2) revelado
await page.evaluate(() => { const el = document.querySelector('#planos h2'); scrollTo({ top: el.getBoundingClientRect().top + scrollY - 300, behavior: 'instant' }); });
await new Promise(r => setTimeout(r, 2500));
b = await page.evaluate(() => { const r = document.querySelector('#planos h2').getBoundingClientRect(); return { x: r.x - 20, y: r.y + scrollY - 40, width: r.width + 40, height: r.height + 80 }; });
await page.screenshot({ path: 'shots/t/word-shown.png', clip: b, captureBeyondViewport: true });
await browser.close();

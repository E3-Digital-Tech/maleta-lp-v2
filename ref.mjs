import { createRequire } from 'node:module';
const puppeteer = createRequire('C:/Users/DELL/site-to-pdf/package.json')('puppeteer');
const browser = await puppeteer.launch({ headless: 'new', args: ['--no-sandbox'] });
const page = await browser.newPage(); await page.setViewport({ width: 1440, height: 900 });
await page.goto('https://comunidadecutpro.com/presets-dinamicos/', { waitUntil: 'networkidle2', timeout: 60000 });
await new Promise(r => setTimeout(r, 2500));
await page.screenshot({ path: 'shots/ref-0.jpg', type: 'jpeg', quality: 80 });
await page.evaluate(() => scrollTo(0, 900)); await new Promise(r => setTimeout(r, 1500));
await page.screenshot({ path: 'shots/ref-1.jpg', type: 'jpeg', quality: 80 });
const info = await page.evaluate(() => {
  const out = [];
  const els = [document.documentElement, document.body, ...document.querySelectorAll('body > *, section, header, main, div')];
  for (const el of els.slice(0, 400)) {
    const cs = getComputedStyle(el); const r = el.getBoundingClientRect();
    if (r.width < 600 || r.height < 300) continue;
    const bg = cs.backgroundImage + ' ' + cs.backgroundColor;
    if (bg.includes('gradient') || bg.includes('url') || (cs.backgroundColor !== 'rgba(0, 0, 0, 0)' && cs.backgroundColor !== 'rgb(0, 0, 0)'))
      out.push({ tag: el.tagName, cls: (el.className||'').toString().slice(0,80), w: r.width|0, h: r.height|0, bgc: cs.backgroundColor, bgi: cs.backgroundImage.slice(0, 300), pos: cs.position });
  }
  const canv = [...document.querySelectorAll('canvas,video')].map(c => ({ tag: c.tagName, w: c.width, h: c.height, cls: c.className, src: c.src }));
  return { out: out.slice(0, 25), canv };
});
console.log(JSON.stringify(info, null, 1));
await browser.close();

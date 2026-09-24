// Screenshots da LP em vários pontos do scroll, desktop e mobile.
// uso: node shot.mjs [porta]   (servidor: python -m http.server <porta> na pasta)
import { createRequire } from 'node:module';
const puppeteer = createRequire('C:/Users/DELL/site-to-pdf/package.json')('puppeteer');
import fs from 'node:fs';
const port = process.argv[2] || 5410;
const page = process.argv[3] || "index.html";
const url = `http://localhost:${port}/${page}`;
const pre = page.replace(/.html$/, "").replace("index", "");
fs.mkdirSync('shots', { recursive: true });
const browser = await puppeteer.launch({ headless: 'new', args: ['--no-sandbox'] });
async function run(name, vp, stops) {
  const page = await browser.newPage();
  await page.setViewport(vp);
  await page.goto(url, { waitUntil: 'networkidle0' });
  await new Promise(r => setTimeout(r, 1200));
  const total = await page.evaluate(() => document.documentElement.scrollHeight - innerHeight);
  for (const s of stops) {
    const y = Math.round(total * s);
    await page.evaluate(y => window.scrollTo({ top: y, behavior: 'instant' }), y);
    await new Promise(r => setTimeout(r, 900));
    await page.screenshot({ path: `shots/${pre?pre+"-":""}${name}-${String(Math.round(s * 100)).padStart(2, '0')}.jpg`, type: 'jpeg', quality: 80 });
  }
  console.log(name, 'total scroll', total);
  await page.close();
}
await run('desk', { width: 1440, height: 900 }, [0, .05, .10, .15, .20, .27, .33, .40, .47, .53, .60, .66, .72, .78, .84, .90, .96, 1]);
await run('mob', { width: 390, height: 844, deviceScaleFactor: 2, isMobile: true, hasTouch: true }, [0, .06, .12, .18, .25, .33, .42, .50, .58, .66, .74, .82, .90, 1]);
await browser.close();

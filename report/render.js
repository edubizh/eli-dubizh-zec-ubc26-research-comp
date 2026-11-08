const puppeteer = require('puppeteer');
const path = require('path');

(async () => {
  const browser = await puppeteer.launch({
    headless: 'new',
    executablePath: '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome',
    args: ['--no-sandbox'],
  });
  const page = await browser.newPage();
  const file = 'file://' + path.resolve(__dirname, 'report.html');
  await page.goto(file, { waitUntil: 'networkidle0' });
  // give the inline chart script a tick to paint
  await new Promise(r => setTimeout(r, 400));
  await page.pdf({
    path: path.resolve(__dirname, 'Solana_SOL_Long_Thesis_UBC2026.pdf'),
    format: 'Letter',
    printBackground: true,
    preferCSSPageSize: true,
  });
  await browser.close();
  console.log('PDF written');
})();

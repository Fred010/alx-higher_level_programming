#!/usr/bin/node

const fs = require('fs');
const https = require('https');

if (process.argv.length !== 4) {
  console.error('Usage: ./5-request_store.js <URL> <file_path>');
  process.exit(1);
}

const url = process.argv[2];
const filePath = process.argv[3];

https.get(url, (res) => {
  let body = '';
  res.setEncoding('utf-8');
  res.on('data', (data) => {
    body += data;
  });
  res.on('end', () => {
    fs.writeFile(filePath, body, { encoding: 'utf-8' }, (err) => {
      if (err) {
        console.error('Error writing file:', err);
        process.exit(1);
      }
      console.log(`Successfully saved the contents of ${url} to ${filePath}`);
    });
  });
}).on('error', (err) => {
  console.error('Error fetching URL:', err);
  process.exit(1);
});

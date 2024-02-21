#!/usr/bin/node

const fs = require('fs');

const [filePath, stringToWrite] = process.argv.slice(2);

fs.writeFile(filePath, stringToWrite, 'utf-8', (err) => {
  if (err) {
    console.error(err);
  }
});

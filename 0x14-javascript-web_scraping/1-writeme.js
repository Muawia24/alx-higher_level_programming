#!/usr/bin/node

const fs = require('node:fs');

const args = process.argv.slice(2);
const filePath = args[0];
const content = args[1];

fs.writeFile(filePath, content, 'utf8', (err, data) => {
  if (err) {
    console.error(err);
  }
  console.log(data);
});

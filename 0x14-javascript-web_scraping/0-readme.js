#!/usr/bin/node

const fs = require('node:fs');

const args = process.argv.slice(2);

const filePath = args[0];

fs.readFile(filePath, 'utf8', (err, data) => {
  if (err) {
    console.error(err);
  }
  console.log(data);
});

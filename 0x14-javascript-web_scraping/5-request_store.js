#!/usr/bin/node

const request = require('request');
const fs = require('node:fs');
const args = process.argv.slice(2);

const url = args[0];
const filePath = args[1];
request(url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    fs.writeFile(filePath, body, 'utf8', err => {
      if (err) {
        console.log(err);
      }
    });
  }
});

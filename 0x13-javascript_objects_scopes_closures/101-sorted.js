#!/usr/bin/node
const dict = require('./101-data.js').dict;
const dict1 = {};
for (const key in dict) {
  if (!dict1[dict[key]]) {
    dict1[dict[key]] = [key];
  } else {
    dict1[dict[key]].push(key);
  }
}
console.log(dict1);

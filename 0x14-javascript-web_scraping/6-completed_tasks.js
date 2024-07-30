#!/usr/bin/node

const request = require('request');
const args = process.argv.slice(2);
const url = args[0];
const userDict = {};

request(url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    const data = JSON.parse(body);

    for (let i = 0; i < data.length; i++) {
      const id = data[i].userId;
      let count = 0;
      for (let j = 0; j < data.length; j++) {
        if (data[j].userId === id) {
          if (data[j].completed === true) {
            count += 1;
          }
        }
      }
      userDict[String(id)] = count;
    }
  }
  console.log(userDict);
});

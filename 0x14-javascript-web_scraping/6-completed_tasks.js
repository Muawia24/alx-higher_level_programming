#!/usr/bin/node

const request = require('request');
const args = process.argv.slice(2);
const url = args[0];
const userDict = {};

request(url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    body = JSON.parse(body);

    for (let i = 0; i < body.length; i++) {
      const id = body[i].userId;
      let count = 0;
      for (let j = 0; j < body.length; j++) {
        if (body[j].userId === id) {
          if (body[j].completed === true) {
            count += 1;
          }
        }
      }
      userDict[String(id)] = count;
    }
    console.log(userDict);
  }
});

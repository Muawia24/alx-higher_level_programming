#!/usr/bin/node

const request = require('request');
const args = process.argv.slice(2);

const id = args[0];
const url = 'https://swapi-api.alx-tools.com/api/films/' + id;
request(url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    body = JSON.parse(body);
    console.log(body.title);
  }
});

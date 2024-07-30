#!/usr/bin/node

const request = require('request');
const args = process.argv.slice(2);
const url = args[0];
const character = 'https://swapi-api.alx-tools.com/api/people/18/';

request(url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    let count = 0;
    const films = JSON.parse(body).results;

    for (let result = 0; result < films.length; result++) {
      if (films[result].characters.includes(character)) {
        count += 1;
      }
    }
    console.log(count);
  }
});

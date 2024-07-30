#!/usr/bin/node

const request = require('request');
const args = process.argv.slice(2);

const id = args[0];
const url = 'https://swapi-api.alx-tools.com/api/films/' + id;
request.get(url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    const characters = JSON.parse(body).characters;
    characters.forEach(actor => {
      request.get(actor, function (error, response, body) {
        if (error) {
          console.log(error);
        } else {
          const data = JSON.parse(body);
          console.log(data.name);
        }
      });
    });
  }
});

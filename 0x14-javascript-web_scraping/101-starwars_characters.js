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
    const promList = [];
    characters.forEach((actor, index) => {
      promList.push(new Promise((resolve, reject) => {
        request.get(actor, function (error, response, body) {
          if (error) {
            reject(error);
          } else {
            const data = JSON.parse(body);
            resolve(data.name);
          }
        });
      }));
    });
    Promise.all(promList).then(names => {
      names.forEach(name => {
        console.log(name);
      });
    });
  }
});

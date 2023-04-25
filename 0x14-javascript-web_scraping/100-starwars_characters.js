#!/usr/bin/node
const request = require('request');
const url = 'https://swapi-api.alx-tools.com/api/films/' + process.argv[2];
request.get(url, function (err, response, body) {
  if (err) { return console.error(err); }
  const actors = JSON.parse(body).characters;
  for (const actor of actors) {
    request.get(actor, function (error, resp, person) {
      if (err) { return console.error(error); }
      console.log(JSON.parse(person).name);
    });
  }
});

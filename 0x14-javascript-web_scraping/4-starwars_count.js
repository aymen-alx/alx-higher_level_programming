#!/usr/bin/node
const request = require('request');
request.get(process.argv[2], function (error, data, body) {
  if (error) { return console.error(error); }
  let count = 0;
  const result = JSON.parse(body).results;
  for (const film of result) {
    for (const actor of film.characters) {
      if (actor.endsWith('18/')) {
        count++;
      }
    }
  }
  console.log(count);
});

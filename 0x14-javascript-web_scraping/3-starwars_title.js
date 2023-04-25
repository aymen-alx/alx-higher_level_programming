#!/usr/bin/node
const request = require('request');
const url = 'https://swapi-api.alx-tools.com/api/films/' + process.argv[2];
request.get(url, function (error, data, body) {
  if (error) { return console.error(error); }
  console.log(JSON.parse(body).title);
});

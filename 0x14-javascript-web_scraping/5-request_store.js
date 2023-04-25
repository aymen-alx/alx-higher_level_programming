#!/usr/bin/node
const fs = require('fs');
const request = require('request');
request.get(process.argv[2], function (error, response, body) {
  if (error) { return console.error(error); }
  fs.writeFile(process.argv[3], body, function (err) {
    if (err) { return console.error(err); }
  });
});

#!/usr/bin/node
const request = require('request');
request.get(process.argv[2], function (error, data) {
  if (error) { return console.error(error); }
  console.log('code:', data.statusCode);
});

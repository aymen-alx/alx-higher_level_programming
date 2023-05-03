#!/usr/bin/node
const fs = require('fs');
fs.readFile(process.argv[2], 'utf8', function (error, data) {
  if (error) { return console.error(error); }
  console.log(data);
});
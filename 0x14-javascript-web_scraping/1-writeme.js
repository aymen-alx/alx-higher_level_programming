#!/usr/bin/node
const fs = require('fs');
fs.writeFile(process.argv[2], process.argv[3], 'utf8', function (error, data) {
  if (error) { return console.error(error); }
});

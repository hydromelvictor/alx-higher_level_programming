#!/usr/bin/node
const fs = require('fs');
fs.readFile(process.argv[2], 'utf8', (error, body) => {
  if (error) console.log(error);
  console.log(body);
});

#!/usr/bin/node
const fs = require ('fs');
const process = require('process');
const file = process.argv[2];
fs.readFile (file, 'utf8', (error, body) =>
{
    if (error) console.log(error);
    console.log(body);
});
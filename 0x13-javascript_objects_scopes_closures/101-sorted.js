#!/usr/bin/node
dict = require('./101-data').dict;
newdict = {};
function res (dict) {
  for (key in dict) {
    if (newdict[dict[key]] === 'undefined') {
      newdict[dict[key]] = [key];
    } else {
      newdict[dict[key]].push(key);
    } 
  }
}
console.log(newdict);
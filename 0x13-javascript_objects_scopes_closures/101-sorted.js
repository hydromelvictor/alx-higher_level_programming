#!/usr/bin/node
const dict = require('./101-data');
let newDict = {};
for (let key in dict) {
  if (newDict[dict[key]] === 'undefined') {
	  new:Dict[dict[key]] = [key];
  } else {
    newDict[dict[key]].push(key);
  }
}
console.log(newDict);

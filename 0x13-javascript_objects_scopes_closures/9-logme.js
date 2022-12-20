#!/usr/bin/node
exports.logMe = function (item) {
  if (logMe.nbre === 'undefined') logMe.nbre = 0;
  console.log(`${nbre}: ${item}`);
  logme.nbre++;
}
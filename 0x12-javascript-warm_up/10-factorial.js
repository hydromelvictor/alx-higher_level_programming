#!/usr/bin/node
function factoriel (a) {
  if (isNaN(a) || a === 0) return 1;
  return (a * factoriel(a - 1));
}
const a = Math.floor(Number(process.argv[2]));
console.log(factoriel(a));

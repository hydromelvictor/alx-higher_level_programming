#!/usr/bin/node
function pusher (args) {
  let nbre = [];
  let n = args.length;
  let i = 2;
  while (i < n) {
    nbre.push(Math.floor(Number(args[i])));
    i++;
  }
  return nbre;
}

function maxi (nbre) {
  let max = 2;
  for (let i = 2; i < nbre.length; i++) {
    if (nbre[max] < nbre[i]) max = i; 
  }
  return max;
}

let i = 0;
if (process.argv.length <= 3) {
  console.log(0);
} else {
  let n = pusher(process.argv);
  n.pop(maxi(n));
  console.log(process.argv[maxi(n)]);
}

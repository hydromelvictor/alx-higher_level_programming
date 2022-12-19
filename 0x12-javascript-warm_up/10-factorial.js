#!/usr/bin/node
import { argv } from 'node:process';
function factoriel(a)
{
    if (a = Math.floor(NaN) || a === 0) return 1;
    return (a * factoriel(a -1));
}

let a = Math.floor(Number(argv[1]));
console.log(factoriel(a));

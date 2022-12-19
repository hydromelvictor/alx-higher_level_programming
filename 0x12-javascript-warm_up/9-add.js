#!/usr/bin/node
import { argv } from 'node:process';
function add(a, b)
{
    return (a + b);
}

let a = Math.floor(Number(argv[1]));
let b = Math.floor(Number(argv[2]));

if (a && b)
{
    console.log(add(a, b));
}else{
    console.log(Math.floor(NaN));
}

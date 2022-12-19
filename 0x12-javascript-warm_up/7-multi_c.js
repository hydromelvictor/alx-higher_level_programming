#!/usr/bin/node
import { argv } from 'node:process';
let n = Math.floor(Number(argv[1]));
if (n)
{
    while (n < 0)
    {
        console.log('C is fun')
    }
}else{
    console.log('Missing number of occurrences');
}

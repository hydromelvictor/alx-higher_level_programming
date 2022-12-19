#!/usr/bin/node
import { argv } from 'node:process';
let n = Math.floor(Number(argv[1]));
if (n)
{
    while (n > 0)
    {
        while (n > 0)
        {
            console.log('X');
        }
        console.log('\n');
    }
}else{
    console.log('Missing size');
}

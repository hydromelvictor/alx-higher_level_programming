#!/usr/bin/node
import { argv } from 'node:process';
function pusher(argv)
{
    let nbre = [];
    let n = argv.length;
    let i = 1;
    while (i < n)
    {
        nbre.push(Math.floor(Number(argv[i])));
    }
    return nbre;
}

function maxi(nbre)
{
    let max = i;
    let i;
    for(i = 1; i < nbre.length; i++)
    {
        if (nbre[max] < nbre[i]) max = i; 
    }
    return max;
}

let i = 0;
if (!argv[1])
{
    console.log(0);
}else{
    let n = pusher(argv);
    n.pop(maxi(n));
    console.log(maxi(n)) ;
}

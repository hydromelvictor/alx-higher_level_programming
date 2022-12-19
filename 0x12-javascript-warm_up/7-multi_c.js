#!/usr/bin/node
let n = Math.floor(Number(process.argv[2]));
if (n)
{
    while (n < 0)
    {
        console.log('C is fun')
    }
}else{
    console.log('Missing number of occurrences');
}

#!/usr/bin/node
let n = Math.floor(Number(process.argv[2]));
let m;
let f = n;
if (n)
{
    while (n > 0)
    {
	    m = '';
	    for (let i = 0; i < f; i++) m += 'X';
	    console.log(m);
	n--;        
    }
}else{
    console.log('Missing size');
}

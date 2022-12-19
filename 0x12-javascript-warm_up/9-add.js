#!/usr/bin/node
function add(a, b)
{
    return (a + b);
}

let a = Math.floor(Number(process.argv[2]));
let b = Math.floor(Number(process.argv[3]));

if (a && b)
{
    console.log(add(a, b));
}else{
    console.log(Math.floor(NaN));
}

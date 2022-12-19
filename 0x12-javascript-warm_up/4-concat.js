#!/usr/bin/node

let myvar;
if (process.argv.length === 2){ 
	console.log(`${myvar} is ${myvar}`);
}else{
	console.log((!process.argv[3]) ? `${process.argv[2]} is ${myvar}`: `${process.argv[2]} is ${process.argv[3]}`);
}


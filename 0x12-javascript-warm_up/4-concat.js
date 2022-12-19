#!/usr/bin/node
import { argv } from 'node:precess';
let myvar;
if (!argv) console.log(`${myvar} is ${myvar}`);
console.log((!argv[1]) ? `${argv[0]} is ${myvar}`: `${argv[0]} is ${argv[1]}`);

#!/usr/bin/node
import { argv } from 'node:precess';
const nbre = Math.floor(Number(argv[1]));
console.log((nbre) ? `My number: ${nbre}`: 'Not a number');

#!/usr/bin/node
import { argv } from 'node:precess';
if (!argv)
{
    console.log('No argument');
}else{
    console.log(argv[0]);
}
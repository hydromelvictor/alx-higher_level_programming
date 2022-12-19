#!/usr/bin/node
import { argv } from 'node:precess';

if (!argv)
{
    console.log('No argument');
}else{
    console.log((argv[1]) ? 'Arguments found' : 'Argument found');
}

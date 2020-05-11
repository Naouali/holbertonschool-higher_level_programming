#!/usr/bin/node
const arr = require('./100-data.js').list;
const m = arr.map(x => arr.indexOf(x) * x);
console.log(arr);
console.log(m);

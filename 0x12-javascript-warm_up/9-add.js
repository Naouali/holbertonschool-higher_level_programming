#!/usr/bin/node
const aa = process.argv[2];
const bb = process.argv[3];

function add (a, b) {
  return parseInt(a) + parseInt(b);
}
console.log(add(aa, bb));

#!/usr/bin/node
let f = process.argv[2];
function factorial(n) {
  if (n === 1) {
    return 1;
  } else {
    return (n * factorial(n - 1));
  }
  console.log(factorial(f));

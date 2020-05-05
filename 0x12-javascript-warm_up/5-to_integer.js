#!/usr/bin/node
const first = parseInt(process.argv[2]);
if (isNaN(first)) {
  console.log('Not a number');
} else {
  console.log('My number: ' + first);
}

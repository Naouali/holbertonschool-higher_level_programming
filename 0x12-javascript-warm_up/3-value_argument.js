#!/usr/bin/node
let args = process.argv.slice(2);
let len = args.length;
if (len > 0) {
  console.log(process.argv[2]);
} else {
  console.log('No argument');
}

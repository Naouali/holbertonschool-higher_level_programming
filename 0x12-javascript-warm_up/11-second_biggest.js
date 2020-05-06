#!/usr/bin/node
const args = process.argv.slice(2);
const len = args.length;
if (len <= 1) {
  console.log(0);
} else {
  let sorted = args.sort();
  sorted = sorted.reverse();
  console.log(sorted[1]);
}

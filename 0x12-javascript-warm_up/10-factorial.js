#!/usr/bin/node
const f = process.argv[2];
function factorial (f) {
  if (f > 1) {
    return (f * factorial(f - 1));
  } else if (f === 1) {
    return 1;
  }
}
if (f === undefined || !typeof (f)) {
  console.log(1);
} else {
  console.log(factorial(f));
}

#!/usr/bin/node
const dic = require('./101-data').dict;

const newdic = {};

for (const [key, value] of Object.entries(dic)) {
  if (newdic[value] !== undefined) {
    newdic[value].push(key);
  } else {
    newdic[value] = [key];
  }
}

console.log(newdic);

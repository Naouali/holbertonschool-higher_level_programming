#!/usr/bin/node
const request = require('request');
const fs = require('fs');
request(process.argv[2], (err, res, body) => {
  if (err) {
    console.log(err);
  } else {
    const store = body;
    fs.writeFile(process.argv[3], store, 'utf8', (error) => {
      if (error) {
        console.log(error);
      }
    });
  }
});

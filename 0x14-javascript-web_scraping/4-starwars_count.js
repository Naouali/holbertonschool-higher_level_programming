#!/usr/bin/node
const request = require('request');
request(process.argv[2], { json: true }, (err, res, body) => {
  if (err) { return console.log(err); }
  let i, j;
  const rslt = body.results;
  let n = 0;
  if (rslt !== undefined) {
    for (i = 0; i < rslt.length; i++) {
      const car = rslt[i].characters;
      for (j = 0; j < car.length; j++) {
        if (car[j] === 'https://swapi-api.hbtn.io/api/people/18/') {
          n++;
          break;
        }
      }
    }
  }
  console.log(n);
});

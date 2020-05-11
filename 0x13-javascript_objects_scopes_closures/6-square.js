#!/usr/bin/node
class Square extends require('./5-square.js') {
  charPrint (c) {
    if (c === undefined) {
      super.print();
    } else {
      for (let x = 0; x < this.height; x++) {
        for (let y = 0; y < this.width; y++) {
          process.stdout.write('C');
        }
        console.log();
      }
    }
  }
}
module.exports = Square;

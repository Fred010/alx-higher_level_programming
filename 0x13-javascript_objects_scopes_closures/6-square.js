#!/usr/bin/node
const SquareP = require('./5-square');

class Square extends SquareP {
  charPrint (c) {
    if (c === undefined) {
      c = 'X';
    }
    for (let id1 = 0; id1 < this.height; id1++) {
      let f = '';
      for (let id2 = 0; id2 < this.width; id2++) {
        f += c;
      }
      console.log(f);
    }
  }
}

module.exports = Square;

#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if ((w > 0) && (h > 0)) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let id1 = 0; id1 < this.height; id1++) {
      let f = '';
      for (let id2 = 0; id2 < this.width; id2++) {
        f += 'X';
      }
      console.log(f);
    }
  }

  rotate () {
    const backup = this.width;
    this.width = this.height;
    this.height = backup;
  }

  double () {
    this.width *= 2;
    this.height *= 2;
  }
}

module.exports = Rectangle;

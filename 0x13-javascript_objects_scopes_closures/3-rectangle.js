#!/usr/bin/node
module.exports = class Rectangle {
  constructor (w, h) {
    if (typeof (h) === 'number' && typeof (w) === 'number' && h > 0 && w > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let i = 0; i < this.height; i++) {
      let m = '';
      for (let j = 0; j < this.width; j++) m += 'X';
      console.log(m);
    }
  }
};

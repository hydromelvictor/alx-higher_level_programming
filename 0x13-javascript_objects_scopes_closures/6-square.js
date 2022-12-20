#!/usr/bin/node
const Rectangle = require('./4-rectangle').Rectangle;

class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    if (!c) {
      super.print();
    } else {
      let m = '';
      for (let i = 0; i < this.height; i++) {
        for (let j = 0; j < this.width; j++) m += c;
        console.log(m);
      }
    }
  }
}
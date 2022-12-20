#!/usr/bin/node
const Rectangle = require('./4-rectangle');

module.exports = class Square extends Rectangle {
  charPrint (c) {
    if (!c) {
      this.print();
    } else {
      for (let i = 0; i < this.height; i++) {
	let m = '';
        for (let j = 0; j < this.width; j++) m += c;
        console.log(m);
      }
    }
  }
};

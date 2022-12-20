#!/usr/bin/node
module.exports = class Rectangle {
  constructor (w, h) {
    if (typeof(h) === 'number' && typeof(w) === 'number' && h > 0 && w > 0) {
      this.width = w;
      this.height = h;
    }  
  }
};

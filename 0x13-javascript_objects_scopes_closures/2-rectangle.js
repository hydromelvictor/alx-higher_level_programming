#!/usr/bin/node
class Rectangle {
  constructor (h, w) {
    if (typeof(h) === 'number' && typeof(w) === 'number' && h === 0 && w === 0) {
      this.width = w;
      this.height = h;
    }  
  }
}
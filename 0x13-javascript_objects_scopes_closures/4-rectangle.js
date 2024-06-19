#!/usr/bin/node
module.exports = class Rectangle {
  constructor (w, h) {
    if (h > 0 && w > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    let str1 = '';
    let i;
    let j;
    for (i = 0; i < this.height; i++) {
      for (j = 0; j < this.width; j++) {
        str1 += 'X';
      }
      console.log(str1);
      str1 = '';
    }
  }

  rotate () {
    const temp = this.width;
    this.width = this.height;
    this.height = temp;
  }

  double () {
    this.width *= 2;
    this.height *= 2;
  }
};

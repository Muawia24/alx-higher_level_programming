#!/usr/bin/node
const Square1 = require('./5-square.js');
module.exports = class Square extends Square1 {
  charPrint (c) {
    if (c) {
      let str1 = '';
      let i;
      let j;
      for (i = 0; i < this.height; i++) {
        for (j = 0; j < this.width; j++) {
          str1 += c;
        }
        console.log(str1);
        str1 = '';
      }
    } else {
      this.print();
    }
  }
};

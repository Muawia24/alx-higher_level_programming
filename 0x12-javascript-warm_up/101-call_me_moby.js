#!/usr/bin/node
let i;
exports.callMeMoby = function (x, theFunction) {
  if (!x) {
    console.log('Missing number of occurrences');
  } else {
    for (i = 0; i < x; i++) {
      theFunction();
    }
  }
};

#!/usr/bin/node

exports.addMeMaybe = function (x, theFunction) {
  if (!x) {
    console.log('Missing number of occurrences');
  } else {
    theFunction(x + 1);
  }
};

#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  let i;
  let count = 0;
  for (i = 0; list[i]; i++) {
    if (list[i] === searchElement) {
      count += 1;
    }
  }
  return count;
};

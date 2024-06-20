#!/usr/bin/node
exports.esrever = function (list) {
  let len = list.length - 1;
  let i;
  const rev = [];
  for (i = 0; list[len]; i++) {
    rev[i] = list[len];
    len--;
  }
  return rev;
};

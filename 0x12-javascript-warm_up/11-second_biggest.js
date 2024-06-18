#!/usr/bin/node
const args = process.argv;
const len = args.length;

function secMax (args) {
  if (len <= 3) {
    return 0;
  }
  let i;
  const arr = [];
  for (i = 2; i < len; i++) {
    arr.push(args[i]);
  }
  arr.sort();
  arr.reverse();
  return arr[1];
}
console.log(secMax(args));

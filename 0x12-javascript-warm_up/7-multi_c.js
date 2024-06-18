#!/usr/bin/node
const arg1 = process.argv[2];
const num = Number(arg1);
let i;

if (!num) {
  console.log('Missing number of occurrences');
} else {
  for (i = 0; i < num; i++) {
    console.log('C is fun');
  }
}

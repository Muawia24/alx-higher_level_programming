#!/usr/bin/node
const arg1 = process.argv[2];
const num = Number(arg1);
if (!num) {
  console.log('Not a number');
} else {
  console.log(`My number: ${num}`);
}

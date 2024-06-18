#!/usr/bin/node
const arg1 = process.argv[2];
const num = Number(arg1);
let i, j;

if (!num) {
  console.log('Missing size');
} else {
  const str1 = 'X';
  let dup = '';
  for (i = 0; i < num; i++) {
    for (j = 0; j < num; j++) {
      dup += str1;
    }
    console.log(dup);
    dup = '';
  }
}

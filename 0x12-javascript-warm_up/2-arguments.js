#!/usr/bin/node
const arg = process.argv;
const len = arg.length - 2;

if (len < 1) {
  console.log('No argument');
} else if (len === 1) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}

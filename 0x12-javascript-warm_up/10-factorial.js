#!/usr/bin/node
const num1 = Number(process.argv[2]);

function factorial (num) {
  let fac = 1;
  if (!num) {
    return fac;
  } else {
    fac = num * factorial(num - 1);
  }
  return fac;
}
console.log(factorial(num1));

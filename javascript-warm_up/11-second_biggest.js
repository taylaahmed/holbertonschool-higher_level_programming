#!/usr/bin/node

let i = 2;
const array = [];

while (process.argv[i] !== undefined) {
  array.push(Number(process.argv[i]));
  i++;
}

if (array.length === 0 || array.length === 1) {
  console.log(0);
} else {
  array.sort((a, b) => a - b);
  console.log(array[array.length - 2]);
}

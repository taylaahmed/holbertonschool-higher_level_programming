#!/usr/bin/node

const size = Number(process.argv[2]);
let i = 0;
const array = [];

if (isNaN(size)) {
  console.log('Missing size');
} else {
  while (i < size) {
    array.push('X');
    i++;
  }
  i = 0;

  while (i < size) {
    console.log(array.join(''));
    i++;
  }
}

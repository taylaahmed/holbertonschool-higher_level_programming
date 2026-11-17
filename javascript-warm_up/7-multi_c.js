#!/usr/bin/node

const count = Number(process.argv[2]);
let i = 0;

if (isNaN(count)) {
  console.log('Missing number of occurrences');
} else {
  while (i < count) {
    console.log('C is fun');
    i++;
  }
}

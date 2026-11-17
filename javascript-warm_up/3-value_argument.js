#!/usr/bin/node

const print = process.argv[2];

if (print === undefined) {
  console.log('No argument');
} else {
  console.log(process.argv[2]);
}

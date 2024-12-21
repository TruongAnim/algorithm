"use strict";
// https://codeforces.com/problemset/problem/1352/C

// Util
const fs = require("fs");

let input = [];
let readIndex = 0;
let readInput = () => {
  fs.readFile("input.txt", "utf8", (err, data) => {
    input = data.split("\n");
    main();
  });
};
readInput();

function readline() {
  return input[readIndex++];
}

function print(...args) {
  console.log(...args);
}

// solving start
const checkNumber = (n, k, x) => {
  let a = Math.floor(x / n);
  if (x - a >= k) {
    return true;
  }
  return false;
};

const binarySearch = (left, right, n, k) => {
  while (left < right) {
    const mid = Math.floor((left + right) / 2);
    if (checkNumber(n, k, mid)) {
      right = mid;
    } else {
      left = mid + 1;
    }
  }
  return right;
};

function main() {
  const test = +readline();
  for (let t = 0; t < test; t++) {
    let l = readline().trim().split(" ").map(Number);
    let a = l[0];
    let b = l[1];
    print(binarySearch(1, Math.pow(10, 10) + 1, a, b));
  }
}

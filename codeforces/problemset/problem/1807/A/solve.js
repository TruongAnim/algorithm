"use strict"
// https://codeforces.com/problemset/problem/1807/A

// Util
const fs = require('fs');

let input = []
let readIndex = 0
let readInput = () => {
    fs.readFile('input.txt', 'utf8', (err, data) => {
        input = data.split('\n');
        main()
    })
}
readInput()

function readline() {
    return input[readIndex++]
}

function print(msg) {
    console.log(msg)
}

// solving start
function main() {
    const test = +readline()
    for (let t = 0; t < test; t++) {
        let l = readline().trim().split(' ').map(Number)
        if (l[0] + l[1] == l[2]) {
            print('+')
        } else {
            print('-')
        }
    }
}
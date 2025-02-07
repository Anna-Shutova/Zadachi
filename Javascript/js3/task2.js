const prompt = require('prompt-sync')();

let N = parseInt(prompt('Введите число N: ')); 
let result = [];

for (let i = 1; i <= N ; i += 1) {
    if (i % 2 !== 0)
        result.push(i);
}
result.reverse();

console.log(result.join(' '));


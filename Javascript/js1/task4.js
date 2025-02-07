const prompt = require('prompt-sync')();

let x = prompt("ввeдите число:");

if (x>=0 && x<=9) {
    console.log(`да, это действительно ${x}`);
} else {
    console.log(`нет, это не ${x}`);
}
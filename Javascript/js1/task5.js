const prompt = require('prompt-sync')();

let x = prompt("ввeдите число:");

if (x >= 0 && x <= 10 && (x % 2 == 0)) {
    console.log('истина');
} else {
    console.log('ложь');
}
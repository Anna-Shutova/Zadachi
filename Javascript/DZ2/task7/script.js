document.getElementById('button').addEventListener('click', function(){
    const num = document.getElementById('numInput').value;
    const result = document.getElementById('result');

    if (num >= 200 && num <= 300) {
        result.textContent = `Ваша сумма покупки со скидкой 3%: ${num - (num * 0.03) }`;
    }else if (num >= 300 && num <= 500) {
        result.textContent = `Ваша сумма покупки со скидкой 5%: ${num - (num * 0.05)}`;
    }else if (num >= 500) {
        result.textContent = `Ваша сумма покупки со скидкой 7%: ${num - (num * 0.07)}`;
    } else {
        alert('Введите корректную сумму!');
    }

});

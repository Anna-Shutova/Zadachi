document.getElementById('calculateButton').addEventListener('click', function() {
    const distance = parseFloat(document.getElementById('distance').value);
    const time = parseFloat(document.getElementById('time').value);

    if (sid) {
        message.textContent = `Периметр квадрата ${sid * 4}`;
    } else {
        message.textContent = 'Пожалуйста, введите значение';
    }
});
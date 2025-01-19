document.getElementById('Button').addEventListener('click', function() {
    const radius = document.getElementById('nameInput').value;
    const message = document.getElementById('message');

    if (radius) {
        message.textContent = `Площадь окружности: ${2 * Math.PI * radius} кв.см.`;
    } else {
        message.textContent = 'Пожалуйста, введите значение';
    }
});
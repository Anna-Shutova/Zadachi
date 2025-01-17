document.getElementById('calculateButton').addEventListener('click', function() {
    const flashcard_GB = parseFloat(document.getElementById('GB').value);

    if (!isNaN(flashcard_GB) && flashcard_GB > 0) {
        const files = flashcard_GB * 1024 / 820;
        document.getElementById('result').innerText = `Количество файлов ${files.toFixed(2)}`;
    } else {
        document,this.getElementById('result').innerText = 'Пожалуйста, введите нормально..';
    }
});
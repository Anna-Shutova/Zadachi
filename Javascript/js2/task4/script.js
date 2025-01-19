document.addEventListener('DOMContentLoaded', function() {

    const num = prompt("Введите число х:")
    const numTwo = prompt("Введите число у: ");
    
    
        if (Number(num) == Number(numTwo)){
            alert('Числа равны');
        }else if (Number(num) >= Number(numTwo)){
            alert(`Число ${num} больше числа ${numTwo}`);
        }else{
            alert(`Число ${num} меньше числа ${numTwo}`);
    
        }
    
    });
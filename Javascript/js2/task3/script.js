document.addEventListener('DOMContentLoaded', function() {
    let chislo = prompt("Введите число ");


    if (chislo >= 0 && chislo <= 100){
        alert('принадлежит');
    
    } else {
        alert('не принадлежит');
    }

});
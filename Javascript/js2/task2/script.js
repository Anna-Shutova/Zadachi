document.addEventListener('DOMContentLoaded', function() {
    let password = prompt("Введите пароль ");
    const vallitPassword = ["Step" , "Web" , "Javascript"];

    if (vallitPassword.includes(password)){
        alert('подтверджено');
    } else {
        alert('отменено');
    }

});

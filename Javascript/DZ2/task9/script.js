document.getElementById('button').addEventListener('click', function() {
    const vopros1 = document.getElementById('voprosInput').value;
    const vopros2 = document.getElementById('vopros2Input').value;
    const vopros3 = document.getElementById('vopros3Input').value;
    let score = 0;
    const mes = document.getElementById('mes');

        if (vopros1 == 'Близнецы') {
            score += 2
            mes.textContent = `Правильный ответ 2`  
        }

    
        if (vopros2 == 'Да') {
            score += 2
            mes.textContent = `Правильный ответ 1`  
        }
           
        if (vopros3 == 'Нет') {
            score += 2
            mes.textContent = `Правильный ответ 2`  
            }
       
        
mes.textContent = score
        
    });
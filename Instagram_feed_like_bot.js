/*Rode esta versão no console para curtir #topicos específicos onde precisa clicar no botão Avançar 
e Curtir o próximo. Para curtir os posts no feed, remova a linha 5 e linha 9.*/

let likes = 0;
setInterval(() => {
    const heart = document.querySelector('svg[aria-label="Curtir"][width="24"]'); 
    const arrow = document.querySelector('svg[aria-label="Avançar"]');
    if (heart) {
        heart.parentNode.parentElement.click()
        likes++;
        console.log(`Já curti ${likes} posts automaticamente!`);
    }
    arrow.parentElement.parentElement.click();
}, 19000); */Tempo para curtidas. Lembre-se que o máximo são 400 curtidas por dia!*/

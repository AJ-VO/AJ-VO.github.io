fetch("https://aj-vo.github.io/jsons/players.json")

.then(function(response){
    return response.json();
})

.then(function(products){
    let playerQueryString = decodeURIComponent(window.location.search);
    playerQueryString = playerQueryString.substring(2);
    playerQueryString = parseInt(playerQueryString)//change to integer
    let out = "";
    let winrate = 0;
    for(let product of products){
        if (playerQueryString == product.id){
            winrate = product.wins/(product.wins+product.losses)*100
            winrate = Math.round(winrate * 10) / 10
            out += `
            <img src="${product.img}" alt="Profile" style="width:100%"><h1>${product.name}</h1><p class="title">${product.elo}</p><p>${product.wins} Victoires - ${product.losses} Defaites (${winrate}%)</p><p>Sequence : ${product.streak}</p><br>
            `;
        }
    }
    document.getElementById("playerTab").innerHTML = out

})
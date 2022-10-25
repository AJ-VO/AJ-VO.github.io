fetch("https://aj-vo.github.io/jsons/players.json")

.then(function(response){
    return response.json();
})

.then(function(products){
    let placeholder = document.querySelector("#data-output");
    let out = "";
    var position = 1;
    for(let product of products){
        out+= `
            <tr>
                <td>${position}</td>
                <td><a href="player.html?=${product.id}">${product.name}</a></td>
                <td>${product.elo}</td>
                <td>${product.wins}</td>
                <td>${product.losses}</td>
            </tr>
        `;
        position = position + 1
    }

    placeholder.innerHTML = out;

})

fetch("https://aj-vo.github.io/jsons/results.json")

.then(function(response){
    return response.json();
})

.then(function(products){
    let placeholder = document.querySelector("#data-output1");
    let out = "";
    for(let product of products){
        out+= `
            <tr>
                <td>${product.date}<br><b>${product.winner}</b> + ${product.winnerGain} d. <b>${product.loser}</b> - ${product.winnerGain} <br>[${product.score}]</td>
            </tr>
        `;
    }

    placeholder.innerHTML = out;

})
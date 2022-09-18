fetch("http://127.0.0.1:8000/jsons/players.json")

.then(function(response){
    return response.json();
})

.then(function(products){
    let placeholder = document.querySelector("#data-output");
    let out = "";
    for(let product of products){
        out+= `
            <tr>
                <td>${product.name}</td>
                <td>${product.elo}</td>
                <td>${product.wins}</td>
                <td>${product.losses}</td>
            </tr>
        `;
    }

    placeholder.innerHTML = out;

})

fetch("http://127.0.0.1:8000/jsons/results.json")

.then(function(response){
    return response.json();
})

.then(function(products){
    let placeholder = document.querySelector("#data-output1");
    let out = "";
    for(let product of products){
        out+= `
            <tr>
                <td>${product.date}<br><b>${product.winner}</b> (${product.winnerELO}) + ${product.winnerGain} d. <b>${product.loser}</b> (${product.loserELO}) - ${product.winnerGain} [${product.score}]</td>
            </tr>
        `;
    }

    placeholder.innerHTML = out;

})
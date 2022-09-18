fetch("https://aj-vo.github.io/jsons/players.json")

.then(function(response){
    return response.json();
})

.then(function(products){
    let playerQueryString = decodeURIComponent(window.location.search);
    playerQueryString = playerQueryString.substring(2);
    playerQueryString = parseInt(playerQueryString)
    let placeholder = document.querySelector("#data-output");
    let out = "";
    for(let product of products){
        if (playerQueryString == product.id){
            out+= `
            <tr>
                <td><a href="player.html?=${product.id}">${product.name}</a></td>
                <td>${product.elo}</td>
                <td>${product.wins}</td>
                <td>${product.losses}</td>
            </tr>
        `;
        }
        else{
            console.log("Nothing")
        }
    }

    placeholder.innerHTML = out;

})
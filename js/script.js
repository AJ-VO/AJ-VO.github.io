fetch("https://aj-vo.github.io/jsons/players.json")

.then(function(response){
    return response.json();
})

//Standings
.then(function(products){
    let placeholder = document.querySelector("#data-output");
    let out = "";
    var position = 1;
    for(let product of products){
        if (product.wins == 0 && product.losses == 0){
          console.log(product.name)
        }
        else{
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
    }
    placeholder.innerHTML = out;

})

//Top Players
.then(function(products){
    let out = "";
    console.log(products)
    out+=`<table border=1 align="center">
    <thead>
      <tr>
        <th colspan="3">#1</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td colspan="3">#1 Name</td>
      </tr>
      <tr>
        <td colspan="3"></td>
      </tr>
      <tr>
        <td colspan="3"></td>
      </tr>
      <tr>
        <td colspan="3"></td>
      </tr>
      <tr>
        <td>#2</td>
        <td></td>
        <td>#3</td>
      </tr>
      <tr>
        <td></td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td></td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td></td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td></td>
        <td></td>
        <td></td>
      </tr>
    </tbody>
    </table>`;
    document.getElementById("topPlayersOFFLINE").innerHTML = out
})

fetch("https://aj-vo.github.io/jsons/results.json")

.then(function(response){
    return response.json();
})

.then(function(products){
    let matchShowed = 0
    //console.log()
    let placeholder = document.querySelector("#data-output1");
    let out = "";
    for(let product of products){
        if(matchShowed == 5){
            break;
        }
        else{
            out+= `
            <tr>
                <td>${product.date}<br><b>${product.winner}</b> + ${product.winnerGain} d. <b>${product.loser}</b> - ${product.winnerGain} <br>[${product.score}]</td>
            </tr>
        `;
        }
        matchShowed = matchShowed + 1;
    }

    placeholder.innerHTML = out;

})
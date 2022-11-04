fetch("https://aj-vo.github.io/jsons/players.json")

.then(function(response){
    return response.json();
})

//Top Players
.then(function(products){
    let out = "";
    console.log(products[1])
    out+=`<table align="center" id="customers">
    <thead>
      <tr valign="top">
        <th colspan="2" align="center"><h4>Meneur.euse</h4></th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td colspan="2" align="center"><b><font size="6"><a href="player.html?=${products[0]["id"]}">${products[0]["name"]}</a></font></b></td>
      </tr>
      <tr>
        <td colspan="2" align="center"><b>${products[0]["elo"]}</b></td>
      </tr>
      <tr>
        <td colspan="2" align="center">${products[0]["wins"]} victoires - ${products[0]["losses"]} défaites (${Math.round(products[0]["wins"]/(products[0]["wins"]+products[0]["losses"])*100)}%)</td>
      </tr>
      <tr>
        <td align="center"><b>#2</b></td>
        <td align="center"><b>#3</b></td>
      </tr>
      <tr>
        <td width="100px" align="center"><b><font size="5"><a href="player.html?=${products[1]["id"]}">${products[1]["name"]}</a></font></b></td>
        <td width="100px" align="center"><b><font size="5"><a href="player.html?=${products[2]["id"]}">${products[2]["name"]}</a></font></b></td>
      </tr>
      <tr>
        <td align="center"><b>${products[1]["elo"]}</b></td>
        <td align="center"><b>${products[2]["elo"]}</b></td>
      </tr>
      <tr>
        <td align="center">${products[1]["wins"]} victoires - ${products[1]["losses"]} défaites (${Math.round(products[0]["wins"]/(products[0]["wins"]+products[0]["losses"])*100)}%)</td>
        <td align="center">${products[2]["wins"]} victoires - ${products[2]["losses"]} défaites (${Math.round(products[0]["wins"]/(products[0]["wins"]+products[0]["losses"])*100)}%)</td>
      </tr>
    </tbody>
    </table>`;
    document.getElementById("topPlayers").innerHTML = out
})
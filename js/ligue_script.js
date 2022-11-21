///////////////////////////////////////////////////////////////////////////////////////////////
//async functions to request data
///////////////////////////////////////////////////////////////////////////////////////////////
//fetch jsons (string)
async function getData() {
    var file = "https://aj-vo.github.io/jsons/players.json";
    let x = await fetch(file);
    let y = await x.text();

    var file1 = "https://aj-vo.github.io/jsons/results.json";
    let z = await fetch(file1);
    let q = await z.text();
    return [y, q]
}
//send y to functions
getData().then(
    //returns value
    function(value) {
        myDisplayer(value);
    },
    //returns error
    function(error) {
        catchingFetchError(error);
    }
);
/////////////////////////////////////////////////////////////////////////////////////////////////

//on page load
function pageInitializing() {
    console.log("Page Successfully Initialized");   
    console.log("Provided by jaZZ");
}
//log fecth error
function catchingFetchError(data){
    console.log("failed to fetch json")
    console.log(data)
}

function myDisplayer(data){
    //parse to json
    const playerData = JSON.parse(data[0]),
        resultsData  = JSON.parse(data[1]);
    //top_layer, left_layer, right_layer
    //fix math.round()

    //top_layer
    meneur_winrate = playerData[0]["wins"]/(playerData[0]["wins"]+playerData[0]["losses"])*100;
    document.getElementById("top_layer").innerHTML = 
    `
    <h1>Meneur</h1>
    <h2>`+playerData[0]["name"]+`</h2>
    <img src="https://aj-vo.github.io/img/players/test.png">
    <p style="font-size: 26px;">`+playerData[0]["elo"]+` PTS `+playerData[0]["wins"]+`W-`+playerData[0]["losses"]+`L (`+meneur_winrate+`%)</p>
    `
    ;

    //right_layer (resultats)
    var result_string = "";
    for (let j=0;j<5;j++){
        result_string = result_string + 
        `
        <tr>
        <td><u>`+resultsData[j]["date"]+`</u>
        <br>`+(resultsData[j]["winner"])+` d. `+(resultsData[j]["loser"])+` 
        <br><b>[`+(resultsData[j]["score"])+`]</b><br><br></td>
        </tr>
        `;
    }
    document.getElementById("right_layer").innerHTML = 
    `
    <h1>Derniers Résultats</h1>
    <table>
    <tbody>
    <tr>
    `+result_string+`
    </tr>
    </tbody>
    </table>
    `
    ;

    //left_layer (classement)
    var standing_string = "";
    var place = 0;
    for (let i=0; i<playerData.length;i++){
        if (playerData[i]["gp"] == 0){
            continue;
        }
        place = place+1;
        standing_string = standing_string + 
        `
        <tr>
        <td align="center">&nbsp;`+(place)+`&nbsp;</td>
        <td><a href="" style="color:rgb(223, 223, 68); font-size: 14px;">`+(playerData[i]["name"])+`</a></td>
        <td>&nbsp;`+(playerData[i]["elo"])+`&nbsp;</td>
        <td align="center">`+(playerData[i]["wins"])+`</td>
        <td align="center">`+(playerData[i]["losses"])+`</td>
        </tr>
        `;
    }
    document.getElementById("left_layer").innerHTML = 
    `
    <h1>Classement</h1>
    <table border="1" class="standings">
    <thead>
    <tr>
        <th>#</th>
        <th>Nom</th>
        <th>Pts</th>
        <th>&nbsp;Victoires&nbsp;</th>
        <th>&nbsp;Défaites&nbsp;</th>
    </tr>
    </thead>
    <tbody>
    `+standing_string+`
    </tbody>
    </table>
    `
    ;
}
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

//players.json and results.json displayer for index.html
function myDisplayer(data){
    //parse to json
    const playerData = JSON.parse(data[0]),
        resultsData  = JSON.parse(data[1]);
    //meneur
    var meneurString = "";
    meneurString = meneurString + "&nbsp;"+playerData[0]["name"]+"&nbsp;";
    document.getElementById("meneur_name").innerHTML = meneurString;
    meneurString = "";
    meneurString = meneurString + playerData[0]["elo"] + " ("+playerData[0]["wins"]+"W-"+playerData[0]["losses"]+"L)";
    document.getElementById("meneur_elo").innerHTML = meneurString;
    //get last match of meneur
    for (let i=0; i<resultsData.length;i++){
        if (resultsData[i]["winner"] == playerData[0]["name"] || resultsData[i]["loser"] == playerData[0]["name"]){
            document.getElementById("meneur_text").innerHTML = "Dernier Match:<br><b>"+resultsData[i]["winner"]+"</b> d. <b>"+resultsData[i]["loser"]+"</b>";
            break;
        }
    }
    //random
    const randomPlayer = Math.floor(Math.random() * Object.keys(playerData).length);
    var randomString = "";
    randomString = randomString + "&nbsp;"+playerData[randomPlayer]["name"]+"&nbsp;";
    document.getElementById("random_name").innerHTML = randomString;
    randomString = "";
    randomString = randomString + playerData[randomPlayer]["elo"] + " ("+playerData[randomPlayer]["wins"]+"W-"+playerData[randomPlayer]["losses"]+"L)";
    document.getElementById("random_elo").innerHTML = randomString;
    //get ranking of random player
    for (let j=0; j<playerData.length;j++){
        if (playerData[j]["name"] == playerData[randomPlayer]["name"] || playerData[j]["name"] == playerData[randomPlayer]["name"]){
            var standing = j+1
            document.getElementById("random_text").innerHTML = "Classement: #"+(standing);
            break;
        }
    }

}
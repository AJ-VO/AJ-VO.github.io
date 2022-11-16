///////////////////////////////////////////////////////////////////////////////////////////////
//async functions to request data
///////////////////////////////////////////////////////////////////////////////////////////////
//fetch players json (string)
async function getData() {
    var file = "https://aj-vo.github.io/jsons/players.json";
    let x = await fetch(file);
    let y = await x.text();
    return y
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

//players.json displayer
function myDisplayer(data){
    //parse to json
    const playerData = JSON.parse(data);
    //meneur
    var meneurString = "";
    meneurString = meneurString + "<p>"+playerData[0]["name"]+"</p>";
    document.getElementById("player_meneur").innerHTML = meneurString;
    //random
    const randomPlayer = Math.floor(Math.random() * Object.keys(playerData).length);
    var randomString = "";
    randomString = randomString + "<p>"+playerData[randomPlayer]["name"]+"</p>";
    document.getElementById("player_random").innerHTML = randomString;

}
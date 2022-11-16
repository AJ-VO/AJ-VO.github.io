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
    document.getElementById("top_layer").innerHTML = "top_layer";
    document.getElementById("left_layer").innerHTML = "left_layer";
    document.getElementById("right_layer").innerHTML = "right_layer";
}
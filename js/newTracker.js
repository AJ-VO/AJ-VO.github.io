//functions

//Changes the layout of the buttons on screen
function button_layout(scene){
    document.getElementById("button_layer").innerHTML = buttonDict[scene];
}

function start_match(){
    //start
}

//script start
console.log("tracker.js staring...")

//get players from urls
var matchup = decodeURIComponent(window.location.search);
matchup = matchup.substring(2);
const players = matchup.split("-");

//load starting serve buttons
button_layout(0);

//all variables
var trackerBackup;//store tracker for "undo"

//initialize const
const tracker = 0;
const pointDict = {
    0: "0",
    1: "15",
    2: "30",
    3: "40",
};
const buttonDict = {
    0: "",
    1: "",
    2: "",
    3: "",
    4: ""
};
//library

//main functions
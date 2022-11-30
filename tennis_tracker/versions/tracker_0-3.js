//v0.3

//Request a match tracker
async function get_tracker() {
    document.getElementById("status_layer").innerHTML = "Requesting Tracker...";
    var file = "https://aj-vo.github.io/tennis_tracker/emptyTracker.json";
    let x = await fetch(file);
    let y = await x.text();
    return y;
}//send y to functions
get_tracker().then(
    //returns value
    function(value) {
        value = JSON.parse(value);
        myTracker = value["match"];
        for (let i=0;i<2;i++){
            myTracker["data"][i]["player_name"] = players[i];
        }
        console.log("got tracker successfully...");
        document.getElementById("status_layer").innerHTML = "Status: Ready";
    },
    //returns error
    function(error) {
        console.log(error);
    }
);

//Functions
function backup_data(){

}

//Variables
var myTracker;
//get players from urls
var matchup = decodeURIComponent(window.location.search);
matchup = matchup.substring(2);
matchup = matchup.split("-");
//attribute values
const players = [matchup[0], matchup[1]];
var playerOnServe = matchup[2];
//basic dictionnaries
const opp = {
    0: 1,
    1: 0
};
const pointDict = {
    0: "0",
    1: "15",
    2: "30",
    3: "40",
};
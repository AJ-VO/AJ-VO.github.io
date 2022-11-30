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
            myTracker["data"][i]["player_name"] = PLAYERS[i];
        }
        //backup initial data
        myTracker["backup_information"]["players"] = PLAYERS;
        
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
function update_stats(){

}
function update_score(){

}
function check_game_state(){

}
function button_layout(){

}
function event_manager(nextLayout, event, winner, serve){

    

    update_stats();
    update_score();
    backup_data();
    button_layout();
    check_game_state();

}


//Variables
var myTracker;
//get PLAYERS from urls
var MATCHUP = decodeURIComponent(window.location.search);
MATCHUP = MATCHUP.substring(2);
MATCHUP = MATCHUP.split("-");
//attribute values
const PLAYERS = [MATCHUP[0], MATCHUP[1]];
var playerOnServe = MATCHUP[2];
//basic dictionnaries
const OPP = {
    0: 1,
    1: 0
};
const pointDict = {
    0: "0",
    1: "15",
    2: "30",
    3: "40",
};
//start match
event_manager(0,null,null,null);
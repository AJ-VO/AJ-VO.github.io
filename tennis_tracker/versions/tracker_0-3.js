//v0.3
//reset values to past event
//restart with series of event?

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
function opp_id(id){
    return 1-id;
}
function show_serve_status_ui(id){
    if (id == playerOnServe){
        return "*";
    }
    else{
        return "";
    }
}
function backup_data(event){
    if (event == "start"){
        return;
    }
    else {
        //need to string vars?
        myTracker["backup_information"]["stats"] = JSON.stringify(myTracker);
        myTracker["backup_information"]["playerOnServe"] = playerOnServe;
        myTracker["backup_information"]["scores"] = SCORES;
        myTracker["backup_information"]["currentPoints"] = String(currentPoints);
        myTracker["backup_information"]["players"] = PLAYERS;
        myTracker["backup_information"]["currentServe"] = currentServe;
        myTracker["backup_information"]["momentum"] = MOMENTUM;
        myTracker["backup_information"]["tiebreakStatus"] = tiebreakStatus;
        myTracker["backup_information"]["breakpointStatus"] = breakpointStatus;
        myTracker["backup_information"]["matchTime"] = matchTime;
        myTracker["backup_information"]["deuceStatus"] = deuceStatus;
    }
}
function update_stats(){

}
function update_score(winner){

    currentPoints[winner] += 1;
    //atrribute game win if needed
    if (currentPoints[winner] == 4){
        check_game_state(winner);
    }
    //check tiebreakStatus
    //check breakpointStatus
    //check deuceStatus
    if (currentPoints[winner] == 3 && currentPoints[winner] == currentPoints[opp_id(winner)]){
        //deuce
    }
}
function check_game_state(winner){
    //add game win
    //check
}
function button_layout(layout){
    document.getElementById("button_layer").innerHTML = "Button: "+layout;
}
function event_manager(nextLayout, event, winner, serve){

    //whatever event, backup any data that could be edited
    backup_data(event); 

    //if event
    if (winner == null && serve == null){
        //
    }
    else{
        update_stats();
        update_score(winner);
    }

    //change layout
    button_layout(nextLayout);
    //update match time
    matchTime = Date.now()-startTime;
}


//Variables
var myTracker;
//get players from urls/
var MATCHUP = decodeURIComponent(window.location.search);
MATCHUP = MATCHUP.substring(2);
MATCHUP = MATCHUP.split("-");
//attribute values
const PLAYERS = [MATCHUP[0], MATCHUP[1]];
var playerOnServe = MATCHUP[2];
//variables
var currentServe = 1;//Current Serve (1,2)
var currentSet = 0;//Current Set (0,1,2)
const startTime = Date.now();//Current time (ms)
var tiebreakStatus = false;//Are we in a tiebreak
var breakpointStatus = false;//Is next point a chance of break
var deuceStatus = false;//Is next point a deuce
var matchTime;//Total match time
var currentPoints = [0,0]//points in game
var SCORES = [[0,0],[0,0],[0,0]];//all the sets
var MOMENTUM
//basic dictionnaries
const pointDict = {
    0: "0",
    1: "15",
    2: "30",
    3: "40",
};
//start match
event_manager(0,"start",null,null);
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
function backup_data(){
    myTracker["backup_information"]["stats"] = JSON.stringify(myTracker);
    myTracker["backup_information"]["playerOnServe"] = playerOnServe;
    //scores
    myTracker["backup_information"]["players"] = PLAYERS;
    myTracker["backup_information"]["currentServe"] = currentServe;
    //momentum
    //tiebreakStatus
    //breakpointStatus
    //matchTime
}
function update_stats(){

}
function update_score(winner){

}
function check_game_state(){

}
function button_layout(layout){

}
function event_manager(nextLayout, event, winner, serve){

    //whatever event, backup any data that could be edited
    backup_data();

    //if event
    if (winner == null && serve == null){
        //
    }
    else{
        update_stats();
        update_score(winner);
        check_game_state();
    }

    //change layout
    button_layout(nextLayout);
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
var start_time = Date.now();//Current time (ms)
//basic dictionnaries
const pointDict = {
    0: "0",
    1: "15",
    2: "30",
    3: "40",
};
//start match
event_manager(0,"start",null,null);
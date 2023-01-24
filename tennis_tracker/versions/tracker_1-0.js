//decode the information that was sent from html file
var MATCHUP = decodeURIComponent(window.location.search);
MATCHUP = MATCHUP.substring(2);
MATCHUP = MATCHUP.split("-");
//attribute values
const PLAYERS = [MATCHUP[0], MATCHUP[1]];
var playerOnServe = MATCHUP[2];

//requesting files
//Request a match tracker
async function get_tracker() {
    document.getElementById("status_layer").innerHTML = "Requesting Tracker...";
    var file = "https://aj-vo.github.io/tennis_tracker/versions/tracker.json";
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

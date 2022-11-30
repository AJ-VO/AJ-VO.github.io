//v0.3

//Request a match tracker
async function get_tracker() {
    document.getElementById("status_layer").innerHTML = "Requesting Tracker...";
    var file = "https://aj-vo.github.io/jsons/trackers/trackerEmpty.json";
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


//Variables
var myTracker;
const players = [];
//v0.2
//undo, color, break point conversion%

///////////////////////////////////////////////////////////////////////////////////////////////////////////////
///////////////////////////////////////////////////////////////////////////////////////////////////////////////
//Async Functions
//fetch jsons
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
        assign_tracker(value);
    },
    //returns error
    function(error) {
        catching_fetch_error(error);
    }
);
//log fetch error
function catching_fetch_error(error){
    console.log(error);
}
//assign tracker data to variable
function assign_tracker(value){
    value = JSON.parse(value);
    tracker = value["match"];
    //set names?
    for (let i=0;i<2;i++){
        tracker["data"][i]["player_name"] = players[i];
    }
    console.log("got tracker successfully...");
    document.getElementById("status_layer").innerHTML = "Status: Ready";
}
///////////////////////////////////////////////////////////////////////////////////////////////////////////////


//BREAK


///////////////////////////////////////////////////////////////////////////////////////////////////////////////
///////////////////////////////////////////////////////////////////////////////////////////////////////////////
//Other Functions
//back key information (WIP)
function backup_data(){
    //data
    try {
        console.log("backup");
        trackerBackup = JSON.stringify(tracker);
    } catch (error) {
        console.log("couldnt backup");
    }
    //score (WIP)
    try {
        console.log("score backup");
        scoreBackup["currentPoints"] = JSON.stringify(currentPoints);
        scoreBackup["theSets"] = JSON.stringify(theSets);
        scoreBackup["currentSet"] = JSON.stringify(gamesWonInSet);
        scoreBackup["tiebreakStatus"] = JSON.stringify(tiebreakStatus);
        //need to store the current keys values of the match
    } catch (error) {
        console.log("score couldnt backup");
    }
}
//undo protocol (WIP)
function undo_event(){
    //trackerBackup, scoreBackup
    //reset score to last score
    //gotta log the score
    //reset tracker to last tracker
    //already store a backup before calling function

    //we changed the objets to string, will have to parse them back
    //can call update_live_score and update_live_stats
    //but will enter return; (FIX)

    //tracker try?
    console.log("undo");
    tracker = JSON.parse(trackerBackup);
    update_live_stats(null,-1,null);

    //score try?
    

}
//check which player is serving (ui) returns string
function check_serve_status(myBox){
    if (myBox == playerOnServe){
        return "*";
    }
    else{
        return "";
    }
}
//returns sum of a list
function sum_list(myList){
    var sum = myList.reduce(function(a, b){
        return a + b;
    }, 0);
    return sum;
}
//change score on display
//checks if the game is over
function update_live_score(winner){
    if (winner == null){
        //no score to update
        return;
    }
    else{
        //reset serve after point
        currentServe = 1;
        //add point
        currentPoints[winner] += 1;
        //are we in a tiebreak?
        if (tiebreakStatus == true){
            //we in a tiebreak (show true score)
            //reset at 7
            //change serve?
            if (sum_list(currentPoints)%2 == 1){
                playerOnServe = opp[playerOnServe];//1
            }
            if (currentPoints[winner] >= 7 && (currentPoints[winner]-currentPoints[opp[winner]]) > 1){
                //game is over
                playerOnServe = opp[playServeTiebreak];//2
                gameIsOver = true;
            }
        }
        else{
            //we in a game (show tennis score)
            //reset at 4
            if (currentPoints[winner] == 4){
                //game is over
                playerOnServe = opp[playerOnServe];//3
                gameIsOver = true;
            }
        }
        checklist(winner);
    }

    //update ui
    //tiebreak or not?
    if (tiebreakStatus == true){
        pointStrings = [currentPoints[0], currentPoints[1]];
    }
    else{
        pointStrings = [pointDict[currentPoints[0]], pointDict[currentPoints[1]]];
    }

    document.getElementById("score_layer").innerHTML = 
    `
    <table border=1>
        <tbody>
            <tr>
                <td>`+check_serve_status(0)+`</td>
                <td>`+players[0]+`</td>
                <td>`+pointStrings[0]+`</td>
                <td>`+gamesWonInSet[0]+`</td>
                <td>`+theSets[0][0]+`</td>
                <td>`+theSets[1][0]+`</td>
                <td>`+theSets[2][0]+`</td>
            </tr>
            <tr>
                <td>`+check_serve_status(1)+`</td>
                <td>`+players[1]+`</td>
                <td>`+pointStrings[1]+`</td>
                <td>`+gamesWonInSet[1]+`</td>
                <td>`+theSets[0][1]+`</td>
                <td>`+theSets[1][1]+`</td>
                <td>`+theSets[2][1]+`</td>
            </tr>
        </tbody>
    </table>
    `
    ;

}
//changes stats on display
function update_live_stats(event, serve, winner){
    if (winner == null || event == "fault" || event == "ip"){
        //no stats to update
        eventsAmount += 1;
    }
    else{
        //a winner, so stats needs to change
        //break points?
        if (currentPoints[opp[playerOnServe]] == 3){
            //deuce counts as a break point!!
            tracker["data"][opp[playerOnServe]]["conversion"]["break_points"] += 1;
        }
        //momentum
        momentum.push(winner);
        tracker["momentumArray"] = momentum;
        //time
        var current_time = Date.now();
        var match_time = Math.round((current_time-start_time)/1000/60);
        tracker["match_time"] = current_time-start_time;
        document.getElementById("time_layer").innerHTML = "Durée: "+match_time+"m ";
        //for every point played
        //add to total points
        tracker["total_points"] += 1;
        //add to total services
        tracker["data"][playerOnServe]["service"]["total_services"] += 1;
        //1,2
        tracker["data"][playerOnServe]["service"][serve.toString()] += 1;
        //calculate service rates
        total = tracker["data"][playerOnServe]["service"]["total_services"];
        tracker["data"][playerOnServe]["service"]["1_serve_p"] = tracker["data"][playerOnServe]["service"]["1"]/total;
        tracker["data"][playerOnServe]["service"]["2_serve_p"] = (tracker["data"][playerOnServe]["service"]["2"]-tracker["data"][playerOnServe]["service"]["df"])/tracker["data"][playerOnServe]["service"]["2"];
        //%point won on specific serve?

        //total points won
        tracker["data"][winner]["points"]["total_points_won"] += 1;
        //receive points won
        if (winner == opp[playerOnServe]){
            tracker["data"][winner]["conversion"]["receiving_points_won"] += 1;
        }
        //on serve
        if (winner == playerOnServe){
            tracker["data"][winner]["conversion"][serve+"_service_points_won"] += 1;
        }
        //conversion
        //calculate rate conversion
        for (let i=1;i<3;i++){
            var win = 0;
            win = tracker["data"][playerOnServe]["conversion"][i+"_service_points_won"]/tracker["data"][playerOnServe]["service"][String(i)];
            tracker["data"][playerOnServe]["service"][i+"_win"] = win;
        }
        //break point

        switch (event) {
            //specific stats
            case "ace":
                //winner
                //ace
                tracker["data"][playerOnServe]["service"]["ace"] += 1;
                tracker["data"][playerOnServe]["points"]["w"] += 1;
                break;
            case "df":
                tracker["data"][playerOnServe]["service"]["df"] += 1;
                tracker["data"][playerOnServe]["points"]["ue"] += 1;
                break;
            case "re":
                tracker["data"][opp[playerOnServe]]["return"]["re"] += 1;
                tracker["data"][opp[playerOnServe]]["return"]["unreturned_"+serve] += 1;
                if (serve == 1){
                    tracker["data"][playerOnServe]["points"]["fe"] += 1;
                }
                else{
                    //serve == 2
                    tracker["data"][opp[playerOnServe]]["points"]["ue"] += 1;
                }
                break;
            case "rw":
                tracker["data"][opp[playerOnServe]]["points"]["w"] += 1;
                tracker["data"][opp[playerOnServe]]["return"]["rw"] += 1;
                break;
            case "w":
                tracker["data"][winner]["points"]["w"] += 1;
                break;
            case "ue":
                tracker["data"][opp[winner]]["points"]["ue"] += 1;
                break;
            case "fe":
                tracker["data"][winner]["points"]["fe"] += 1;
                break;
            default:
                console.log("error, switch(event)[update_live_stats]");
        }
        //after specific event stats
        tracker["data"][playerOnServe]["service"]["2_serve_p"] = (tracker["data"][playerOnServe]["service"]["2"]-tracker["data"][playerOnServe]["service"]["df"])/tracker["data"][playerOnServe]["service"]["2"];
        //aggresive margin
        for (let i=0;i<2;i++){
            tracker["data"][i]["points"]["aggresive_margin"] = tracker["data"][i]["points"]["w"]+tracker["data"][i]["points"]["fe"]-tracker["data"][i]["points"]["ue"];
        }
    }
    //update ui
    //parse json
    fakeTracker = JSON.stringify(tracker)
    document.getElementById("stat_layer").innerHTML = fakeTracker;
    //backup button
    //onclick=undo_event()
    document.getElementById("undo_layer").innerHTML = `<button>Précédent/Annulé Dernier Point</button>`;
}
//checklist for breaks in the match
//only if score changes
function checklist(winner){
    if (gameIsOver == true){
        gameIsOver = false;
        gamesWonInSet[winner] += 1;
        currentPoints = [0,0];
        //check gamesWonInSet
        if (sum_list(gamesWonInSet) == 12 && gamesWonInSet[winner] == gamesWonInSet[opp[winner]]){
            //tiebreak
            console.log("entering tiebreak...");
            //get serve
            playServeTiebreak = playerOnServe;
            tiebreakStatus = true;
        }
        else if ((gamesWonInSet[winner] == 7 && gamesWonInSet[opp[winner]] == 6) || (gamesWonInSet[winner] >= 6 && (gamesWonInSet[winner]-gamesWonInSet[opp[winner]] > 1))){
            //done
            console.log("set done...");
            //add to set score
            theSets[currentSet] = (gamesWonInSet);
            currentSet += 1;
            gamesWonInSet = [0,0];
            setValues[winner] += 1;
            tiebreakStatus = false;
            //is match over?
            if (setValues[winner] == 2){
                //match is over
                console.log("match is done...");
                document.getElementById("button_layer").innerHTML = "<p>THAT'S ALL FOLKS!</p>";
                matchIsOver = true;
                //END
            }
        }
        else{
            //not done
            return;
        }
    }
    else{
        return;
    }
}
///////////////////////////////////////////////////////////////////////////////////////////////////////////////


//BREAK


///////////////////////////////////////////////////////////////////////////////////////////////////////////////
///////////////////////////////////////////////////////////////////////////////////////////////////////////////
//Main Functions
//evaluates the parameters of the event
function event_manager(nextLayout, event, winner, serve, pointStatus){

    if (matchIsOver == true){
        //nahhhh
        return;
    }

    //parse parameters
    //start : (0, "start", null, null, true)
    //i only change currentServe if need to be
    switch (event){
        case "start":
            console.log("match is starting...");
            break;
        case "fault":
            currentServe += 1;
            break;
        default:
            console.log(event);
    }
    //backup_data();
    update_live_stats(event, serve, winner);
    update_live_score(winner);
    button_layout(nextLayout);
    //check if something is wrong in stats?

}
//changes the layout of the buttons on screen
function button_layout(scene){
    //switch statement
    if (matchIsOver == true){
        //nahhhh
        return;
    }
    var buttonString = "";
    var buttonDict = {
        0: '<button onclick=event_manager(1,"fault",null,1,false)>Faute</button>',
        1: '<button onclick=event_manager(0,"df",'+opp[playerOnServe]+',2,true)>Double Faute</button>'
    };
    switch (scene){
        case 0:
        case 1:
            //send currentServe
            buttonString =
            `
            <table border=1>
                <tbody>
                    <tr>
                        <td><button onclick=event_manager(0,"ace",`+[playerOnServe]+`,`+currentServe+`,true)>Ace</button></td>
                        <td>`+buttonDict[scene]+`</td>
                    </tr>
                    <tr>
                        <td><button onclick=event_manager(0,"re",`+[playerOnServe]+`,`+currentServe+`,true)>Retour Erreur</button></td>
                        <td><button onclick=event_manager(0,"rw",`+opp[playerOnServe]+`,`+currentServe+`,true)>Retour Gagnant</button></td>
                    </tr>
                    <tr>
                        <td colspan="2"><button onclick=event_manager(2,"ip",null,`+currentServe+`,false)>En Jeu</button></td>
                    </tr>
                </tbody>
            </table>
            `;
            document.getElementById("button_layer").innerHTML = buttonString;
            break;
        case 2:
            //show name
            buttonString =
            `
            <table border=1>
                <tbody>
                    <tr>
                        <td align="center">`+players[0]+`</td>
                        <td align="center">`+players[1]+`</td>
                    </tr>
                    <tr>
                        <td><button onclick=event_manager(0,"w",0,`+currentServe+`,true)>Coup Gagnant</button></td>
                        <td><button onclick=event_manager(0,"w",1,`+currentServe+`,true)>Coup Gagnant</button></td>
                    </tr>
                    <tr>
                        <td><button onclick=event_manager(0,"ue",1,`+currentServe+`,true)>Erreur Non-Forcée</button></td>
                        <td><button onclick=event_manager(0,"ue",0,`+currentServe+`,true)>Erreur Non-Forcée</button></td>
                    </tr>
                    <tr>
                        <td><button onclick=event_manager(0,"fe",0,`+currentServe+`,true)>Force l'Erreur</button></td>
                        <td><button onclick=event_manager(0,"fe",1,`+currentServe+`,true)>Force l'Erreur</button></td>
                    </tr>
                </tbody>
            </table>
            `;
            document.getElementById("button_layer").innerHTML = buttonString;
            break;
        case 3:
            console.log("match is done");
            break;
        default:
            console.log("scene does not match any layout");
    }
}
///////////////////////////////////////////////////////////////////////////////////////////////////////////////


//BREAK


///////////////////////////////////////////////////////////////////////////////////////////////////////////////
///////////////////////////////////////////////////////////////////////////////////////////////////////////////
//Script Start
console.log("tracker.js staring...");
//get players from urls
var matchup = decodeURIComponent(window.location.search);
matchup = matchup.substring(2);
matchup = matchup.split("-");
//attribute values
const players = [matchup[0], matchup[1]];
var playerOnServe = matchup[2];
console.log(players[playerOnServe]+" starting on serve...");

//initialize all variables
var trackerBackup, setWon, currentPoints, tracker, tiebreakStatus, gameIsOver, currentServe, gamesWonInSet, theSets, currentSet, setValues,
pointStrings, momentum, matchIsOver, scoreBackup, eventsAmount;
eventsAmount = 0;
currentServe = 1;
currentSet = 0;
tiebreakStatus = false;
gameIsOver = false;
matchIsOver = false;
setWon = [0,0];
currentPoints = [0,0];
gamesWonInSet = [0,0];
theSets = [[0,0],[0,0],[0,0]];
setValues = [0,0];
momentum = [];
trackerBackup = {};
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
scoreBackup = {
    "currentPoints": 0,
    "currentSet": 0,
    "theSets": 0,
    "tiebreakStatus": false
};
//run script at first
var start_time = Date.now();
console.log("start_time: "+start_time)
document.getElementById("title_layer").innerHTML = players[0]+" vs. "+players[1];
event_manager(0, "start", null, null, true);
///////////////////////////////////////////////////////////////////////////////////////////////////////////////


//BREAK


///////////////////////////////////////////////////////////////////////////////////////////////////////////////
///////////////////////////////////////////////////////////////////////////////////////////////////////////////
//variables dictionnary

//matchup = [] = array of parameters from the url
//players = [] = array of the names of the players
//playerOnServe = 0,1 = id of the current player serving
//tracker = json = current statistics
//trackerBackup = json = statistics from the last point
//setWon = [] = ammount of sets players have won
//currentPoints = [] = points of each player in the current game(0, 1, 2, 3, 4)(0, 15, 30, 40, G)(tiebreak)
//gameIsOver = bool = is the game over status
//opp = json = opposite of the current id
//pointDict = json = show good points(15-30-40)
//buttonDict = json = show faute ou double faute
//buttonString = "" = button layout string
//currentServe = 1,2 = serve of the player
//gamesWonInSet = [] = games of both player during the current set
//playServeTiebreak = 0,1 = player that started serving at the begining of a tiebreak
//theSets = [] = score of all the sets in the match 
//setValues = [] = number of sets each player has won
//pointStrings = [] = show or not the points changed
//momentum = [] = winner of each point
//matchIsOver = bool = is the match over
//scoreBackup = json = score before changing to next score
///////////////////////////////////////////////////////////////////////////////////////////////////////////////

//add state of game json?
//playerOnServe, players, score, stats, currentServe, tiebreakStatus, momentum
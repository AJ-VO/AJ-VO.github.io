//undo, change score, color

///////////////////////////////////////////////////////////////////////////////////////////////////////////////
///////////////////////////////////////////////////////////////////////////////////////////////////////////////
//Async Functions
//fetch jsons (string)
async function get_tracker() {
    var file = "https://aj-vo.github.io/jsons/trackers/trackerEmpty.json";
    let x = await fetch(file);
    let y = await x.text();

    return y;
}
//send y to functions
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
    console.log("get tracker successfull...");
}
///////////////////////////////////////////////////////////////////////////////////////////////////////////////


//BREAK


///////////////////////////////////////////////////////////////////////////////////////////////////////////////
///////////////////////////////////////////////////////////////////////////////////////////////////////////////
//Other Functions
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
    //give winner his point
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
                playerOnServe = opp[playerOnServe];
            }
            if (currentPoints[winner] >= 7 && (currentPoints[winner]-currentPoints[opp[winner]]) > 1){
                //game is over
                playerOnServe = opp[playServeTiebreak];
                gameIsOver = true;
                console.log("tiebreak is done");
            }
        }
        else{
            //we in a game (show tennis score)
            //reset at 4
            if (currentPoints[winner] == 4){
                //game is over
                playerOnServe = opp[playerOnServe];
                console.log("serve change");
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
                <td>`+players[0]+`</td>
                <td>`+pointStrings[0]+`</td>
                <td>`+gamesWonInSet[0]+`</td>
                <td>`+theSets[0][0]+`</td>
                <td>`+theSets[1][0]+`</td>
                <td>`+theSets[2][0]+`</td>
            </tr>
            <tr>
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
        return;
    }
    else{
        //a winner, so stats needs to change
        //backuptracker
        //switch 
    }
    //update ui
}
//checklist for breaks in the match
//only if score changes
function checklist(winner){
    if (gameIsOver == true){
        gameIsOver = false;
        gamesWonInSet[winner] += 1;
        console.log(gamesWonInSet);
        currentPoints = [0,0];
        //check gamesWonInSet
        if (sum_list(gamesWonInSet) == 12 && gamesWonInSet[winner] == gamesWonInSet[opp[winner]]){
            //tiebreak
            console.log("tiebreak");
            //get serve
            playServeTiebreak = playerOnServe;
            tiebreakStatus = true;
        }
        else if ((gamesWonInSet[winner] == 7 && gamesWonInSet[opp[winner]] == 6) || (gamesWonInSet[winner] >= 6 && (gamesWonInSet[winner]-gamesWonInSet[opp[winner]] > 1))){
            //done
            console.log("done");
            //add to set score
            theSets[currentSet] = gamesWonInSet;
            gamesWonInSet = [0,0];
            setValues[winner] += 1;
            console.log(setValues);
            tiebreakStatus = false;
            //is match over?
            if (setValues[winner] == 2){
                //match is over
                button_layout(3);
            }
        }
        else{
            //not done
            console.log("not done");
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

    //parse parameters
    //start : (0, "start", null, null, true)
    switch (event){
        case "start":
            console.log("match is starting...");
            break;
        case "ace":
            console.log(event);
            break;
        case "df":
            console.log(event);
            break;
        case "fault":
            currentServe += 1;
            break;
        case "re":
            console.log(event);
            break;
        case "rw":
            console.log(event);
            break;
        case "w":
            console.log(event);
            break;
        case "ue":
            console.log(event);
            break;
        case "fe":
            console.log(event);
            break;
        default:
            //ip
            console.log(event+" triggers nothing");
    }
    console.log(winner);
    update_live_score(winner);
    update_live_stats(event, serve, winner);
    button_layout(nextLayout);

}
//changes the layout of the buttons on screen
function button_layout(scene){
    //switch statement
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
            buttonString =
            `
            <table border=1>
                <tbody>
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
            console.log("match is done")
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
pointStrings;
currentServe = 1;
currentSet = 0;
tiebreakStatus, gameIsOver = false;
setWon = [0,0];
currentPoints = [0,0];
gamesWonInSet = [0,0];//[0,0]
theSets = [[0,0], [0,0], [0,0]];
setValues = [0,0];
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
//run script at first
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
///////////////////////////////////////////////////////////////////////////////////////////////////////////////
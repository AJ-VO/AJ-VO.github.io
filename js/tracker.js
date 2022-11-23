//bugs:

//Library

function opposite(id){
    if (id == 0){
        return 1
    }
    else {
        return 0
    }
}

function showGoodScore(playerScore){
    return pointDict[playerScore]
}

function matchOver(){
    console.log("match is over...");
    //generate link
    //https://aj-vo.github.io/match?=trackerJSON
    //change layout
    buttonLayout(3);
    document.getElementById("mainTracker").innerHTML = "Final Stats";
}

function theSetIsOver(winner){
    //set is over
    //change set
    currentSet = currentSet+1;
    //add set to winner
    total_sets[winner] = total_sets[winner] + 1;
    //reset game score
    game_score[0] = 0;
    game_score[1] = 0;
    //is the match over?
    if (total_sets[winner] == 2){
        matchOver();
    }
    else{
        console.log("set over... keep playing");
    }

}

function checkIfEndOfGame(winner){
    //check if the last point ended the game (from eventManager)

    //for every player
    for (let i=0;i<2;i++){
        //does the player have more than three points? 40->G
        //is the game over?
        if (score[i] > 3){
            //game has ended
            console.log("end of game");
            //log score win
            //game win
            game_score[winner] = game_score[winner]+1;
            //edit current total_score
            total_score[currentSet][winner] = total_score[currentSet][winner]+1;
            //change serving keys
            serverKey = opposite(serverKey);
            returnKey = opposite(returnKey);
            //reset game score for both players
            for (let j=0;j<2;j++){
                score[j] = 0;
            }

        //game has ended, is the set over?

        //does a winner of the last game have 6 games in the bank?
        if (game_score[winner] == 6){
            
            //does the other player has less than 5 games? over
            if (game_score[opposite(winner)] < 5){
                theSetIsOver(winner);
            }
            
            //6-5
            else if (game_score[opposite(winner)] == 5){
                console.log("set is not over");
            }
            //6-6
            else{
                tiebreakStatus = true;
                theTiebreak[0] = 0;
                theTiebreak[1] = 0;
                console.log("tiebreak");
            }
        }
        //does the winner have 7 games in the bank
        else if (game_score[winner] == 7){
            //over
            theSetIsOver(winner);
        }
        //set is not over
        else {
            console.log("set is not over");
        }

       }
    }
    
}

function logEvent(winner, playerEvent, event, pointStatus, serve){

    console.log("log event");
    //logging protocol
    //keep last event for undo?

    //is the point over?
    if (pointStatus == true){
        //point is over

        //Service
        //1) Add to ["service"]["total_services"]
        trackerJSON["match"]["data"][serverKey]["service"]["total_services"]=trackerJSON["match"]["data"][serverKey]["service"]["total_services"]+1;
        //2)If ace of double fault
        if (event == "ace" || event == "df"){
            trackerJSON["match"]["data"][serverKey]["service"][event]=trackerJSON["match"]["data"][serverKey]["service"][event]+1;
            trackerJSON["match"]["data"][serverKey]["points"][serveEventDict[event]]=trackerJSON["match"]["data"][serverKey]["points"][serveEventDict[event]]+1;
        }
        //3)Enter serve in play
        trackerJSON["match"]["data"][serverKey]["service"][serve]=trackerJSON["match"]["data"][serverKey]["service"][serve]+1;
        //4)Calculate first serve % (1st services / total services[will never be 0])
        var firstServeP = trackerJSON["match"]["data"][serverKey]["service"]["1"]/trackerJSON["match"]["data"][serverKey]["service"]["total_services"];
        trackerJSON["match"]["data"][serverKey]["service"]["first_serve_p"] = firstServeP;


        //Return
        //Add winner, fe, ue
        //5)Does the return end the point?
        if (event == "re" || event == "rw"){
            trackerJSON["match"]["data"][returnKey]["return"][event]=trackerJSON["match"]["data"][returnKey]["return"][event]+1;
            //5.1)Unreturned serve?
            if (event == "re"){
                trackerJSON["match"]["data"][serverKey]["return"]["unreturned_"+serve]=trackerJSON["match"]["data"][serverKey]["return"]["unreturned_"+serve]+1;
                if (serve == "1"){
                    //fe on first serve
                    trackerJSON["match"]["data"][serverKey]["points"]["fe"]=trackerJSON["match"]["data"][serverKey]["points"]["fe"]+1;
                }
                else{
                    //ue on second serve
                    trackerJSON["match"]["data"][returnKey]["points"]["ue"]=trackerJSON["match"]["data"][returnKey]["points"]["ue"]+1;
                }
            }
            //rw
            else{
                trackerJSON["match"]["data"][returnKey]["points"]["winner"]=trackerJSON["match"]["data"][returnKey]["points"]["winner"]+1;
            }
        }
        //6) If ball is in play (can end with winner, fe, ue)
        if (event == "winner" || event == "fe" || event == "ue"){
            //["points"]event[i]
            trackerJSON["match"]["data"][playerEvent]["points"][event] = trackerJSON["match"]["data"][playerEvent]["points"][event] + 1;
        }

        //add to total points
        trackerJSON["match"]["data"][winner]["points"]["total_points_won"]=trackerJSON["match"]["data"][winner]["points"]["total_points_won"]+1;

        //reset currentServe
        currentServe = 1;
    }
    else{
        //point is not over
        //nothing to log
        //fault
        console.log("in play...")
    }
    //update live tracker information
    updateTrackerLive();
}

//Main Functions

function updateTrackerLive(){
    //mainTracker html element
    newElement = JSON.stringify(trackerJSON)
    document.getElementById("mainTracker").innerHTML =
    `
    <br>
    <p>`+players[0]+` vs. `+players[1]+`</p>
    <table align="center" border=1>
        <tbody>
        <tr align="center">
            <td colspan="3"><u><b>Service</b></u></td>
        </tr>
        <tr align="center">
            <td>`+(Math.round((trackerJSON["match"]["data"][0]["service"]["first_serve_p"]) * 100))+`%</td>
            <td>1st %</td>
            <td>`+(Math.round((trackerJSON["match"]["data"][1]["service"]["first_serve_p"]) * 100))+`%</td>
        </tr>
        <tr align="center">
            <td>`+trackerJSON["match"]["data"][0]["service"]["df"]+`</td>
            <td>DF</td>
            <td>`+trackerJSON["match"]["data"][1]["service"]["df"]+`</td>
        </tr>
        <tr align="center">
            <td>`+trackerJSON["match"]["data"][0]["service"]["total_services"]+`</td>
            <td>Services</td>
            <td>`+trackerJSON["match"]["data"][1]["service"]["total_services"]+`</td>
        </tr>
        <tr align="center">
            <td>`+(trackerJSON["match"]["data"][0]["return"]["unreturned_1"]+trackerJSON["match"]["data"][0]["return"]["unreturned_2"])+`</td>
            <td>Unreturned</td>
            <td>`+(trackerJSON["match"]["data"][1]["return"]["unreturned_1"]+trackerJSON["match"]["data"][1]["return"]["unreturned_2"])+`</td>
        </tr>
        <tr align="center">
            <td colspan="3"><u><b>Retour</b></u></td>
        </tr>
        <tr align="center">
            <td>`+trackerJSON["match"]["data"][0]["return"]["re"]+`</td>
            <td>Erreur</td>
            <td>`+trackerJSON["match"]["data"][1]["return"]["re"]+`</td>
        </tr>
        <tr align="center">
            <td>`+trackerJSON["match"]["data"][0]["return"]["rw"]+`</td>
            <td>Winner</td>
            <td>`+trackerJSON["match"]["data"][1]["return"]["rw"]+`</td>
        </tr>
        <tr align="center">
            <td colspan="3"><u><b>Points</b></u></td>
        </tr>
        <tr align="center">
            <td>`+trackerJSON["match"]["data"][0]["points"]["total_points_won"]+`</td>
            <td>Points Gagnés</td>
            <td>`+trackerJSON["match"]["data"][1]["points"]["total_points_won"]+`</td>
        </tr>
        <tr align="center">
            <td>`+trackerJSON["match"]["data"][0]["points"]["winner"]+`</td>
            <td>Winners</td>
            <td>`+trackerJSON["match"]["data"][1]["points"]["winner"]+`</td>
        </tr>
        <tr align="center">
            <td>`+trackerJSON["match"]["data"][0]["points"]["ue"]+`</td>
            <td>Unforced</td>
            <td>`+trackerJSON["match"]["data"][1]["points"]["ue"]+`</td>
        </tr>
        <tr align="center">
            <td>`+trackerJSON["match"]["data"][0]["points"]["fe"]+`</td>
            <td>Forced</td>
            <td>`+trackerJSON["match"]["data"][1]["points"]["fe"]+`</td>
        </tr>
        <tr align="center">
            <td>`+(trackerJSON["match"]["data"][0]["points"]["winner"]+trackerJSON["match"]["data"][0]["points"]["fe"]-trackerJSON["match"]["data"][0]["points"]["ue"])+`</td>
            <td>Marge</td>
            <td>`+(trackerJSON["match"]["data"][1]["points"]["winner"]+trackerJSON["match"]["data"][1]["points"]["fe"]-trackerJSON["match"]["data"][1]["points"]["ue"])+`</td>
        </tr>
        </tbody>
    </table>
    `;
}

function showScore(){
    //update score table
    //can we make both if statements in one?
    var tableString = 
    `
    <table border="1" align="center">
        <tbody>
            <tr>
    `;
    //who serves?
    if (serverKey == 0){
        tableString = tableString + "<td>*</td>";
    }
    else {
        tableString = tableString + "<td></td>";
    }
    tableString = tableString +
    `
                <td>`+players[0]+`</td>
                <td>`+showGoodScore(score[0])+`</td>
                <td>`+total_score[0][0]+`</td>
                <td>`+total_score[1][0]+`</td>
                <td>`+total_score[2][0]+`</td>
                <td>`+theTiebreak[0]+`</td>
            </tr>
            <tr>
    `;
    //who serves
    if (serverKey == 0){
        tableString = tableString + "<td></td>";
    }
    else {
        tableString = tableString + "<td>*</td>";
    }
    tableString = tableString + 
    `
                <td>`+players[1]+`</td>
                <td>`+showGoodScore(score[1])+`</td>
                <td>`+total_score[0][1]+`</td>
                <td>`+total_score[1][1]+`</td>
                <td>`+total_score[2][1]+`</td>
                <td>`+theTiebreak[1]+`</td>
            </tr>
        </tbody>
    </table>
    `;
    document.getElementById("scoreContainer").innerHTML = tableString;
    
}

function eventManager(newLayout, event, winner, serve, pointStatus, playerEvent){

    //is the point over? (pointStatus)
    if (pointStatus == true){
        //point is over
        //are we in a tiebreak?
        if (tiebreakStatus == true){
            //yes
            theTiebreak[winner] = theTiebreak[winner]+1;
            totalTiebreakPoints = totalTiebreakPoints+1;

            //change server if needed
            if (totalTiebreakPoints%2 == 1){
                serverKey = opposite(serverKey);
                returnKey = opposite(returnKey);
            }

            //is the tiebreak over?
            //at least 7 points and more than 1 point difference
            if (theTiebreak[winner] >= 7 && theTiebreak[winner]-theTiebreak[opposite(winner)] > 1){
                //set win
                total_score[currentSet][winner] = total_score[currentSet][winner]+1;
                //reset tiebreak status and scores
                tiebreakStatus = false;
                theTiebreak[0] = "";
                theTiebreak[1] = "";
                totalTiebreakPoints = 0;
            }
        }
        else {
            //if not in tiebreak, add point to game
            score[winner] = score[winner] + 1;
        }
        //check if point ended the game
        logEvent(winner, playerEvent, event, pointStatus, serve);
        checkIfEndOfGame(winner);
        //update score
        showScore();
    }
    //point is not over (false)
    else{
        console.log("points still ongoing...");
        if (event == "fault"){
            currentServe = 2;
        }
        //log event in tracker
    }

    //after looking if the point was over
    //log event and edit tracker
    //switch layout buttonLayout(newLayout);
    buttonLayout(newLayout);

}

function buttonLayout(layout){
    //change layout
    //<!-- (newLayout, event, winner, serve, pointStatus, playerEvent, otherEvent) -->
    if (layout == 0){//First Layout
        document.getElementById("buttonContainer").innerHTML = 
        `
        <table>
            <tbody align="center">
                <tr>
                    <td><button class="layoutButton" onclick=eventManager(0,"ace",`+serverKey+`,"1",true,`+serverKey+`)>Ace</button></td>
                    <td><button class="layoutButton" onclick=eventManager(0,"rw",`+returnKey+`,"1",true,`+returnKey+`)>Return Winner</button></td>
                </tr>
                <tr>
                    <td><button class="layoutButton" onclick=eventManager(1,"fault",-1,1,false,`+serverKey+`)>Fault</button></td>
                    <td><button class="layoutButton" onclick=eventManager(0,"re",`+serverKey+`,"1",true,`+returnKey+`)>Return Error</button></td>
                </tr>
                <tr>
                    <td colspan="2"><button class="layoutButton" onclick=eventManager(2,"ip",-1,"1",false,`+serverKey+`)>In Play</button></td>
                </tr>
            </tbody>
        </table>
        `
        ;
    }
    else if (layout == 1){
        document.getElementById("buttonContainer").innerHTML = 
        `
        <table>
            <tbody align="center">
                <tr>
                    <td><button class="layoutButton" onclick=eventManager(0,"ace",`+serverKey+`,"2",true,`+serverKey+`)>Ace</button></td>
                    <td><button class="layoutButton" onclick=eventManager(0,"rw",`+returnKey+`,"2",true,`+returnKey+`)>Return Winner</button></td>
                </tr>
                <tr>
                    <td><button class="layoutButton" onclick=eventManager(0,"df",`+returnKey+`,"2",true,`+serverKey+`)>Double Fault</button></td>
                    <td><button class="layoutButton" onclick=eventManager(0,"re",`+serverKey+`,"2",true,`+returnKey+`)>Return Error</button></td>
                </tr>
                <tr>
                    <td colspan="2"><button class="layoutButton" onclick=eventManager(2,"ip",-1,"2",false,`+serverKey+`)>In Play</button></td>
                </tr>
            </tbody>
        </table>
        `
        ;
    }
    else if (layout == 2){
        document.getElementById("buttonContainer").innerHTML = 
        `
        <table>
            <thead>
                <tr>
                    <th><button class="layoutButton" onclick=eventManager(0,"winner",0,`+currentServe+`,true,0)>Winner</button></th>
                    <th><button class="layoutButton" onclick=eventManager(0,"winner",1,`+currentServe+`,true,1)>Winner</button></th>
                </tr>
                </thead>
                <tbody>
                <tr>
                    <td><button class="layoutButton" onclick=eventManager(0,"ue",1,`+currentServe+`,true,0)>Unforced</button></td>
                    <td><button class="layoutButton" onclick=eventManager(0,"ue",0,`+currentServe+`,true,1)>Unforced</button></td>
                </tr>
                <tr>
                    <td><button class="layoutButton" onclick=eventManager(0,"fe",0,`+currentServe+`,true,0)>Forced</button></td>
                    <td><button class="layoutButton" onclick=eventManager(0,"fe",1,`+currentServe+`,true,1)>Forced</button></td>
                </tr>
            </tbody>
        </table>
        `
        ;
    }
    else if (layout == 3){
        document.getElementById("buttonContainer").innerHTML = "<p>Shit's over, go home!</p>"
    }
    else{
        console.log("layout does not exist");
    }
}

function attributeServeStart(server){
    
    console.log("starting match...");
    //first function event
    //attribute server status to player
    serverKey = server;
    returnKey = opposite(server);
    //log start time
    document.getElementById("askForServe").innerHTML = "Match Started<br>"+start_time;

    //load firts button layout
    buttonLayout(0);

    //load first score
    showScore();
}

////////////////
//script start//
////////////////
console.log("starting script...");

//decompose URL
var matchup = decodeURIComponent(window.location.search);
matchup = matchup.substring(2);
const players = matchup.split("-");
console.log("players: "+players);

//load buttons
document.getElementById("askForServe").innerHTML = 
`
<button id="playerServe" onclick="attributeServeStart(0)">`+players[0]+` au service</button>
<button id="playerServe" onclick="attributeServeStart(1)">`+players[1]+` au service</button>
`
;

//load playerContainer
document.getElementById("playerContainer").innerHTML = 
`
<table border="1">
    <tbody>
        <tr>
            <td>`+players[0]+`</td>
            <td>`+players[1]+`</td>
        </tr>
    </tbody>
</table>
`
;

//initialize variables
var total_score = [[0, 0],[0, 0],[0, 0]];//log results of set
var total_sets = [0, 0];//amount of sets won
var game_score = [0, 0];//game values (set score)
var score = [0, 0];//point value (game score)
var currentServe = 1;
var currentSet = 0;
var tiebreakStatus = false;
var theTiebreak = ["", ""];
var totalTiebreakPoints = 0;
var serverKey;
var returnKey;
const pointDict = {
    0: "0",
    1: "15",
    2: "30",
    3: "40",
};
const serveEventDict = {
    "ace": "winner", 
    "df": "ue"
};
const returnEventDict = {
    "rw": "winner",
    "re": "ue"
};

//tracker
const tracker = 
`
{
"match": {
    "data": [
        {
            "service": {
                "total_services": 0,
                "first_serve_p": 0,
                "ace": 0,
                "df": 0,
                "1": 0,
                "2": 0
            },
            "return": {
                "re": 0,
                "rw": 0,
                "unreturned_1": 0,
                "unreturned_2": 0
            },
            "points": {
                "total_points_won": 0,
                "winner": 0,
                "ue": 0,
                "fe": 0,
                "aggresive_margin": 0
            },
            "conversion": {
                "2_service_points_won": 0,
                "1_service_points_won": 0,
                "receiving_points_won": 0,
                "break_points": 0,
                "net_points": 0,
                "approach_points": 0
            },
            "rally_time_won": {
                "average": 0,
                "longest": 0,
                "0-3": 0,
                "0-10": 0,
                "10-20": 0,
                ">20": 0
            },
            "player_name": ""
        },
        {
            "service": {
                "total_services": 0,
                "first_serve_p": 0,
                "ace": 0,
                "df": 0,
                "1": 0,
                "2": 0
            },
            "return": {
                "re": 0,
                "rw": 0,
                "unreturned_1": 0,
                "unreturned_2": 0
            },
            "points": {
                "total_points_won": 0,
                "winner": 0,
                "ue": 0,
                "fe": 0,
                "aggresive_margin": 0
            },
            "conversion": {
                "2_service_points_won": 0,
                "1_service_points_won": 0,
                "receiving_points_won": 0,
                "break_points": 0,
                "net_points": 0,
                "approach_points": 0
            },
            "rally_time_won": {
                "average": 0,
                "longest": 0,
                "0-3": 0,
                "0-10": 0,
                "10-20": 0,
                ">20": 0
            },
            "player_name": ""
        }
    ],
    "final_score": [],
    "match_time": 0
}
}
`;
var trackerJSON = JSON.parse(tracker);//tracker variable
trackerJSON["match"]["data"][0]["player_name"] = players[0];
trackerJSON["match"]["data"][1]["player_name"] = players[1];

//start time
var start_time = new Date();
start_time = start_time.toLocaleTimeString();

////////////////
//script end////
////////////////
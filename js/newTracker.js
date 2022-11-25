//Main Function
function start_match(){

    //containers
    while (matchOver == false){
        //while the match is not over
        while (setOver == false){
            //while the set is not over
            while (gameOver == false){
                //while the game is not over
                while (pointOver == false){
                    //while the point is not over
                    //lastPointWinner must be defined every
                }//point is over
                //log event in tracker
                //edit score
                currentPoints[lastPointWinner] = currentPoints[lastPointWinner]+1;
                //change layout
                button_layout(1);
                //check result for game is over and tiebreaks
                if (currentPoints[lastPointWinner] == 7){
                    //w
                    gameOver = true;
                }
                else if () {

                }
                else{
                    //check if end of game
                }
                //reset pointOver
                pointOver = false;

            }//game is over
            //
        }//set is over
        //add set win
        setWon[lastPointWinner] = setWon[lastPointWinner]+1;
        //append score

        //check if last winner won the match
        if (setWon[lastPointWinner] == 2){
            matchOver = true;
        }

        //reset setOver status
        setOver = false;

    }//end of match

}

//Other Functions
//Changes the layout of the buttons on screen
function button_layout(scene){
    //document.getElementById("button_layer").innerHTML = buttonDict[scene];
}

//script start
console.log("tracker.js staring...");
//get players from urls
var matchup = decodeURIComponent(window.location.search);
matchup = matchup.substring(2);
const players = matchup.split("-");

//initialize all variables
var trackerBackup;//store tracker for "undo"
var matchOver, setOver, gameOver, pointOver, setWon, currentPoints, currentGames, lastPointWinner;
matchOver = setOver = gameOver, pointOver = false;
setWon, currentPoints = [];
//const
const tracker = 0;
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
//will change during match?
const buttonDict = {
    0: "2 buttons [0 au service, 1 au service]",
    1: "",
    2: "",
    3: "",
    4: ""
};

//run
//load starting serve buttons
button_layout(0);//choosing the server will trigger start_match()


//variables dictionnary
//setWon = [] = ammount of sets players have won
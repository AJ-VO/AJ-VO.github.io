function insertText() {
    var myEvents = ['1e', '2e', 'df', 'ue', 'fe', 'w'];
    for (var i = 0; i < myEvents.length; i++){
        document.getElementById(myEvents[i]).innerHTML = 0;
    }
}

function myFunction(event) {
    document.getElementById(event).innerHTML = parseInt(document.getElementById(event).innerText)+1;
    document.getElementById("errorLog").innerHTML = "Added: "+event;
    //create last event
    document.getElementById("lastEvent").innerHTML = event;
}

function cancelEvent() {
    //if still at beginning
    if (document.getElementById("lastEvent").innerText == "Hello"){
        document.getElementById("errorLog").innerHTML = "NO PREVIOUS EVENT";
    }
    //if already canceled
    else if (document.getElementById("lastEvent").innerText == "Canceled") {
        document.getElementById("errorLog").innerHTML = "ALREADY CANCELED PREVIOUS EVENT";
    }
    //passes all tests
    else{
        //get last event
        var myLastEvent = document.getElementById("lastEvent").innerText;//string
        //remove
        document.getElementById(myLastEvent).innerHTML = parseInt(document.getElementById(myLastEvent).innerText)-1;
        document.getElementById("lastEvent").innerHTML = "Canceled";
        document.getElementById("errorLog").innerHTML = "Removed: "+myLastEvent;
    }
}
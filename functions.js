/* ////////////// */
/* C O N N E C T */
/* ////////////// */

let storage = {darkMode: "enabled"}

function changeToLightMode() {
    localStorage.setItem('darkMode', 'disabled');
    var icon = document.getElementById("lightModeIcon");
    icon.name = "sunny-outline";
    icon.style.color = "black";
    document.body.style.backgroundColor = "white";
    // change text color
    var all = document.getElementsByTagName("*");
    for (var i=0, max=all.length; i < max; i++) {
        all[i].style.color = "black";
    }
    // change button backgrounds
    elements = document.getElementsByClassName("button");
    for (var i = 0; i < elements.length; i++) {
        elements[i].style.backgroundColor="white";
    }
    // change checkbox backgrounds
    elements2 = document.getElementsByClassName("selectBoxRect");
    for (var i = 0; i < elements2.length; i++) {
        elements2[i].style.backgroundColor="white";
    }
    
}

function changeToDarkMode() {
    localStorage.setItem('darkMode', 'enabled');
    var icon = document.getElementById("lightModeIcon");
    icon.name = "moon-outline";
    icon.style.color = "white";
    document.body.style.backgroundColor = "black";
    // change text color
    var all = document.getElementsByTagName("*");
    for (var i=0, max=all.length; i < max; i++) {
        all[i].style.color = "white";
    }
    // change button backgrounds
    elements = document.getElementsByClassName("button");
    for (var i = 0; i < elements.length; i++) {
        elements[i].style.backgroundColor="black";
    }
    // change checkbox backgrounds
    elements2 = document.getElementsByClassName("selectBoxRect");
    for (var i = 0; i < elements2.length; i++) {
        elements2[i].style.backgroundColor="black";
    }
}

function changeLightMode(){
    var e = localStorage.getItem("darkMode");
    if (e == "enabled") {
        changeToLightMode();
    } else if (e == "disabled") {
        changeToDarkMode();
    }
}

document.addEventListener("DOMContentLoaded", function(event) {
    var e = localStorage.getItem("darkMode");
    if (e == "enabled") {
        changeToDarkMode();
        localStorage.setItem('darkMode', 'enabled');
    } else if (e == "disabled") {
        changeToLightMode();
        localStorage.setItem('darkMode', 'disabled');
    }
});

function connectSpotifyAcct() {
    if (true) {
        window.location.href = "create.html";
        // TODO: Load Playlists
    } else {
        alert("connecting spotify account...");
    }
}

/* /////////// */
/* C R E A T E */
/* /////////// */

var allPlaylistsSelected = false;

var anyBoxesChecked = [];
var numeroPerguntas = 10;   
for (var i = 0; i < numeroPerguntas+1; i++) {
  anyBoxesChecked.push(false);
}

function selectPlaylist(divObj) {
    allPlaylistsSelected = false;
    var id = divObj.id;
    if (anyBoxesChecked[id] == false) {
        divObj.style.background = "rgba(30, 215, 96, 0.5)";
        anyBoxesChecked[id] = true;
    } else {
        divObj.style.background = "rgba(78, 78, 78, 0.705)";
        anyBoxesChecked[id] = false;
    }
}

function selectAll() {
    if (allPlaylistsSelected) {
        for (var id = 1; id < numeroPerguntas+1; id++) {
            var pl = document.getElementById(id);
            pl.style.background = "rgba(78, 78, 78, 0.705)";
            anyBoxesChecked[id] = false;
        }
        allPlaylistsSelected = false;
    } else {
        for (var id = 1; id < numeroPerguntas+1; id++) {
            var pl = document.getElementById(id);
            if (anyBoxesChecked[id] == false) {
                pl.style.background = "rgba(30, 215, 96, 0.5)";
                anyBoxesChecked[id] = true;
            }
        }
        allPlaylistsSelected = true;
    }
}

var expanded = [];
var genres = 5;   
for (var i = 0; i < genres; i++) {
    expanded.push(false);
}

function showCheckboxes(divObj) {
    var id = divObj.id;
    var checkboxes = document.getElementById("checkboxes" + id);
    if (!expanded[id]) {
        checkboxes.style.display = "block";
        expanded[id] = true;
    } else {
        checkboxes.style.display = "none";
        expanded[id] = false;
    }
}

function createPlaylist() {
    if (true) {
        window.location.href = "customize.html";
    } else {
        alert("creating playlist...");
    }
}

/* ///////////////// */
/* C U S T O M I Z E */
/* ///////////////// */


function addPlaylist() {
    if (true) {
        alert("Adding to Your Spotify");
    } else {
        alert("...");
    }
}


function newPlaylist() {
    if (true) {
        window.location.href = "create.html";
        // TODO: Clear Previous Page
    } else {
        alert("...");
    }
}

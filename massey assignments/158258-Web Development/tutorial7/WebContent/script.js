originalFont = "Times";    // Global variable for original font
fontChanges = Array();  // TODO: rewrite using alternative syntax

function setFont(whichFont) {
    if (originalFont == null) {
        originalFont = document.body.style.fontFamily;
    }
    document.body.style.fontFamily = whichFont;
    fontChanges.push(whichFont);
}

function showChanges() {
    if (fontChanges.length == 0) {
        alert("No changes");
    }
    else {
        s = ''
        for (i in fontChanges) {
            s = s + fontChanges[i] + '<br>';
        }
        document.getElementById("changeList").innerHTML = s
       
    }
}

function revertFont() {
	document.body.style.fontFamily = originalFont;
	fontChanges.push(originalFont);
}
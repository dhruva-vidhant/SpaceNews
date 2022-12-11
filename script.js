function addEmail() {
    //read json file and stores into variable json
    var xmlHttp = new XMLHttpRequest();
    xmlHttp.open( "GET","https://test.dhruvasrinivasa.repl.co/",   
    false); // false for synchronous request
    xmlHttp.send(null);
    console.log(xmlHttp.responseText)
    let json = eval(xmlHttp.responseText)
    let newLat = null
    let newLong = null
    //gets new email, name and location
    var newEmail = document.getElementById("email").value
    var newName = document.getElementById("name").value
    console.log(newName)
    navigator.geolocation.getCurrentPosition((position => {
        newLat = position.lat
        newLong = position.long
    }, console.log));
    //adds to json
    json.push({
        email: newEmail,
        name: newName,
        lat: newLat,
        long: newLong,
        hadIssRecently: 0
    })
    //updates file
    var xmlHttp = new XMLHttpRequest();
    xmlHttp.open( "GET","https://test.dhruvasrinivasa.repl.co/"+JSON.stringify(json),   
    false); // false for synchronous request
    xmlHttp.send( null );
}

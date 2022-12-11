function addEmail() {
    const fs = require('fs')
    //read json file and stores into variable json
    let json = get("https://test.dhruvasrinivasa.repl.co/read", {
        method: "GET",
        headers: {},
    })
    //gets new email, name and location
    var newEmail = Document.getElementById("email")
    var newName = Document.getElementById("name")
    navigator.geolocation.getCurrentPosition((position => {
        let newLat = position.lat
        let newLong = position.long
    }, console.log));
    //adds to json
    json.add({
        email: newEmail,
        name: newName,
        lat: newLat,
        long: newLong,
        hadIssRecently: 0
    })
    //updates file
    get("https://Test.dhruvasrinivasa.repl.co/"+json, {
        method: "GET",
        headers: {}
    })
}

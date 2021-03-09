// Create a request variable and assign a new XMLHttpRequest object to it.
var request = new XMLHttpRequest()

// Open a new connection, using the GET request on the URL endpoint
request.open('GET', 'https://padax.github.io/taipei-day-trip-resources/taipei-attractions.json')
// request.open('GET', 'https://ghibliapi.herokuapp.com/films')

request.onload = function () {
    // Begin accessing JSON data here
    var data = JSON.parse(this.response);

    let divlist = document.createElement("div");
    divlist.className = "content";
    document.body.appendChild(divlist);

    if (request.status >= 200 && request.status < 400) {

        // for (i = 0; i < data.result.results.length; i++) {
        for (i = 0; i < 8; i++) {

            let divitme =document.createElement("div")
            divitme.className = "box";
            divlist.appendChild(divitme)

            let imgitem =document.createElement("img")
            imgitem.src="http://"+data.result.results[i].file.split('http://')[1]
            divitme.appendChild(imgitem)
            
            let textitem =document.createElement("div")
            textitem.className="text"
            textitem.textContent=data.result.results[i].stitle
            divitme.appendChild(textitem)
            // console.log(data.result.results[i].stitle)

            // const divlist = document.createElement('div')
            // divlist.id="test"
            // divlist.className="hi"
            // divlist.textContent=data.result.results[i].stitle
            // document.body.appendChild(divlist);

        }
        // ["result"]["results"] 

    } else {
        console.log('error')
    }

}
// Send request
request.send()

document.body.onload = addElement;

function addElement () {
  var divlist = document.createElement("div");
  divlist.className = "content";
  divlist.textContent="";
  document.body.appendChild(divlist);
}


function SearchName() {
    inputaccount = document.SearchAccountName.account;
    // alert('http://127.0.0.1:3000/api/users?username=' + inputaccount.value)

    // // Create a request variable and assign a new XMLHttpRequest object to it.
    var request = new XMLHttpRequest()
    var Nametext = document.querySelector('.content');
    Nametext.textContent="";
    // // Open a new connection, using the GET request on the URL endpoint
    request.open('GET', 'http://127.0.0.1:3000/api/users?username=' + inputaccount.value, true)


    request.onload = function () {
        if (request.status >= 200 && request.status < 400)
         {
          console.log(request.response, request.responseXML);


        // Begin accessing JSON data here
        let data = JSON.parse(this.response);
        console.log(data);
        // Nametext = document.querySelector('.content');
        Nametext.textContent=data.data.name;
        
        }

    }
    // Send request
    request.send()
}

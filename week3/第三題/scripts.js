// Create a request variable and assign a new XMLHttpRequest object to it.
var request = new XMLHttpRequest()

// Open a new connection, using the GET request on the URL endpoint
request.open('GET', 'https://padax.github.io/taipei-day-trip-resources/taipei-attractions.json')
var boxnumberstart = 0;

var boxnumberend = 8;

request.onload = function () {


    // Begin accessing JSON data here
    let data = JSON.parse(this.response);

    let divlist = document.createElement("div");
    divlist.className = "content";
    document.body.appendChild(divlist);


    if (request.status >= 200 && request.status < 400) {

        // for (i = 0; i < data.result.results.length; i++) {
        for (i = boxnumberstart; i < boxnumberend; i++) {

            let divitme = document.createElement("div")
            divitme.className = "box";
            divlist.appendChild(divitme)

            let imgitem = document.createElement("img")
            imgitem.src = "http://" + data.result.results[i].file.split('http://')[1]
            divitme.appendChild(imgitem)

            let textitem = document.createElement("div")
            textitem.className = "text"
            textitem.textContent = data.result.results[i].stitle
            divitme.appendChild(textitem)


        }

    } else {
        console.log('error')
    }
    let lodding = document.createElement("div");
    lodding.style = "display:flex;align-items:center;justify-content:center;margin-top: 8px;";


    
    lodding.id = "loddingbtn"
    document.body.appendChild(lodding);
    
    let loddingbtn = document.createElement("button");
    loddingbtn.style="width:200px;height:50px;font-size:18px"
    loddingbtn.textContent = "載入更多"
    loddingbtn.id = "button"

    loddingbtn.setAttribute("onclick", "AddBox(this)")
    lodding.appendChild(loddingbtn)
    


}
// Send request
request.send()

function AddBox(element) {

    boxnumberstart += 8;
    boxnumberend += 8;
    // alert(boxnumber)        
    request.onload()
    element.style.display="none"
    // var loadBtn = document.getElementById("loddingbtn");
    // var removeNode = document.getElementById('button');
    // loadBtn.removeChild(loadBtn)

    // loadBtn.style.display="none";
}
//   // 取得容器
//   var myList  = document.getElementById('myList');

//   // 取得 "<li>Item 02</li>" 的元素
//   var removeNode = document.querySelectorAll('li')[1];

//   // 將 myList 下的 removeNode 節點移除
//   myList.removeChild(removeNode);

document.body.onload = addElement;

function addElement() {
  var SearchText = document.createElement("div");
  SearchText.className = "SearchText";
  SearchText.textContent = "";
  document.body.appendChild(SearchText);

  var UpdateText = document.createElement("div");
  UpdateText.className = "UpdateText";
  UpdateText.textContent = "";
  document.body.appendChild(UpdateText);

  var CurrentDiv = document.getElementById("table");
  document.body.insertBefore(SearchText, CurrentDiv);
}
function SearchName() {
  let InputAccount = document.SearchAccountName.account;

  // // Create a request variable and assign a new XMLHttpRequest object to it.
  var Request = new XMLHttpRequest()
  var SearchText = document.querySelector('.SearchText');
  SearchText.textContent = "";
  // // Open a new connection, using the GET request on the URL endpoint
  Request.open('GET', 'http://127.0.0.1:3000/api/users?username=' + InputAccount.value, true)


  Request.onload = function () {
    if (Request.status >= 200 && Request.status < 400) {
      // Begin accessing JSON data here
      let data = JSON.parse(this.response);
      // console.log(data);
      SearchText.textContent = data.data.name;
    }

  }
  // Send request
  Request.send()
}

function UpdateNameData() {
  let UpdateName = document.UpdateAccountName.newname;
  let data = { "name": UpdateName.value }
  // console.log('UpdateName:', UpdateName.value);

  const uri = 'http://127.0.0.1:3000/api/user';
  fetch(uri, {
    method: 'POST',
    // body: encodeURI(JSON.stringify(data)),
    body: JSON.stringify(data),
    headers: {
      'Content-Type': 'application/json'
    }
  })
    .then(res => {
      return res.json();
    })
    .then(result => {
      console.log(result);
      if (result.ok) {
        var UpdateText = document.querySelector('.UpdateText');
        UpdateText.textContent = "更新成功";
        var TitleText = document.querySelector('.headbox2');
        TitleText.textContent = UpdateName.value + "，歡迎登入系統。";
      }
    });

}
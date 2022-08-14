const scan_button = document.getElementById("scan-button")
const scan_div = document.getElementById('reader')


function findTheOne(elemnts,info){

    for (let i =0 ; i < elemnts.length;i++){
        console.log(elemnts[i].innerHTML)
        if(elemnts[i].innerHTML == info){
            elemnts[i].selected = 'selected'
            console.log("selected")
        }
    }
}
let ID = document.querySelector("#id_receiver").querySelectorAll('option')
let currencyElem = document.querySelector("#id_currency_type").querySelectorAll('option')

function onScanSuccess(decodedText, decodedResult) {
    let splitted =decodedText.split("_--_")
    let user = splitted[0]
    let currency = splitted[1]
    let symbol = '$'
    if(currency == "LB"){
        symbol = "L.L."
    }

    findTheOne(ID,user)
    findTheOne(currencyElem,symbol)
    
  }
  
  function onScanFailure(error) {
    // handle scan failure, usually better to ignore and keep scanning.
    // for example:
    console.warn(`Code scan error = ${error}`);
  }
  
  let html5QrcodeScanner = new Html5QrcodeScanner(
    "reader",
    { fps: 10, qrbox: {width: 150, height: 150} },
    /* verbose= */ false);
  html5QrcodeScanner.render(onScanSuccess, onScanFailure);

scan_button.onclick = () => {
  const button = document.getElementById('reader__camera_permission_button')
  
    if (scan_div.style.display != "none"){
        scan_div.style.display = "none"
    }else{
        scan_div.style.display = ''
    }
    button.onclick()
}


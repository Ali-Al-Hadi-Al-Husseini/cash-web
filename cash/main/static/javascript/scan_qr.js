// This method will trigger user permissions
const html5QrCode = new Html5Qrcode("reader");
const scan_button = document.getElementById("scan-button")
const scan_div = document.getElementById('reader')
const openfile = document.getElementById('openfile')
let ID = document.querySelector("#id_receiver").querySelectorAll('option')
let currencyElem = document.querySelector("#id_currency_type").querySelectorAll('option')

function display_camera_output(){
    if (scan_div.style.display != "none"){
        scan_div.style.display = "none"
    }else{
        scan_div.style.display = 'block'
    }
}
function findTheOne(elemnts,info){

    for (let i =0 ; i < elemnts.length;i++){
        if(elemnts[i].innerHTML == info){
            elemnts[i].selected = 'selected'
        }
    }
}

function qrCodeSuccessCallback(decodedText, decodedResult){

    let splitted = decodedText.split("_--_")
    let user = splitted[0]
    let currency = splitted[1]
    let symbol = '$'

    if(currency == "LB"){
        symbol = "L.L."
    }

    findTheOne(ID,user)
    findTheOne(currencyElem,symbol)

    html5QrCode.stop().then((ignore) => {
        // QR Code scanning is stopped.
      }).catch((err) => {
        // Stop failed, handle it.
      });
    
}
function qrCodeFailCallback(){
    handleClick()
}
function handleClick(){

    const config = { fps: 10, qrbox: { width: 250, height: 250 } };
    html5QrCode.start({ facingMode: "environment" }, config, qrCodeSuccessCallback,qrCodeFailCallback);
}
scan_button.onclick = ()=>{
    display_camera_output()

    handleClick()
}

openfile.addEventListener('change', e => {
  if (e.target.files.length == 0) {
    // No file selected, ignore 
    return;
  }

  const imageFile = e.target.files[0];
  // Scan QR Code
  html5QrCode.scanFile(imageFile, true)
  .then(decodedText => {

    let splitted = decodedText.split("_--_")
    let user = splitted[0]
    let currency = splitted[1]
    let symbol = '$'

    if(currency == "LB"){
        symbol = "L.L."
    }

    findTheOne(ID,user)
    findTheOne(currencyElem,symbol)
  })
  .catch(err => {
    // failure, handle it.
    console.log(`Error scanning file. Reason: ${err}`)
  });
});

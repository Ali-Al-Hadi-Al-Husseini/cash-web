package main

import (
	"image/png"
	"os"

	"github.com/boombuler/barcode"
	"github.com/boombuler/barcode/qr"
)

func main(){
	seprator := "?!7865!?"
	generate_qr("1234","100",seprator)
}

func generate_qr(addres string,payment string,seprator string){
		// Create the barcode
		qrCode, _ := qr.Encode(addres + seprator + payment, qr.M, qr.Auto)

		// Scale the barcode to 200x200 pixels
		qrCode, _ = barcode.Scale(qrCode, 400, 400)
	
		// create the output file
		file, _ := os.Create("qrcode.png")
		defer file.Close()
	
		// encode the barcode as png
		png.Encode(file, qrCode)
}
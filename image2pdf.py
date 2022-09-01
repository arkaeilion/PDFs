import img2pdf

with open("1.pdf","wb") as f:
	f.write(img2pdf.convert("audit 2020 1.jpeg"))

with open("2.pdf","wb") as f:
	f.write(img2pdf.convert("audit 2020.jpeg"))
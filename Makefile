file = ""

# example make new file = hoge
new:
	mkdir ${file}
	mkdir ${file}/${file}_a ${file}/${file}_b ${file}/${file}_c ${file}/${file}_d ${file}/${file}_e ${file}/${file}_f
	cp exam.py ${file}/${file}_a/main.py
	cp exam.py ${file}/${file}_b/main.py
	cp exam.py ${file}/${file}_c/main.py
	cp exam.py ${file}/${file}_d/main.py
	cp exam.py ${file}/${file}_e/main.py
	cp exam.py ${file}/${file}_f/main.py
	code ${file}/*
	cd ${file}


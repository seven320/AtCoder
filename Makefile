file = ""

# example make new file = hoge
new:
	acc new abc1
	# mkdir ${file}
	# mkdir ${file}/a ${file}/b ${file}/c ${file}/d ${file}/e ${file}/f
	# cp exam.py ${file}/a/main.py
	# cp exam.py ${file}/b/main.py
	# cp exam.py ${file}/c/main.py
	# cp exam.py ${file}/d/main.py
	# cp exam.py ${file}/e/main.py
	# cp exam.py ${file}/f/main.py

test:
	oj t -c "python3 main.py"


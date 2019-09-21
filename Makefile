name = foo


make:
	mkdir $(name)
	cd $(name)
	touch A.py B.py C.py D.py
	atom A.py B.py C.py D.py	

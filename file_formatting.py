def func_formatting(content):
	content=content.replace("  ", "")
	content=content.split("\n")
	num=0
	file=""
	for i in range (len(content)):
		y="</" in content[i]
		t=content[i].find("<")
		if t== -1 :
			x=False 
		else :
			x=content[i].find("<",t+1)
			if x==-1:
				x=True 
			else :
				x=False 
		if not (x and y) :
			content[i]="    "*num+content[i]+"\n"
		if x and not y:
			num=num+1
		elif  x and y :
				num=num-1
				content[i]="    "*num+content[i]+"\n"
		file=file+content[i] 	
	return file

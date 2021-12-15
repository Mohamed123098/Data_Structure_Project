def func_formatting(content):
	content=content.replace("  ", "")
	content=content.split("\n")
	num=0
	file=""
	for i in range (len(content)):
		y="</" in content[i]
		t=content[i].find("<")
		if i<len(content)-1 :
			next=content[i+1].find("<")
		if i>0:
			previous=content[i-1].find("<")
		if t== -1 :
			x=False 
		else :
			x=content[i].find("<",t+1)
			if x==-1:
				x=True 
			else :
				x=False 
		if not (x and y) :
			if t != -1 and not next :
				content[i]="    "*num+content[i]+"\n"
			if next ==-1:
				content[i]="    "*num+content[i]
		if x and not y:
			num=num+1
		elif  x and y :
				num=num-1
				if previous ==-1: 
					content[i]=content[i]+"\n"
				else :
					content[i]="    "*num+content[i]+"\n"
		file=file+content[i] 	

	return file
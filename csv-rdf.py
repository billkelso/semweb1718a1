import csv


with open ('out1.csv', 'r', newline='', encoding='utf-8') as ifp:
	
	ir = csv.reader(ifp)
	for	s, p, o in ir:   
		s='_:'+s
		p='<'+p+'>'
		if p=="<http://dilab77.ionio.gr/sw/p12kour/myvocab#ΗΜΕΡΑ>":
			o='"'+o+'"'
		elif p=='<http://dilab77.ionio.gr/sw/p12kour/myvocab#ΕΝΑΡΞΗ>' or p=="<http://dilab77.ionio.gr/sw/p12kour/myvocab#ΛΗΞΗ>": 
			if  len(o)==4:
				o='0'+o
			o='"'+o+':00"^^<http://www.w3.org/2001/XMLSchema#time>'
		else:
			o='<'+o+'>'
		print('{} {} {} .'.format(s,p,o))
			

import re

def function(m): 
	if (m.group(0)=='&amp;'):
		return '&'
  
	elif (m.group(0)=='&gt;'):
		return '>'

	elif (m.group(0)=='&lt;'):
		return '<'

	else:
		return ' '	

s1 = re.compile('<title>(.+?)</title>') 
s2 = re.compile('<!--.*?-->',re.DOTALL) 
s3 = re.compile(r'<(s(?:cript|tyle)).*?>.*?</\1>',re.DOTALL) 
s4 = re.compile(r'<a.+?href="(.*?)".*?>(.*?)</a>',re.DOTALL) 
s5_1 = re.compile(r'<.+?>|</.+?>',re.DOTALL) 
s5_2 = re.compile(r'<.+?/>',re.DOTALL) 
s6 = re.compile(r'&(amp|gt|lt|nbsp);') 
s7 = re.compile(r'\s+')

with open('testpage.txt','r') as fp:

	keimeno = fp.read() 
	m = s1.search(keimeno) 
	print(m.group(1)) 
	keimeno = s2.sub(' ',keimeno) 
	keimeno = s3.sub(' ',keimeno) 
	
	for m in s4.finditer(keimeno): 
		print('{} {}'.format(m.group(1),m.group(2))) 
	
	keimeno = s5_1.sub(' ',keimeno) 
	keimeno = s5_2.sub(' ',keimeno) 
	keimeno = s6.sub(function,keimeno) 
	keimeno = s7.sub(' ',keimeno)

	print(keimeno) 

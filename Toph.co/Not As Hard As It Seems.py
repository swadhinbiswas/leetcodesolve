while(True):
	try:
		s=input()
		a=0; x=0; t=[]
		for n in range(len(s)):
			if s[n]=='(' or s[n]=='[': t.append(s[n])
			elif len(t):
				if (s[n]==')' and t[len(t)-1]=='(') or (s[n]==']' and t[len(t)-1] == '['):
					t.pop(); x+=2; a=max(a,x)
					if(len(t)==0): x=0
				else:
					t.clear(); x=0
		print(a)
	except EOFError: break


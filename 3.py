def reverseword(s):    
   w = s.split(" ")        
   nw = [i[::-1] for i in w]
   ns = " ".join(nw)
   return ns

s ="Pace Wisdom Solutions"
print(reverseword(s))	 

s = " the sky is blue"
words = s.split()
words = words[::-1]
r = ""

for word in words:
    r += word + " "
    
r = r.rstrip()
    
print(r)
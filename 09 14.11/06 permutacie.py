import random
text = 'autobus'
T=[]
for i in range(len(text)):
    T.append(text[i])
random.shuffle(T)

perm_text=''
for i in range(len(T)):
    perm_text=perm_text+T[i]
    
print(text)
print(perm_text)

d={}
for i in range(len(text)):
    if not text[i] in d:
        d[text[i]]=perm_text[i]
print(d)

new=''
for i in text:
    new=new+d[i]
print(new)

x={}
for i in range(len(new)):
    if not new[i] in x:
        x[new[i]]=text[i]
print(x)

old=''
for i in new:
    old=old+x[i]
print(old)


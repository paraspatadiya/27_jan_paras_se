txt='hydrogen'
f={}
for char in txt:
    f[char]=f.get(txt,0)+1
print(f)
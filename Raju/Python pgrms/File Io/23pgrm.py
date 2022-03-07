
with open("ab.txt","r") as  f:
    lines = f.read().replace(" ","")
with open("ab.txt","w") as f:
    f.write(lines)
print(lines)

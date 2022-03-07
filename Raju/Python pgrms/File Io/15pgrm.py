import io
f = open("D://Python pgrms//file//raju.txt","rb")
f.seek(5,io.SEEK_SET)
s = f.readline()
print(s)
print(f.tell())


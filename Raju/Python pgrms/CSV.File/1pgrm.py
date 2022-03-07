r1 = '1200 raju tata 26000 23'
r2 = '1330 ram tcs 23402 32'
f = open("csvfile.csv","w")
l = r1.split()
m = ','.join(l)+"\n"
f.write(m)
l = r2.split()
m = ','.join(l)
f.write(m)

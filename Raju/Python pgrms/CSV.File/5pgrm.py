import csv
with open("D:\\Python pgrms\\assignment1\\student_marks.csv",'r') as f:

    csv_reader = csv.reader(f)
    g = list(csv_reader)
    d = {}
    for i in range(0, len(g)):
        if g[i][0] not in d:
            d[g[i][0]]=[int(g[i][2])]
        else:
            d[g[i][0]].append(int(g[i][2]))
    w = max(d.items(),key=lambda x : sum(x[1]))
    print(w[0],":",sum(w[1]))

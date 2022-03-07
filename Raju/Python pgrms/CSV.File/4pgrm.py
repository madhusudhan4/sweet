import csv
with open("D:\\Python pgrms\\assignment1\\student_marks.csv",'r') as f:

    csv_reader = csv.reader(f)
    g = list(csv_reader)
    d = {}
    for i in range(0, len(g)):
        if g[i][1] == 'Mathematics':
            d[g[i][0]] = int(g[i][2])

    print(d)












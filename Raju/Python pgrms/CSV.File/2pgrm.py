import csv

with open("D:\\Python pgrms\\assignment1\\subject_faculty.csv",'r') as f:
    datareader = csv.reader(f)
    for row in datareader:
        print(row)
with open("D:\\Python pgrms\\assignment1\\student_marks.csv",'r') as f:
    datareader = csv.reader(f)
    for row in datareader:
        print(row)


import csv
with open("D:\\Python pgrms\\assignment1\\student_marks.csv",'r') as f:
    csv_reader = csv.reader(f)
    with open("new_csvfile",'w') as h:
        csv_writer = csv.writer(h)
        for line in csv_reader:
            csv_writer.writerow(line)

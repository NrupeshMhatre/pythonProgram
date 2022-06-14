import csv
with open(r"C:\Users\Nrupsh mhatre\Desktop\nrupesh.py\fileHandling\Myfile.csv") as csvfile:
    myreader=csv.reader(csvfile,delimiter=',')
    print("%10s"%"stdNo","%20s"%"stdName","%10s"%"Div")
    print("_______________________________________")
    for row in myreader:
        print("%10s"%row[0],"%20s"%row[1],"%10s"%row[2])

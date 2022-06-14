import csv 
header =['Bookno','Bname','publisher','price']
records=[
        [1,'C++','xyz','aaa',500],
        [2,'python','abc','bbb',550],
        [3,'java','asd','ccc',600]
]
with open('write.csv','w') as cs:
    mywriter=csv.writer(cs,delimiter=',')
    mywriter.writerow(header)
    mywriter.writerows(records)
print('::::Data Saved')
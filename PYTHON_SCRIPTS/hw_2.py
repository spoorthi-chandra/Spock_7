
import xlwt
import re
import array
#Creating workbook and worksheet

def first(str):
    t = str[0]
    return t[:1]
    
    

book = xlwt.Workbook()
sheet = book.add_sheet('python',True)
f = open('silicon_data.txt','r')
row = 0
col = 0
count = 0
r = 0
c = 0
all_lines = f.readlines()
list = ['1,1','1,2','1,3','1,4','1,5','1,6','3,1','3,2']
a = []
w = []
for sort in range(0,len(list)):
    for line in all_lines:
        word = line.split()
                
        for c in range(3,len(word)):
            cell = word[c]
            
            if cell == list[sort]:                    
                    a = w.append(word)
                    d = w
        count = 0
        r += 1
       
sort += 1

for line in range(0,len(w)):
   
    print w[row]
    s = first(d[row])
    for col in range(0,len(w[row])):
        
        cell = w[row][col]
        
        if s == '#':
            sheet.write(row,col,'')
            count = row
        elif (s == '#' and count == row):
            sheet.write(row,col,'')
        else:
            sheet.write(row,col,cell)
            
    count = 0
    row += 1
book.save('hw_2_xcel.xls')   



        



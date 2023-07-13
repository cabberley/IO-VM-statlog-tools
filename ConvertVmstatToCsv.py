
import re

##update the input filename to the vmstat log file you want to convert


filename =  'd:\\temp\\a_sam\\vmstat.log'
filename2 = filename + '.csv'
inputFile = open(filename, 'r')
outputFile = open(filename2, 'w')
headerCaptureIo = False
headerCaptureCpu = False
headerWrite = False
headerIo = ''
headerCpu = ''
iostatTime = ''
avgCpu = ''
rowCount = 1
header1=0
header2=False

while True:
    line = inputFile.readline()
    if not line:
        break
    cleanLine=re.sub(' +', ' ', line)
    lineSplit = cleanLine.split(' ')
    if lineSplit[0][:5] != "procs" and lineSplit[0][:1] != "r":
        x=len(lineSplit)
        y=0
        rowData=''
        while y < (x-3):
            rowData=rowData + lineSplit[y]+ ',' 
            y+=1
        rowData=rowData + lineSplit[x-3] + ' ' + lineSplit[x-2] + ' '+ lineSplit[x-1] 
        outputFile.write(str(rowCount) + ',' + rowData)
        rowCount += 1
    elif not header2 and lineSplit[0][:1] == "r":
        x=len(lineSplit)
        y=0
        while y < (x-3):
            headerIo=headerIo + lineSplit[y]+ ',' 
            y+=1
        #headerIo=headerIo[:len(headerIo)-1]
        outputFile.write('row,' + headerIo + 'date\n')
        header2 = True
        
print(rowCount)
    
        
    

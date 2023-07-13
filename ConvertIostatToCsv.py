
import re

######
# Update the inputFilename name to load the iostat file you want to process
# update the outputSearchList2 & 3 for the device names you want to filter on
# typically I want to extract separately the raw devices and the LVM devices to get a better understanding of the IO


inputFilename =  'd:\\temp\\a_sam\\run.15.iostat.log'
outputFilename1 = inputFilename + '.nofilter.csv'
outputFilename2 = inputFilename + '.filter1.csv'
outputFilename3 = inputFilename + '.filter2.csv'

outputSearchList2 = ["360"]
outputSearchList3 = ["rh", "db", "wi"]

inputFile = open(inputFilename, 'r')
outputFile = open(outputFilename1, 'w')
outputFile2 = open(outputFilename2, 'w')
outputFile3 = open(outputFilename3, 'w')
headerCaptureIo = False
headerCaptureCpu = False
headerWrite = False
headerIo = ''
headerCpu = ''
iostatTime = ''
avgCpu = ''
rowCount = 1

while True:
    line = inputFile.readline()
    if not line:
        break
    elif not headerCaptureIo and line[:6] == "Device":
        #outputFile.write('DateTime,' + re.sub("\s+", ",", line.strip()))
        headerIo = 'DateTime,' + re.sub("\s+", ",", line.strip())
        headerCaptureIo = True
    elif not headerCaptureCpu and line[:7] == "avg-cpu":
        headerCpu = (re.sub("\s+", ",", line.strip()))[9:]
        headerCaptureCpu = True
    elif line[0].isdigit() and line[2] == '/':
        iostatTime = line[:-1]
    elif line[:7] == '       ':
        avgCpu = re.sub("\s+", ",", line.strip())
    elif line[:6] != "Device" and line[:5] != "Linux" and line[:7] != "avg-cpu" and len(line) > 1:
        if not headerWrite:
            outputFile.write('Row,' + headerIo + ',' + headerCpu + '\n')
            outputFile2.write('Row,' + headerIo + ',' + headerCpu + '\n')
            outputFile3.write('Row,' + headerIo + ',' + headerCpu + '\n')
            headerWrite = True
        outputFile.write(str(rowCount) + ',' + iostatTime +','+ re.sub("\s+", ",", line.strip()) + ',' + avgCpu + '\n')        
        for i in outputSearchList2:    
            if line[:1].find(i[:1]) > -1:
                    if line.find(i) > -1:
                        outputFile2.write(str(rowCount) + ',' + iostatTime +','+ re.sub("\s+", ",", line.strip()) + ',' + avgCpu + '\n')
        for i in outputSearchList3:    
            if line[:1].find(i[:1]) > -1:
                    if line.find(i) > -1:
                        outputFile3.write(str(rowCount) + ',' + iostatTime +','+ re.sub("\s+", ",", line.strip()) + ',' + avgCpu + '\n')
   
        rowCount += 1
print(rowCount)
    
        
    

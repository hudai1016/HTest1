import urllib.request
import sys

target_url=("http://archive.ics.uci.edu/ml/machine-learning-""databases/undocumented/connectionist-bench/sonar/sonar.all-data")
data=urllib.request.urlopen(target_url)
xList=[]
labels=[]
for line in data:
    row=line.split(",".encode(encoding="utf-8"))
    xList.append(row)

sys.stdout.write("Row="+str(len(xList))+'\n')
sys.stdout.write("Col="+str(len(xList[1])))

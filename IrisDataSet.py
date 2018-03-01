# Grace Burke, 01/03/2018
# Exercise 5, Input & Output of Iris Data Set
# http://archive.ics.uci.edu/ml/datasets/Iris

with open("Data/IrisData.csv") as Iris:
    for line in Iris:
        col1 = (line.split(',')[0])
        col2 = (line.split(',')[1])
        col3 = (line.split(',')[2])
        col4 = (line.split(',')[3])
        print('{:4s} {:4s} {:4s} {:4s}'\
        .format(col1,col2,col3,col4))

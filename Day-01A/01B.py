#
## Day 01 Puzzle A of the Advent of Code 2024
#   https://adventofcode.com/2024/day/1

file01a = open("C:\_Projects\__dev\Advent_of_Code-2024\Day-01A\input01A.txt", "r")

# Read the input file and split it into a list of integers

# m, n = map(str,input().split())

a_list = list(map(str,  file01a.readlines()))

listB = []
listC = []
listD = []
# print(a_list)
for line in a_list: 
    x, y = map(int,  (line.split())) 
    listB.append((x))
    listC.append((y))

# #listB, listC = a_list
# listB.sort() 
# listC.sort()
# totalDist = 0
# print(listB, listC)

#for i in range(len(listB)):
#    totalDist += (abs(listC[i] - listB[i]))

#print(totalDist)

#items = ['a', 'b', 'a', 'c', 'd', 'd', 'd', 'c', 'a', 'b']
#  counts = {item:listC.count(item) for item in listB}
sims = 0
for item in listB:
    counts = {item:listC.count(item) }
    # listD.append( tuple([item , item:listC.count(item)] ))
    listD.append( tuple([item,listC.count(item)] ))
    sims += item * listC.count(item)

print(counts)
print(listD)
print(sims)

# Close the input file
file01a.close()



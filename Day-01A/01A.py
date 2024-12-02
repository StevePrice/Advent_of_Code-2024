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

#listB, listC = a_list
listB.sort() 
listC.sort()
totalDist = 0
print(listB, listC)
for i in range(len(listB)):
    totalDist += (abs(listC[i] - listB[i]))

# Close the input file

print(totalDist)
file01a.close()

# Find the two numbers that add up to 2020 and return their product

# for i in range(len(numbers)):
#     for j in range(i+1, len(numbers)):
#         if numbers[i] + numbers[j] == 2020:
#             product = numbers[i] * numbers[j]
#             break
            


#
## Day 02 Puzzle A of the Advent of Code 2024
#   https://adventofcode.com/2024/day/2

def isAscending( a, b, c, d, e) -> bool:
    if (( a<b) and (b<c) and (c<d) and (d<e)):
        return True
    else:
        return False

def isD3cending( a, b, c, d, e) -> bool:
    if (( a>b) and (b>c) and (c>d) and (d>e)):
        return True
    else:
        return False



file01a = open("C:\_Projects\__dev\Advent_of_Code-2024\Days\Day-02A\input_test.txt", "r")

# Read the input file and split it into a list of integers

# m, n = map(str,input().split())

reports_list = list(map(str,  file01a.readlines()))
num_safe_reports = 0


# print(reports_list)
for line in reports_list: 
    is_safe_report = False
    a,b,c,d,e = map(int,  (line.split())) 
    # Logic for determining the number of safe reports
    # if line is increasing and diffs are less than 2 then report is safe, num_safe_reports += 1
    # if line is decreasing and diffs are less than 2 then report is safe, num_safe_reports += 1
    # else not safe
    if ((a < b) and (b < c) and (c < d) and (d < e)):
        is_safe_report = True
    if ((a > b) and (b > c) and (c > d) and (d > e)):
        is_safe_report = True
    print('Report[{0}] is {1}').
# Close the input file
file01a.close()


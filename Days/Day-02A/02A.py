#
## Day 02 Puzzle A of the Advent of Code 2024
#   https://adventofcode.com/2024/day/2

from itertools import tee
 
def pairwise(iterable):
    a, b = tee(iterable)
    next(b, None)
    return zip(a, b)
 
def isAscending( a, b, c, d, e) -> bool:
    if (( a<b) and (b<c) and (c<d) and (d<e)):
        return True
    else:
        return False

def isAscending2( a, b, ) -> bool:
    if ( a == b ):
        return False
    if (( a<b) ):
        return True
    else:
        return False

def isDecending( a, b, c, d, e) -> bool:
    if (( a>b) and (b>c) and (c>d) and (d>e)):
        return True
    else:
        return False
    
def isDecending2( a, b) -> bool:
    if ( a == b ):
        return False
    if ( (a>b)  ):
        return True
    else:
        return False

def isGradual( a, b, c, d, e) -> bool:
    if ( ( abs(a-b) <=1 or abs(a-b) <=3) and (abs(b-c) <= 1 or abs(b-c) <=3) and (abs(d-e) <= 1 or abs(d-e) <=3) and (abs(c-d) <= 1 or abs(c-d) <=3) ):
        return True
    else:
        return False

def isGradual2( a, b) -> bool:
    ans = False
    diff = abs(a-b)
    # print ("diff = %i" % diff)
    if (a == b):
        return False
    if ( ( diff > 0) and (diff <= 3) ):
        return True
    else:
        return False
 
def direction(a,b) -> int:
    if (a == b):
        return 0
    if ( a > b) :
        return -1
    else:
        return 1

file01a = open("C:\_Projects\__dev\Advent_of_Code-2024\Days\Day-02A\input.txt", "r")

# Read the input file and split it into a list of integers

# m, n = map(str,input().split())

reports_list = list(map(str,  file01a.readlines()))
num_safe_reports = 0
indx = 0
iline = []
prev_direction = 0
curr_direction = 0
is_safe_report = True
is_gradual = True
#print(reports_list)
for line in reports_list: 
    #iline = map(int,  (line.split())) 
    #print(line)
    iline =list(map(int, line.split()))

    print("---------\n indx: %s " % (indx))
    indx +=1
    print(iline)
    idxr =0
    count=0
    is_gradual = True
    safety_violations = 0
    
    for num in iline:
        count+=1
  
    for i in range(count-1):
        #print(iline[i], iline[i+1])
        is_gradual = True
        is_safe_report = True
        a = iline[i]
        b = iline[i+1]
        
        curr_direction = direction(a,b)
        
        if (i==0):
            prev_direction = curr_direction
            print("b is_safe = %s - is_gradual = %s" % (is_safe_report, isGradual2(a,b)))
            if (isGradual2(a,b) == False):
                is_safe_report = False
                safety_violations += 1
                print("b Itteration[%i]  Using %i , %i ,dir = %i safetyViolations= %i -- is_safe_report = %s " % (i, a,b,curr_direction, safety_violations,is_safe_report))
                # break
            else:
                is_safe_report = True
                print("b Itteration[%i]  Using %i , %i ,dir = %i -- is_safe_report = %s " % (i, a,b,curr_direction, is_safe_report))
        else:
            if (curr_direction != prev_direction):
                #is_safe_report = False
                safety_violations += 1
                print("c Itteration[%i]  Using %i , %i -- is_safe_report = %s -- direction not matching Breaking" % (i, a,b, is_safe_report))
                # break
            else:
                if (isGradual2(a,b) ):
                    is_safe_report = True
                    is_gradual = True
                    print("d Itteration[%i]  Using %i , %i - direction matching isGradual= %s  is_safe_report= %s" % (i, a,b, is_safe_report, is_gradual ))
                else:
                    is_safe_report = False
                    is_gradual = False                    
                    #is_safe_report = False
                    safety_violations += 1
                    print("e Itteration[%i]  Using %i , %i - direction matching isGradual= %s is_safe_report= %s" % (i, a,b, is_gradual, is_safe_report))
                    # break
        print("Safety Violations so far: %i" % safety_violations)            
        prev_direction = curr_direction
    if (safety_violations == 1) or (safety_violations == 0):
        num_safe_reports += 1
        safety_violations = 0
    # print("Using %i , %i -- is_safe_report = %s " % (a,b, is_safe_report))
    print("Num_safe_report = %s " % (num_safe_reports))
        
    
    # Logic for determining the number of safe reports
    # if line is increasing and diffs are less than 2 then report is safe, num_safe_reports += 1
    # if line is decreasing and diffs are less than 2 then report is safe, num_safe_reports += 1
    # else not safe
    # if ((isAscending(a,b,c,d,e) or isDecending(a,b,c,d,e))and isGradual(a,b,c,d,e)): 
    #     is_safe_report = True
    #     num_safe_reports += 1
    # else:
    #     is_safe_report = False
    # print("Report[%i] is %i" % (indx, is_safe_report))
    #print("--------------------------------")

print("Number of safe reports: %i" % (num_safe_reports))
# Close the input file
file01a.close()


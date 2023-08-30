'''
You are planning to go to the 5 nearest tourist spots from your house. So you start calculating the distance of all possible places from your house. //
 The 2d coordinates of the tourist spots are given in a list of tuples lis and the coordinates of your house are in the list pnt.

Complete the function compute_Dist(lis,pnt) that returns a list of tuples consisting of the coordinates of the 5 nearest tourist spots.

Input Format:

The first line consists of two space-separated integers representing the coordinates of your house.
The second line consists of an integer n representing the number of tourist spots for consideration.
After the 2nd line, there will be n lines of input each line will have two space-separated integers representing the coordinates of the tourist spots.
Output Format:

A list of 5 tuples is simply printed
Sample input:

0 0
6
5 5
1 1
2 2
3 3
4 4
6 6
Sample output:

[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)]
Note: You can use Euclidean distance for the calculation of distances. The returned order of coordinates in the list should be //
increasing in terms of distance from the house coordinates. In case the distance is same for 2 points, the order should be same as obtained in the input.
'''
#YOUR CODE GOES HERE
import math
def compute_distance(lis,pnt):
    '''input: lis = list of tuples representing coordinates of tourist spots
       output: a list of tuples of length 5 is expected to be returned.'''
    return math.sqrt((lis[0] - pnt[0])**2 + (lis[1] - pnt[1])**2)
       
def compute_Dist(lis, pnt):
    distances = [(point, compute_distance(point,pnt)) for point in lis]
    distances.sort(key=lambda x: (x[1], lis.index(x[0])))
    nearest_spots = [point[0] for point in distances[:5]]
    return nearest_spots
    
    
#-------------------- Input sessions-------------------------#    
# Input house coordinates
house_coordinates = (0,0)#tuple(map(int, input().split()))

# Input number of tourist spots
n = 6 #int(input())

# Input coordinates of tourist spots
tourist_spots = [(5, 5), (1, 1), (2, 2), (3, 3), (4, 4), (6, 6)] #[tuple(map(int, input().split())) for _ in range(n)]
#print(tourist_spots)

# Calculate and print the 5 nearest tourist spots
nearest_spots = compute_Dist(tourist_spots, house_coordinates)
print(nearest_spots)

for t in range(int(input())):
    n = int(input())
    heights = list(map(int, input().split()))
 
    heights.sort()
 
    while(abs(heights[0]-heights[n-1])>1):
        add = (heights[n-1]-heights[0])//2
        heights[0] += add
        heights[n-1] -= add
        heights.sort()
    print(abs(heights[n-1]-heights[0]))
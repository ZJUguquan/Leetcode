'Largest Rectangle in Histogram'



'First try, get TLE.'
# class Solution:
#     # @param height, a list of integer
#     # @return an integer
#     def largestRectangleArea(self, height):
#         mx, i = 0, 0
#         j = len(height) - 1
#         if j < 0 : return 0
#         while(i<j):
#             mx = max(mx, (j-i) * min(height[i:j]))
#             if (height[i] < height[j]):
#                 i += 1
#             else:
#                 j -= 1
# 		return mx

'modified after http://www.geeksforgeeks.org/largest-rectangle-under-histogram/'


class Solution:
    # @param height, a list of integer
    # @return an integer
    def largestRectangleArea(self, height):
    	s = [];
    	max_area = 0; tp = 0; area_with_top = 0
    	if len(height) == 0:
    		return 0
    	if len(height) ==1:
    		return height[-1]
    	area_with_top = 0
    	i = 0
    	while (i < len(height)):
    		if s == [] or height[s[-1]] <= height[i] :
    			s.append(i)
    			i += 1
    		else:
    			tp = s.pop()
    			if s == []:
    				area_with_top = height[tp] * (i )
    			else:
    				area_with_top = height[tp] * (i - s[-1] -1)
    			if max_area < area_with_top:
    				max_area = area_with_top
    	while( s != []):
    		tp = s.pop()
    		if s == []:
    				area_with_top = height[tp] * (i )
    		else:
    			area_with_top = height[tp] * (i - s[-1] -1)
    		if max_area < area_with_top:
    				max_area = area_with_top
    	return max_area


s = Solution()
Height = [2,1,5,6,2,3] # right
Height= [1,1,2]
print(s.largestRectangleArea(Height))




"""
// C++ program to find maximum rectangular area in linear time
#include<iostream>
#include<stack>
using namespace std;

// The main function to find the maximum rectangular area under given
// histogram with n bars
int getMaxArea(int hist[], int n)
{
    // Create an empty stack. The stack holds indexes of hist[] array
    // The bars stored in stack are always in increasing order of their
    // heights.
    stack<int> s;

    int max_area = 0; // Initalize max area
    int tp;  // To store top of stack
    int area_with_top; // To store area with top bar as the smallest bar

    // Run through all bars of given histogram
    int i = 0;
    while (i < n)
    {
        // If this bar is higher than the bar on top stack, push it to stack
        if (s.empty() || hist[s.top()] <= hist[i])
            s.push(i++);

        // If this bar is lower than top of stack, then calculate area of rectangle
        // with stack top as the smallest (or minimum height) bar. 'i' is
        // 'right index' for the top and element before top in stack is 'left index'
        else
        {
            tp = s.top();  // store the top index
            s.pop();  // pop the top

            // Calculate the area with hist[tp] stack as smallest bar
            area_with_top = hist[tp] * (s.empty() ? i : i - s.top() - 1);

            // update max area, if needed
            if (max_area < area_with_top)
                max_area = area_with_top;
        }
    }

    // Now pop the remaining bars from stack and calculate area with every
    // popped bar as the smallest bar
    while (s.empty() == false)
    {
        tp = s.top();
        s.pop();
        area_with_top = hist[tp] * (s.empty() ? i : i - s.top() - 1);

        if (max_area < area_with_top)
            max_area = area_with_top;
    }

    return max_area;

"""
#User function Template for python3
class Solution:
    def swapNibbles (self, N):
        # code here
        return ( (N & 0x0F)<<4 | (N & 0xF0)>>4 )

#{ 
#  Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N = int(input())


        ob = Solution()
        print(ob.swapNibbles(N))
# } Driver Code Ends
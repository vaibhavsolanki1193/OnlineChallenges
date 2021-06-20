class Solution:
	def setBits(self, N):
		# code here
		return str(bin(N)).count("1")

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		N = int(input())
		ob = Solution()
		ans = ob.setBits(N)
		print(ans)

        """This could be solved using '&' bitwise operator as well 
        def  countSetBits(n):
            count = 0
            while (n):
                count += n & 1
                n >>= 1
            return count
            #Boring 
        """
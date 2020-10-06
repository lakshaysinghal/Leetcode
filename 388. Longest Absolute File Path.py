class Solution:
    def lengthLongestPath(self, input: str) -> int:
        stack = []
        result = 0
        for path in input.split('\n'):
            pathname = path.strip('\t')
            numOfLevel = len(path)-len(pathname)
            while(len(stack)>numOfLevel):
                stack.pop(-1)
            if "." in pathname:
                filePath = "/".join(stack)+"/"+ pathname if len(stack) >0  else pathname
                result = max(result,len(filePath))
            stack.append(pathname)
        return result
                
                
print(Solution().lengthLongestPath("dir\n\tsubdir1\n\tsubdir2\n\t\tfile.ext"))
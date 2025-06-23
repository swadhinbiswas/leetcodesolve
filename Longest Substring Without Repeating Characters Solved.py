class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hashmap={} # take a hashmap
        maxlength=0 # set the max length to 0
        left=0 # set variable left to 0
        for right in range(0,len(s)): # Run loop to range (0.len s)
          while s[right] in hashmap: # cheack the right exist in Hasmap or not
            hashmap.remove(s[left]) # if exist remove the left one
            left+=1 # increse the left +1

          hashmap.add(s[right]) # add the right one
          maxlength=max(maxlength,right-left+1) # find the max length between current
          #max length and the current position of your right pointer


        return maxlength # return the max length 

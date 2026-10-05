def Major_Element(nums):
   freq={}
   for i in nums:
         if i in freq:
              freq[i]+=1
         else:
              freq[i]=1
   max_key=max(freq, key=freq.get)
   return max_key
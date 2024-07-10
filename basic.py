# num=int(input('enter a number '))
# i=1
# while i<num+1:
#     print(i**2)
#     i=i+1
#
#
#
# N=int(input('enter a num'))
# i=1
# mul=1
# while i<N+1:
#     mul=mul*i
#     i+=1
# print(mul)
#
# N=int(input())
# mul=1
# for i in range(1,N+1):
#     mul=mul*i
#     print(mul)
#
# #remove a wovel in string
# N=(input())
# ans=0
# i=0
# while i<len(N):
#     c=N[i]
#     if c=='a' or c=='e' or c=='o' or c=='i' or c=='u':
#         ans+=1
#     i+=1
# print(ans)


from typing import List #list variable is imported
class Solution:  #merging list1 and list2 in ascending
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        for ele in range (m,len(nums1)):
            nums1.pop()
        nums1+=nums2
        nums1.sort()
        print(nums1)
    def remove(self,nums=List[int],val=int): #removing the element and replacing '-'
        while val in nums:
            nums.remove(val)
            nums.insert(val,'_')
        print(nums)
    def removedupli(self,nums=List[int]): #removing the duplicate in list
        k=[]
        nums=set(nums)
        k.extend(nums)
        print('number of element in nums:',len(k),k)
    def removesort(self,nums=[]):
        nums.sort()
        remove_element=nums.pop()
        print(nums)
        print(f'remove element:{remove_element},remaining list:{nums}')


t1=Solution()
t1.removesort([2,2,4,6,8])

t1.removedupli([1,1,2,3,5,4,5,6,7,7,9])
t1.remove([1,1,2,3,5,4,5,6,7,7,9],1)
t1.merge([1,2,3,4,5,6],3,[2,2,4,6,8],3)




# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if head.next == None:
            return True
        arr = []
        arr.append(head.val)
        while head.next != None:
            head = head.next
            arr.append(head.val)
        
        length = len(arr)

        if length % 2 == 0:
            midpoint = length//2
            j = midpoint
            for i in range(midpoint-1, -1, -1):
                if arr[i] == arr[j]:
                    j += 1
                    continue
                else:
                    return False
            return True
        else:
            midpoint = length//2
            j = midpoint+1
            for i in range(midpoint-1, -1, -1):
                if arr[i] == arr[j]:
                    j += 1
                    continue
                else:
                    return False
            return True
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        carry = 0
        addens = l1, l2
        meowmix = end = ListNode()
        while addens or carry:
            carry += sum(a.val for a in addens)
            if addens:
                end.next = addens[0]
                end.next.val = carry % 10
                end = end.next
                addens = [a.next for a in addens if a.next]
            else:
                end.next = ListNode(carry)
            carry //= 10
        return meowmix.next

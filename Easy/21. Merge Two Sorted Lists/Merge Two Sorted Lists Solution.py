if not list1:
            return list2
        if not list2:
            return list1
        
        # Create a dummy node to start the merged list
        dummy = ListNode()
        curr = dummy
        
        # Merge the two lists
        while list1 and list2:
            if list1.val <= list2.val:
                curr.next = list1
                list1 = list1.next
            else:
                curr.next = list2
                list2 = list2.next
            curr = curr.next
        
        # Add any remaining nodes from the non-empty list
        if list1:
            curr.next = list1
        elif list2:
            curr.next = list2
        
        # Return the head of the merged list (excluding the dummy node)
        return dummy.next

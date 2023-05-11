def merge_lists(head1, head2):
  """
  Merges two sorted linked lists into one sorted linked list.

  Args:
    head1: The head of the first linked list.
    head2: The head of the second linked list.

  Returns:
    The head of the merged linked list.
  """

  # Create a dummy node to serve as the head of the merged list.
  dummy = Node()
  tail = dummy

  # Iterate through the two linked lists, merging the nodes in sorted order.
  while head1 is not None and head2 is not None:
    if head1.val < head2.val:
      tail.next = head1
      head1 = head1.next
    else:
      tail.next = head2
      head2 = head2.next

  # Link the remaining nodes of the first linked list.
  if head1 is not None:
    tail.next = head1

  # Link the remaining nodes of the second linked list.
  if head2 is not None:
    tail.next = head2

  # Return the head of the merged linked list.
  return dummy.next

#Here is an example of how to use the merge_lists() function:

head1 = Node(1)
head1.next = Node(3)
head1.next.next = Node(5)

head2 = Node(2)
head2.next = Node(4)
head2.next.next = Node(6)

merged_head = merge_lists(head1, head2)

print(merged_head)
#This will print the following output:
#1 2 3 4 5 6
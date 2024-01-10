# stack implementation using list

# size method to determine size of stack
def size(stack):
    """
    stack: gonna pass stack 
    return value will be size of stack in integer
    """
    return len(stack)

# is_empty method to check empty or not
def is_empty(stack):
    """
    stack: gonna pass stack
    return value is boolean empty -> true else fasle
    """
    return len(stack) == 0

# initialized empty list to perform stack operation
stack = []

# append method is used to push element into stack
stack.append('a')
stack.append('m')
stack.append('z')

# now stack contains
print('Initail stack')
print(stack)

# pop method is used to pop element from stack
stack.pop()

# now stack contains
print('After pop operation')
print(stack)

# calculating stack size
print(size(stack))

# check if stack is empty or not
print(is_empty(stack))

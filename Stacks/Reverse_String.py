def reverse_string(string):
    stack = []
    reversed_string = ""
    for s in string:
        stack.append(s)

    for s in string:
        reversed_string += stack.pop()
    return reversed_string

print(reverse_string("hello"))
def reverse_string(word):
    stack=[]

    for ch in word:
        stack.append(ch)

    reverse=""
    while stack:
        reverse+=stack.pop()
    return reverse
print(reverse_string("Hello"))
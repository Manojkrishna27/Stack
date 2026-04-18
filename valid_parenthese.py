def valid_parenthesis(s):
    stack=[]  # always think stack is vertical of array
    for ch in s:
        if ch in "({[": # opening present append
            stack.append(ch)
        else:
            if not stack:
                return False
            top=stack.pop()   # this take peek value of open

            if ch==")" and top !="(": # campoare to close 
                return False
            if ch=="[" and top !="]":
                return False
            if ch =="{" and top !="}":
                return False
    return len(stack)==0
vaild=valid_parenthesis("{([])}")
print(vaild)
notvalid=valid_parenthesis("[](})")            
print(notvalid)
from stack import Stack

def is_match(x,y):
    if x == '(' and y==')':
        return True
    elif x== '[' and y==']':
        return True
    elif x=='{' and y=='}':
        return True
    else:
        return False

def is_balance(paren_string):
    s = Stack()
    is_balance= True
    index = 0

    while len(paren_string)>index and is_balance:
        paren = paren_string[index]
        if paren in "({[":
            s.push(paren)
        else:
            if s.is_empty():
                is_balance = False
            else:
                top = s.pop()
                if not is_match(top,paren):
                    is_balance = False
        index += 1

    if is_balance and s.is_empty():
        return True
    else:
        return False

print(is_balance("({[([{}])]})"))

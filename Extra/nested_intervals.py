from collections import deque 

def nested_intervals(equation):
    #equation = equation.split() # turns into 1 size array for len
    equation = equation.replace(" ", "")  # eliminate any existing whitespace
    stack = deque()
    for i in equation:
        if i in ("[","{","("):            
            stack.append(i)               # add left bracket to deque (double ended queue)
        elif i in ("]", "}", ")"):        
            if not stack:   
                return False              # FALSE if right bracket found without any left bracket
            check = stack.pop()           # pop most recent left bracket
            print(check+i)
            if not check+i in ("[]", "{}", "()"):  
                return False              # FALSE if left doesnst match right bracket
    return True                           # TRUE finished
if __name__ == '__main__':
    print(nested_intervals("(3+9{12+4})(25)"))
    #print("test")
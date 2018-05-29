

operations = ['add', 'sub', 'mul', 'div', 'mod', 'sqrt']
stack = []
solver = []

def add(a,b):
    return(a+b)
def sub(a,b):
    return(a-b)
def mul(a,b):
    return(a*b)
def div(a,b):
    return((a/b))
def mod(a,b):
    return(a%b)
def sqrt(a):
    return(a**(1/2))

def rpn(input_token):
    for i in input_token:
        if i not in operations:
            stack.append(i)
        else:
            if i == 'add':
                val = add(int(stack[-2]),int(stack[-1]))
                stack.pop(-1)
                stack.pop(-1)
            if i =='sub':
                val = sub(int(stack[-2]),int(stack[-1]))
                stack.pop(-1)
                stack.pop(-1)
            if i =='mul':
                val = mul(int(stack[-2]),int(stack[-1]))
                stack.pop(-1)
                stack.pop(-1)
            if i == 'div':
                 val = div(int(stack[-2]),int(stack[-1]))
                 stack.pop(-1)
                 stack.pop(-1)
            if i == 'mod':
                 val = mod(int(stack[-2]),int(stack[-1]))
                 stack.pop(-1)
                 stack.pop(-1)
            if i == 'sqrt':
                 val = sqrt(int(stack[-1]))
                 stack.pop(-1)
            stack.append(val)
            print(stack)
    print(stack[0])


input_token = """344 114 add 82 61 add add 77 mod 52 24 add 44 25 sub div sqrt mul 459 147 96 sub 17 div 39 17 sub 112 add add add add 41 23 sub 240 15 div 12 7 sub sub sub 15 3060 18 div 136 8 div div sub mul 196 76 add 16 div sub div 168 105769 15551 6469 add mod sqrt 119 17 div 7 mul 60 4 sqrt div sub div div 83 53 sub 240 4 div add 240 120 15 div div sub 21 sub 37 4 sub 20 sub div div div 361 sqrt 112 7 mul sqrt 9356 1231 mod 614 7 add add 17 div add 9 div sub 254 33 45 246 add add 108 3 mul sqrt div add 96 18 3 div 50 add sub 529 sqrt sub div sqrt sub sub 1648 49 26 sub 70 14 div mul 11116 1479 mod 1160 10 div mod add 14 div mul 5054 19 div 5 3 sub mul 2209326 335707 mod 24900 10003 add mod add 159 5 mul 24 16 sub 7 4 sub sub mul add 8542 277 add 2444 mod add add 82322 671 2735 add 521 17 mul add 175 3 mul 60 12 div mul mod 3 mul 288 9 div 1876 392 mod 16 5 sub div 102 2 mul 17 div sub div mul mod mod 2581480 114315 3 mul mod 21561 33652 add 3495 4364 add add mod 5 mul 11431952 1740348 mod 172727 mod 30 117423 add 5 mul add 63678 11596 33657 add 4 2 sub mul add mod mod sqrt 5608 5 mul 34948 4421 mod add sqrt 625 add 2214 27 18 sub div 15 10 sub mul 5642 20 833 add mod 10 26 13 div div mul add add 797 520 add mod add mod add """

rpn(input_token.split())

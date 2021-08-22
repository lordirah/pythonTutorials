#Solution 1

def bracket(a):
    open_brackets = ['{','(','[']
    close_brackets = ['}',')',']']
    bracket_dict = { '{' : '}' ,'(' : ')','[' : ']'}
    bracket_stack = []
    for items in range(len(a)):
        if len(a) > 1:
            if items == 0 and a[items] in open_brackets:
                bracket_stack.append(a[items])
            elif items > 0 and (a[items] in open_brackets or a[items] in close_brackets):
                bracket_stack.append(a[items])
                print(bracket_stack)
                try:
                    if bracket_stack[len(bracket_stack)-1] == bracket_dict[bracket_stack[len(bracket_stack)-2]]:
                        bracket_stack.pop(len(bracket_stack)-1)
                        bracket_stack.pop(len(bracket_stack)-1)
                except:
                    return "Invalid order"
                    break
            else:
                return "Invalid char in string"
                break
        else:
            return "Bracket count must be greater than 1"
    if len(bracket_stack) == 0:
        return "Valid Brackets given"
    else:
        return "Invalid Brackets given"

a = '{()}[({})][]()'
#a = '{}()'
#a = '{'
#a = '{(})'
#a = '{(}'
print(bracket(a))

#Solution 2
import re
#a = '{()}[({})]'
#a = '{}()'
#a = '{'
#a = '{(})'
#a = '{(}'
b = ''

for i in (re.sub('[^\[\]\(\)\{\}]', '' , a)):
    if not b:
        b += i
    elif (i== '}' and b[len(b)-1] == '{'):
        b = b[:len(b)-1]
    elif (i== ')' and b[len(b)-1] == '('):
        b = b[:len(b)-1]
    elif (i== ']' and b[len(b)-1] == '['):
        b = b[:len(b)-1]
    else:
        b += i
print('FAIL' if len(b) >= 1 else 'PASS')
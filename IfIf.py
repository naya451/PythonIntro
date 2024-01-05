import ast

def is_valid_python_code(code):
    try:
        ast.parse(code)
    except SyntaxError:
        return False
    return 'if' in code

text = 
'''
# if a: print("qkrq")
print(qq)
while a:
    print("PP")
'''
print(is_valid_python_code(text))

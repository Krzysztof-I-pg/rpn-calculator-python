# Dictionary holding operator priorities
priority = {
    '+': 1,
    '-': 1,
    '*': 2,
    '/': 2,
    'M': 3,
    '^': 4,
    '(': 0
}
stack = []
output = []
print("give your mathematical operation:")
operation = input()

#grouping digits into multi-digit numbers
tokens = []
for sign in operation:
    if sign.isdigit():
        if tokens and tokens[-1].isdigit():
            tokens[-1] = tokens[-1] + sign
        else:
            tokens.append(sign)
    elif sign != " ":
        tokens.append(sign)
        
#RPN
for token in tokens:
    if token.isdigit():
        output.append(token)
    elif token == '(':
        stack.append(token)
    elif token == ')':
        while stack and stack[-1] != '(':
            output.append(stack.pop())
        stack.pop()
    elif token in ['+', '-', '*', '/', 'M', '^']:
        while stack and priority[stack[-1]] >= priority[token]:
            output.append(stack.pop())
        stack.append(token)
while stack:
    output.append(stack.pop())

print("RPN: ", output)

#RPN Evaluation
for token in output:
            if token in ["+", "-", "*", "/", "M", "^"]:
                down = stack.pop()
                top = stack.pop()
                if token == "+":
                    stack.append(top + down)
                elif token == "-":
                    stack.append(top - down)
                elif token == "*":
                    stack.append(top * down)
                elif token == "/":
                    stack.append(int(float(top) / down))
                elif token == "M":
                    stack.append(top % down)
                elif token == "^":
                    stack.append(top ** down)
            else:
                stack.append(int(token))
print("Result:", stack[0])
x = y = z = t = 0
string_x = string_y = string_z = string_t = ""

notation = "5 1 2 + 4 * + 3 -"
tokens = notation.split(' ')

stack_size = 0

for token in tokens:
    if token in ['+', '-', '*', '/']:
        if stack_size < 2:
            raise ValueError("Expressão inválida: não há números suficientes")
        if token == '+':
            x = y + x
        elif token == '-':
            x = y - x
        elif token == '*':
            x = y * x
        elif token == '/':
            x = y / x

        string_x = f"({string_y} {token} {string_x})"

        y = z
        z = t
        string_y = string_z
        string_z = string_t
        string_t = ""
        stack_size -= 1
    else:
        try:
            value = int(token)
        except Exception:
            exit(f"Token inválido: {token}")
        t = z
        z = y
        y = x
        x = value
        string_t = string_z
        string_z = string_y
        string_y = string_x
        string_x = token
        stack_size += 1
    print(f"Pilha: T={t}, Z={z}, Y={y}, X={x}")

print(f"Expressão na notação algébrica: {string_x}")
print(f"O resultado da expressão algébrica é: {x}")

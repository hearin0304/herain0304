def introduce(c, n):
    print(c * n)

def draw_line_string(msg1, msg2):
    nstr = len(msg1) if len(msg1) > len(msg2) else len(msg2)
    introduce('-', nstr *2)
    print(f'  {msg1}  ')
    print(f'  {msg2}  ')
    introduce('-', nstr *2)

n = input('input his/her name: ')
draw_line_string('Hello', f'{n}, welcome to Seoul.')

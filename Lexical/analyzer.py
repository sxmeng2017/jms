
pos = 0

tok_eof = -1
tok_def = -2
tok_extern = -3
tok_identifier = -4
tok_num = -5
EOF = 'EOF'

Identifier = None
num_val = None

def get_char(path):
    global pos
    with open(path, 'r') as f:
        f.seek(pos, 0)
        char = f.read(1)
        if char == '':
            char = EOF
    pos += 1
    return char

def is_space(char):
    space_char = ' '
    return space_char == char

def is_alpha(char):
    alpha = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    return True if char in alpha else False

def is_num(char):
    num = "0123456789"
    return True if char in num else False

def is_alnum(char):
    alpha = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    num = "0123456789"
    alnum = alpha + num
    return True if char in alnum else False

def get_token(path):
    last_char = ' '
    global Identifier
    global num_val
    while is_space(last_char):
        last_char = get_char(path)
    if is_alpha(last_char):
        Identifier = last_char
        last_char = get_char(path)
        while is_alnum(last_char):
            Identifier += last_char
        if Identifier == "def": return tok_def
        if Identifier == "extern": return tok_extern
    if is_num(last_char) or last_char == '.':
        num_str = last_char
        last_char = get_char(path)
        while is_num(last_char) or last_char == '.':
            num_str += last_char
        num_val = float(num_str)
        return tok_num

    if last_char == '#':
        while last_char != EOF and last_char != '\n' and last_char != 'r':
            last_char = get_char(path)
        if last_char != EOF:
            return get_token(path)

    if last_char == EOF:
        return tok_eof
    this_char = last_char
    last_char = get_char()
    return this_char










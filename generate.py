#!/usr/bin/env python3
# Build a C "Hello World" whose whitespace bytes form a Whitespace "Hello World".

def push(n):
    # Stack IMP = Space. Push cmd = Space. Then sign (Space=+) + binary (MSB first) + LF.
    bits = bin(n)[2:]
    return 'SS' 'S' + ''.join('T' if b == '1' else 'S' for b in bits) + 'L'

def outchar():
    # I/O IMP = Tab,LF.  Output-char cmd = Space,Space.
    return 'TLSS'

msg = "Hello World"
prog = ''.join(push(ord(c)) + outchar() for c in msg) + 'LLL'  # LLL = end program

trans = {'S': ' ', 'T': '\t', 'L': '\n'}
ws = ''.join(trans[c] for c in prog)

assert ws[0] == ' ', "first WS token must be a space so it can hide as the string's space"
first, rest = ws[0], ws[1:]
assert '*/' not in rest  # impossible anyway: rest is only space/tab/newline

c_src = (
    'int/**/printf(const/**/char*,...);'
    'int/**/main(){printf("Hello' + first + 'World");}'
    '/*' + rest + '*/'
)

with open('hello.c', 'w') as f:
    f.write(c_src)

print(f"WS program: {len(ws)} whitespace bytes")
print(f"C file:     {len(c_src)} bytes total, "
      f"{sum(ch in ' \t\n' for ch in c_src)} of them whitespace")

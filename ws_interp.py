import sys
src = open(sys.argv[1], 'rb').read().decode('latin1')
toks = [c for c in src if c in ' \t\n']   # Whitespace ignores everything else
i = 0
def num():
    global i
    sign = 1 if toks[i]==' ' else -1; i+=1
    v = 0
    while toks[i] != '\n':
        v = v*2 + (1 if toks[i]=='\t' else 0); i+=1
    i+=1
    return sign*v
stack=[]; out=[]
while i < len(toks):
    if toks[i]==' ':                      # Stack IMP
        i+=1
        if toks[i]==' ': i+=1; stack.append(num())
        else: raise SystemExit("unexpected stack op")
    elif toks[i]=='\t' and toks[i+1]=='\n':  # I/O IMP
        i+=2
        if toks[i]==' ' and toks[i+1]==' ': i+=2; out.append(chr(stack.pop()))
        else: raise SystemExit("unexpected io op")
    elif toks[i]=='\n' and toks[i+1]=='\n' and toks[i+2]=='\n':  # end
        break
    else:
        raise SystemExit(f"unexpected token at {i}")
print(''.join(out))

def mutate_string(string, position, character):
    st=list(s)
    st[position]=character
    s1=''.join(st)
    return s1

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)

def caesarCipher(s, k):
    k %= 26
    result = ""

    for ch in s:
        if 'a' <= ch <= 'z':
            result += chr((ord(ch) - ord('a') + k) % 26 + ord('a'))
        elif 'A' <= ch <= 'Z':
            result += chr((ord(ch) - ord('A') + k) % 26 + ord('A'))
        else:
            result += ch

    return result


if __name__ == '__main__':
    n = int(input().strip())
    s = input().strip()
    k = int(input().strip())

    print(caesarCipher(s, k))

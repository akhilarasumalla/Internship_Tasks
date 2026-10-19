import os

def caesarCipher(s, k):
    result = []
    k %= 26

    for ch in s:
        if ch.islower():
            result.append(chr((ord(ch) - ord('a') + k) % 26 + ord('a')))
        elif ch.isupper():
            result.append(chr((ord(ch) - ord('A') + k) % 26 + ord('A')))
        else:
            result.append(ch)

    return ''.join(result)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())
    s = input().strip()
    k = int(input().strip())

    result = caesarCipher(s, k)

    fptr.write(result + '\n')
    fptr.close()



def superReducedString(s):
    # Step 1: Create an empty stack
    stack = []

    # Step 2: Process each character
    for ch in s:
        if stack and stack[-1] == ch:
            stack.pop()
        else:
            stack.append(ch)

    # Step 3: Return the result
    if not stack:
        return "Empty String"

    return ''.join(stack)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = superReducedString(s)

    fptr.write(result + '\n')

    fptr.close()

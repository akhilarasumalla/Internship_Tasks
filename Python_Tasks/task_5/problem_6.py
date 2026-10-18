if __name__ == '__main__':
    s = input()
    print(any(True if c.isalnum() else False for c in s))
    print(any(True if c.isalpha() else False for c in s))
    print(any(True if c.isdigit() else False for c in s))
   
    print(any(True if c.islower() else False for c in s))
    print(any(True if c.isupper() else False for c in s))

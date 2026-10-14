def average(array):
    # your code goes here
    s1=set(arr)
    avg=sum(s1)/len(s1)
    return f"{avg:.3f}"

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)

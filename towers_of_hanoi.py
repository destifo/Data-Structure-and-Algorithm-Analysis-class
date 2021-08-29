def hanoi(n, start, end):
    if n == 1:
        print(start, '-->', end)
    else:
        other = 6 - (start + end)
        hanoi(n - 1, start, other)
        print(start, '-->', end)
        hanoi(n -1, other, end)

if __name__ == '__main__':
    input_n, input_start, input_end = map(int, input().split())
    hanoi(input_n, input_start, input_end)

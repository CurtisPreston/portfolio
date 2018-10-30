

if __name__ == '__main__':
    def digits_sum(n):
        s = str(n)
        r = 0
        for c in s:
            r += int(c)
        return r


    def find_n(lower, upper, total):
        for i in range(lower, upper + 1):
            if digits_sum(i) == total:
                return i


    def find_m(lower, upper, total):
        for i in range(upper, lower - 1, -1):
            if digits_sum(i) == total:
                return i


    l = int(input())
    d = int(input())
    x = int(input())
    n = find_n(l, d, x)
    m = find_m(l, d, x)
    print(n)
    print(m)


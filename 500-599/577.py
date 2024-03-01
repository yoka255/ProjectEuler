def main():
    N = 12346
    H = [0] * N
    for i in range(3, N):
        H[i] = 3 * H[i-1] - 3 * H[i-2] + H[i-3]
        if i % 3 == 0:
            H[i] += i//3
    
    for i in [3,4,5,6,20]:
        print(i, H[i])
    print(sum(H))
    
main()
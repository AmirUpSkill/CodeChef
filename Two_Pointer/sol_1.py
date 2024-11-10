def solve():
    t = int(input())
    for _ in range(t):
        n = int(input())
        a = list(map(int, input().split()))
        result = []
        
        # Start from the first element and add it to the result
        if n > 0:
            result.append(a[0])
        
        # Traverse through the sorted array A
        for i in range(1, n):
            if a[i] != a[i - 1]:
                result.append(a[i])
        
        # Print the length of the result
        print("M =", len(result))

        # Print the elements of the result
        print(" ".join(map(str, result)))

if __name__ == "__main__":
    solve()

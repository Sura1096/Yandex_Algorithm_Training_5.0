def profit(N, K, prices):
    maxi = 0
    buy = 0

    for i in range(1, N):
        if i - buy > K:
            buy += 1
        if prices[i] > prices[buy]:
            maxi = max(maxi, prices[i] - prices[buy])
        else:
            buy = i

    return maxi


if __name__ == '__main__':
    N, K = map(int, input().split())
    prices = list(map(int, input().split()))
    print(profit(N, K, prices))
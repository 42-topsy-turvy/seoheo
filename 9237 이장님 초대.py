N = int(input())

#정렬을 하기 위해 list 사용
tree = list(map(int, input().split()))

#리스트 역정렬(내림차순) sort(reverse=True)
tree.sort(reverse=True)

for i in range(N):
    tree[i] = tree[i] + i + 1

#다 자라면 그 다음날 이장님 오신다
print(max(tree) + 1)
n_eng = int(input())
eng_list = set(map(int, input().split()))

n_french = int(input())
french_list = set(map(int, input().split()))

result = list(eng_list ^ french_list)
print(len(result))
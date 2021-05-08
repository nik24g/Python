if __name__ == '__main__':
    lst = list()
    for _ in range(int(input())):
        name = input()
        score = float(input())
        small_lst = [name, score]
        lst.append(small_lst)
    # print(lst)
    lst.sort()
    st = list()
    a = list(map(lambda arg: st.append(arg[1]), lst))
    st.sort()
    # print(st)
    def find(st):
        if st[0] == st[1]:
            if st[1] == st[2]:
                pass
            else:
                return st[2]
        else:
            return st[1]


    n = find(st)
    final_lst = list()
    for a, b in lst:
        if b == n:
            final_lst.append(a)
    for i in final_lst:
        print(i)

# Harry
# 37.21
# Berry
# 37.21
# Tina
# 37.2
# Akriti
# 41
# Harsh
# 39
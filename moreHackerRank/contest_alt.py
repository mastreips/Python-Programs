n_p, m_t = input().split()
n_p = int(n_p)
m_t = int(m_t)

the_list = [int(input()) for _ in range(n_p)]
couple_list = [i+j for i in the_list for j in the_list if i != j]
#print(couple_list)
count_zero_list = [str(the_sum).count("0") for the_sum in couple_list]
#print(count_zero_list)
#new_t = [m_t - i for i in count_zero_list]
#print(new_t)
# if max(new_t) == m_t:
#     print(max(new_t))
# else:
#     print(max(new_t) - min(new_t))
#print(max(new_t) - min(count_zero_list))
print(m_t - min(count_zero_list))
print(int(count_zero_list.count(min(count_zero_list)) / 2))

#it seems because not all the length of couple_list equeal to m_t
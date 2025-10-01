import sympy as sp
import pandas as pd

k, T, C, L = sp.symbols('k T C L')

total = 15_000
period = 8
c_ost = total
am_lst = []
c_ost_lst = []

for i in range(period):
    am = (C - L) / T
    c_ost -= am.subs({C: total, L: 0, T: period})
    am_lst.append(round(am.subs({C: total, L: 0, T: period}), 2))
    c_ost_lst.append(round(c_ost, 2))

# print("am_lst", am_lst, "\n"
#       "c_ost_lst", c_ost_lst)

aj = 0
c_ost = total
am_lst_2 = []
c_ost_lst_2 = []

for i in range(period):
    am = k * 1 / T * (C - aj)
    c_ost -= am.subs({k: 2, C: total, T: period})
    am_lst_2.append(round(am.subs({k: 2, C: total, T: period}), 2))
    aj += am
    c_ost_lst_2.append(round(c_ost, 2))

# print("am_lst_2", am_lst_2, "\n"
#       "c_ost_lst_2", c_ost_lst_2)

'''
range returns a list of numbers where first argument is start and second is end, but not including end, it means it will generate numbers from [start, end)
'''
Y = range(1, 9)
'''
zip() function returns a zip object, which is an iterator of tuples where the first item in each passed iterator is paired together, and then the second item in each passed iterator are paired together etc.
'''
tbl1 = list(zip(Y, c_ost_lst, am_lst))
tbl2 = list(zip(
    Y,
    c_ost_lst_2,
    am_lst_2,
))
tframe = pd.DataFrame(tbl1, columns=['Y', 'c_ost', 'am'])
tframe2 = pd.DataFrame(tbl2, columns=['Y', 'c_ost_2', 'am_2'])

print(tframe, "\n", tframe2)
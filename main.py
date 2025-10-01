import sympy as sp

k, T, C, L = sp.symbols('k T C L')

total = 100_000
period = 6
c_ost = total
am_lst = []
c_ost_lst = []

for i in range(period):
    am = (C - L) / T
    c_ost -= am.subs({C: total, L: 0, T: period})
    am_lst.append(round(am.subs({C: total, L: 0, T: period}), 2))
    c_ost_lst.append(round(c_ost, 2))

print("am_lst", am_lst, "\n"
      "c_ost_lst", c_ost_lst)

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

print("am_lst_2", am_lst_2, "\n"
      "c_ost_lst_2", c_ost_lst_2)

# import pandas as pd
# '''
# range returns a list of numbers where first argument is start and second is end, but not including end, it means it will generate numbers from [start, end)
# '''
# Y = range(1, 9)
# '''
# zip() function returns a zip object, which is an iterator of tuples where the first item in each passed iterator is paired together, and then the second item in each passed iterator are paired together etc.
# '''
# tbl1 = list(zip(Y, c_ost_lst, am_lst))
# tbl2 = list(zip(
#     Y,
#     c_ost_lst_2,
#     am_lst_2,
# ))
# tframe = pd.DataFrame(tbl1, columns=['Y', 'c_ost', 'am'])
# tframe2 = pd.DataFrame(tbl2, columns=['Y', 'c_ost_2', 'am_2'])

# print(tframe, "\n", tframe2)

# import matplotlib.pyplot as plt
# '''
# subplots() function in matplotlib is used to create a figure and a set of subplots, which is a grid of axes.
# '''
# fig, axes = plt.subplots(1, 3, figsize=(15, 5))

# axes[0].plot(tframe['Y'], tframe['c_ost'], label='Dataset 1', color='blue')
# axes[0].plot(tframe2['Y'], tframe2['c_ost_2'], label='Dataset 2', color='red')
# axes[0].set_title('Linear Cost')
# axes[0].set_xlabel('Y')
# axes[0].set_ylabel('Cost')
# axes[0].legend()
# axes[0].grid(True, alpha=0.3)

# axes[1].pie(am_lst,
#             labels=range(1, period + 1),
#             explode=[0.1] * period,
#             autopct='%1.1f%%',
#             shadow=True,
#             wedgeprops={
#                 'edgecolor': 'k',
#                 'lw': 1,
#                 'ls': '--'
#             },
#             rotatelabels=True)
# axes[1].set_title('Pie cost 1')
# axes[1].axis('equal')

# axes[2].pie(am_lst_2,
#             labels=range(1, period + 1),
#             explode=[0.1] * period,
#             autopct='%1.1f%%',
#             shadow=True,
#             wedgeprops={
#                 'edgecolor': 'k',
#                 'lw': 1,
#                 'ls': '--'
#             },
#             rotatelabels=True)
# axes[2].set_title('Pie cost 2')
# axes[2].axis('equal')

# plt.tight_layout()
# plt.show()

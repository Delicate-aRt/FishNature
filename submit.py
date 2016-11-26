# ---------------------------------- #
# random prediction baseline
# ---------------------------------- #
import pandas as pd
import numpy as np
# ---------------------------------- #

# reading example
# headers = ['image', 'ALB', 'BET', 'DOL', 'LAG', 'NoF', 'OTHER', 'SHARK', 'YFT']
submit = pd.read_table('submit_example.csv', sep=',', header=None)

# random predictions
rand_pr = pd.DataFrame(np.random.rand(1001, 9))

# test prints
# print submit.shape
# print submit.ix[1:, 1:]
# print submit.ix[0:1, 0:1]
# print rand_pr.shape, rand_pr
# print rand_pr.ix[0:, 0:]

# change data
submit.ix[1:, 1:] = rand_pr.ix[0:, 0:]

print submit

submit.to_csv("s.csv", header=False, index=False)

# ---------------------------------- #

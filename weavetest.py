from scipy import weave
import numpy as np

order = np.array( list( range(10) ) )
new_order = np.zeros( order.shape )
a = 2
b = 7
weave.blitz("new_order = order[:a] + order[a:b][::-1] + order[b:]")
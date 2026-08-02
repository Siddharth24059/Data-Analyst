#1. wap in python to display count the soft keyword 
# len : is used to display size of the item.

import keyword as kw

hw_count = len(kw.kwlist)
sw_count = len(kw.softkwlist)
total = hw_count + sw_count

print('Total Keyword :',total)





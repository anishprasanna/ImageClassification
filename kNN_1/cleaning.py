# with open('/Users/Carlos/data_mining/kNN/keel_data/banana-10-fold/banana-10-2tst.dat', 'r+') as f:    
#     for line in f:    
#         lines = f.readlines()
#         for line in lines:
#             if '@' in line:
#                 f.strip(line)


with open('/Users/Carlos/data_mining/kNN/keel_data/banana-10-fold/banana-10-2tst.dat', "r") as f:
    lines = f.readlines()
with open('/Users/Carlos/data_mining/kNN/keel_data/banana-10-fold/banana-10-2tst.dat', "w") as f:
    for line in lines:
        if '@' not in line:
            f.write(line)
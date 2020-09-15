import numpy as np
import matplotlib.pyplot as plt 

with open('./data/kitti.txt', 'r') as f:
    data = f.readlines()

pcd = []
for line in data:
    pcd.append(line.split(' '))

pcd = np.asarray(pcd)

print(pcd[:,3])
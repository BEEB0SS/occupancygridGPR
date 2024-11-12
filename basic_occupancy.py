import os
import numpy as np




folder_path = 'tt-4-18-eleventh'
file_list = [f for f in os.listdir(folder_path) if f.endswith('.npz')]



for file_name in file_list:
    data = np.load(os.path.join(folder_path, file_name))
    point_cloud = data['points'] 

print("Raw", point_cloud.shape)


#Finding channel lengths and widths

num_channels = 50 # This could be optimized
print(point_cloud[:,0])
min_x, max_x = point_cloud[:, 0].min(), point_cloud[:, 0].max()
print("Min_x", min_x)
print("Max_x", max_x)
channel_width = (max_x - min_x) / num_channels
print("Channel Width", channel_width)

min_y, max_y = point_cloud[:, 1].min(), point_cloud[:, 1].max()
print("Min_y", min_y)
print("Max_y", max_y)
channel_length = (max_y - min_y) / num_channels
print("Channel Length", channel_length)

grids = []
start_point = (min_x, min_y)

counter = 1
for i in range(num_channels**2):
    if start_point[1]+channel_length > max_y:
        break
    if start_point[0]+channel_width > max_x:
        start_point = (min_x, min_y + counter*channel_length)
        counter += 1
    grid = [start_point, (start_point[0]+channel_width, start_point[1]+channel_length)]
    #print(grid)
    grids.append(grid)
    start_point = (start_point[0] + channel_width, start_point[1])

#print(grids)

for grid in grids:
    pass
    
    
    
    
    

#min_y, max_y = point_cloud[]

'''
channels = []
for i in range(num_channels):
    start_x = min_x + i * channel_width
    end_x = start_x + channel_width
    channel = point_cloud[(point_cloud[:, 0] >= start_x) & (point_cloud[:, 0] < end_x)]
    channels.append(channel)

channels = np.array(channels)
print("Channels", channels.shape)
'''
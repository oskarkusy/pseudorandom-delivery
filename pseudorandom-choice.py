# Author: @oskarkusy

from random import sample
import os

try:
  filename_out = input('Set report filename: ') + '.txt'
  file_path = open(os.path.join(os.path.dirname(__file__), filename_out), 'w')

  start_val = int(input('Set the lowest conunt of deliveries per day: '))
  end_val = int(input('Set the highest count of deliveries per day: '))
  building_count = int(input('Set count of builings: '))
  sample_list = sample(range(start_val, end_val), 30)

  file_path.write('Pseudorandom choice of delivery for each day of month and pseudorandom choice of delivery destinations based on ID of buildings\' centroids\n\n')
  file_path.write('The lowest conunt of deliveries per day: ' + str(start_val) + '\n')
  file_path.write('The highest conunt of deliveries per day: ' + str(end_val) + '\n\n')

  pseudorandom_list = []
  count = 1

  for i in sample_list:

    file_path.write('%s. day\n' %count)
    file_path.write('Delivery count: ' + str(i) + '\n')
    file_path.write('ID of buildings\' centroids: ' + '\n')

    temp_sample_list = sample(range(1, building_count), i)

    for j in temp_sample_list:

      file_path.write(str(j) + '\n')

    pseudorandom_list.append(temp_sample_list)
    count += 1

    file_path.write('\n')

  file_path.close()

except:
  print('Not numerical value was provided or provided end value is higher than start value.')

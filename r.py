from statistics import mean
data = []
lengthNum = []
count = 0
with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line.strip())
		lengthNum.append(len(data[count]))
		count += 1
print(mean(lengthNum))
# print('read in all lines, total ', len(data), ' lines')
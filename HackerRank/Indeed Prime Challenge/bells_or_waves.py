num_points = int(raw_input())
data = [[float(coord) for coord in raw_input().split()] for _ in range(num_points)]
axis_crossings = 0
wave_type = 'sine-wave'

for i in range(len(data) - 4):
	if int(data[i][1]*100000) == int(data[i+1][1]*100000) and int(data[i+1][1]*100000) == int(data[i+2][1]*100000) and int(data[i+2][1]*100000) == int(data[i+3][1]*100000) and int(data[i+3][1]*100000) == int(data[i+4][1]*100000):
		wave_type = 'square-wave'
		break
print(wave_type)

for i in range(len(data) - 1):
	if (data[i][1] >= 0 and data[i+1][1] < 0) or (data[i][1] <= 0 and data[i+1][1] > 0):
		axis_crossings += 1
print(axis_crossings//2)
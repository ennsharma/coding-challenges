import sys

N, Q = [int(x) for x in raw_input().split()]
arr = [int(x) for x in raw_input().split()]
for _ in range(Q):
	query = [int(x) for x in raw_input().split()]
	if query[0] == 1:
		min_index, min_num = sys.maxint, sys.maxint
		for i in range(query[1] - 1, query[2]):
			if arr[i] == 0:
				print(str(0) + " " + str(query[1]) + " " + str(query[2]))
				break

			if arr[i] < min_num:
				min_num, min_index = arr[i], i
		same_index = []
		for i in range(query[1] - 1, query[2]):
			if arr[i] == min_num:
				same_index.append(i)

		max_length, min_up_index, min_down_index = 0,sys.maxint,sys.maxint
		found_longer = True
		for index in same_index:
			up_index = index + 1
			down_index = index - 1
			if up_index >= query[2]:
				if arr[down_index] != 1:
					print(str(min_num) + " " + str(min_index + 1) + " " + str(min_index + 1))
					found_longer = False
					break
			elif down_index < query[1] - 1:
				if arr[up_index] != 1:
					print(str(min_num) + " " + str(min_index + 1) + " " + str(min_index + 1))
					found_longer = False
					break
			elif ((arr[up_index] != 1) and (arr[down_index] != 1)):
				print(str(min_num) + " " + str(min_index + 1) + " " + str(min_index + 1))
				found_longer = False
				break
			while (up_index <= query[2] and arr[up_index] == 1):
				up_index += 1
			while (down_index >= query[1] and arr[down_index] == 1):
				down_index -= 1

			if up_index - down_index > max_length:
				max_length, min_up_index, min_down_index = up_index - down_index, up_index, down_index

		if found_longer:
			print(str(min_num) + " " + str(min_down_index + 1) + " " + str(min_up_index + 1)) 

		
	elif query[0] == 2:
		arr[query[1] - 1] = query[2]
# nums = {0:0, 1:3, 2:3, 3:5, 4:4, 5:4, 6:3, 7:5, 8:5, 9:4,
# 	10:3, 11:6, 12:6, 13:8, 14:8, 15:7, 16:7, 17:9, 18:8, 19:8,
# 	20:6, 30:6, 40:5, 50:5, 60:6, 70:7, 80:6, 90:6}

nums = {0:"", 1:"one", 2:"two", 3:"three", 4:"four", 5:"five", 6:"six", 7:"seven", 8:"eight", 9:"nine",
	10:"ten", 11:"eleven", 12:"twelve", 13:"thirteen", 14:"fourteen", 15:"fifteen", 16:"sixteen", 17:"seventeen", 18:"eighteen", 19:"nineteen",
	20:"twenty", 30:"thirty", 40:"forty", 50:"fifty", 60:"sixty", 70:"seventy", 80:"eighty", 90:"ninety"
	
}

res = 0

# for i in range(1, 1000):
# 	word = ""
# 	if i >= 100:
# 		if i % 100 != 0:
# 			res += len("and")
# 		res += nums[i // 100] + len("hundred")
# 	if i % 100 >= 20:
# 		res += nums[i % 10] + nums[((i % 100)//10)*10]
# 	else:
# 		res += nums[i % 100]
	
for i in range(1, 1000):
	word = ""
	if i >= 100:
		word += nums[i//100] + " hundred"
		if i % 100:
			word += " and "
	if i % 100 >= 20:
		word += nums[((i % 100)//10)*10] + " " + nums[i % 10]
	else:
		word += nums[i % 100]
	print(i, word)
	res += sum([len(x) for x in word.split()])


print(res + len("onethousand"))
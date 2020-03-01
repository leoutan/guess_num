import random
while True:
	small = input('請輸入猜數字範圍最小值： ')
	big = input('請輸入猜數字範圍最大值： ')
	small = int(small)
	big = int(big)
	if small < big:
		break
	else:
		print('請輸入正確的大小值')
r = random.randint(small, big)
i = 0
while True:
	i += 1
	num = input('請猜數字從' + str(small) +'到' + str(big) + ':')
	#將數字及字串同時寫在input，須先將數字轉為字串，並用加號合併，加號須以英文格式（紅色）輸入
	num = int(num)
	if num == r:
		print('你猜對了！')
		break
	elif num > r:
		print('比答案大')
	elif num < r:
		print('比答案小')
print('您總共猜了', i, '次')
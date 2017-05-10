import math

def isPalindrome(num):
	num = str(num)
	
	for i in range(math.ceil(len(num)/2.0)):
		if num[i] != num[len(num) - i - 1]:
			return False
		
	return True
		

if __name__ == "__main__":
	
	maxP = 0
	
	for i in range(900, 1000):
		for j in range(900, 1000):
			v = i * j
			
			if isPalindrome(v) and v > maxP:
				maxP = v
	print maxP
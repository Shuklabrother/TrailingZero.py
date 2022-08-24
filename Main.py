number=float(input ("Enter a no. \n"))

def factorialTrailingZeroes(number):
	count = 0
	i = 5
	while (number//i !=0):
		count+= int(number/i)
		i = i*5
	return count

print(factorialTrailingZeroes(number))
def reverse(str):
	return ' '.join(word[::-1] for word in str.split(" "))


# Driver's Code
st = "1= Siddharth is an Engineer.RollNo is 1234567890"
print(reverse(st))

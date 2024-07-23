n=int(input("Enter number="))
sum=0
t=n
while n>0:
	rem=n%10
	sum=sum*10+rem
	n=n//10
if(t==sum):
	print("It is a palindrome")
else:
	print("It is not a palindrome")

#Starting at 1 and 2
def fib(nthterm):
	num1,num2=1,2
	count=0
	sum=0
	while count<nthterm:
		#print(num1)
		if(num1%2==0):
			sum=sum+num1
		temp=num1+num2
		num1=num2
		num2=temp
		count=count+1
	print(sum)

fib(10)

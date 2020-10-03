from Library import laguerre, syn_div  #importing desired functions

def polynomial(x): #defining the polynomial function
    n = len(a)            # 'a' is the coefficients of the polynomial from higher order term to lower order
    sum = 0
    for i in range(n):
        sum += a[i] * x ** (n - 1 - i) #
    return sum


a = [1, -3, -7, 27, -18]  # coefficients of higher to lower order terms of x^4-3x^3-7x^2+27x-18

b = laguerre(6.9, a, polynomial, 10 ** -6) #making the 1st guess to find the 1st root root and performing synthetic division after finding it
print("1st Root is:",b)
q = syn_div(a, b)

b1 = laguerre(1.5, a, polynomial, 10 ** -6) #making the 2nd guess to find the 2nd root and performing synthetic division after finding it
print("2nd Root is:",b1)
q1 = syn_div(q, b1)

b2 = laguerre(0.5, a, polynomial, 10 ** -6) #making the 3rd guess to find the 3rd root and performing synthetic division after finding it
print("3rd Root is:",b2)
q2 = syn_div(q1, b2)

b3 = laguerre(-15, a, polynomial, 10 ** -6)  #making the 4th guess to find the 4th root and performing synthetic division after finding it
print("4th Root is:",b3)
q3 = syn_div(q2, b3)




#C:\Users\Anshuman\PycharmProjects\pythonProject1\venv\Scripts\python.exe C:/Users/Anshuman/PycharmProjects/pythonProject1/main.py
#1st Root is: 3.0000000000003135
#2nd Root is: 1.9999999904789405
#3rd Root is: 0.9999999999999787
#4th Root is: -3.0000000000000964

#Process finished with exit code 0
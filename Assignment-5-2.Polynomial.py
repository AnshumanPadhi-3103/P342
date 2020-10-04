from Library import laguerre,syn_div

A=[1,-3,-7,27,-18] #coefficient of the polynomial from higher to lower order

b=laguerre(A,4,10**-6) #1st root
q=syn_div(A,b,10**-6) #Reduced polynomial by 1 order


b1=laguerre(q,4,10**-6) #2nd root
q1=syn_div(q,b1,10**-6) #Reduced polynomial by 1 order


b2=laguerre(q1,4,10**-6) #3rd root
q2=syn_div(q1,b2,10**-6)#Reduced polynomial by 1 order


b3=laguerre(q2,4,10**-6)#4th root


print("Roots of the polynomial obtained:",b,b1,b2,b3)
print("Roots of the polynomial obtained after rounding them off:",round(b),round(b1),round(b2),round(b3))



#C:\Users\Anshuman\PycharmProjects\pythonProject1\venv\Scripts\python.exe C:/Users/Anshuman/PycharmProjects/pythonProject1/main.py
#Roots of the polynomial obtained: 3.0000000000000986 2.0000000000019322 0.999999813825891 -2.9999998138442354
#Roots of the polynomial obtained after rounding them off: 3 2 1 -3

#Process finished with exit code 0










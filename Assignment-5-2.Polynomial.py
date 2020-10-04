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













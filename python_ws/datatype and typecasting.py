#data type is used to defined the data in which form 
#int data is used to store the numeric data types
#note in python we don't need to declare the datatypes
#we just assisgn the value in variable
#variable can store any type of value which type of data
age=21
name="harsh"
salary=20000.00

#How to pass the variable inside the print statemnt 
#we have 3 ways to pass the variabe in print statemnt 
#print("my name is"+ name " and salary "+ salary +" and age"+age)
# it generate the type error, reason string only concatenate with string not int
#solution 1:-replace + by , when data type is not string 
print ("my name is: "+name + "and salary",salary,"and age",age)
#solution 2:- pass the variable in print statemnt with f{}
print(f"my name is {name} salary is{salary} and age{age}")
#solution 3:-typecast the data into string
salarystring=str(salary)
agestring=str(age)
print("my name is "+name+ "and salary"+ salarystring+ "and age "+ agestring)

# how to find the type of data we need to use type() function
print(type(name))
print(type(age))
print(type(salary))
# what is map?
# what is lambda?
age = [1,44,23,18,33,11,2,87,23,45,14,54,55,12,42,45]
# please defind adult ages with lambda and map :) very easy
print(list(map(lambda x:"adult" if x>=18 else " not adult please wait :)",age) ))
# exercise 2 ::: enter score and say reject or acc with lambda and map   very easy
score = [60]
my_map = list(map(lambda y: "acepted" if y>=50 else " rejected please more practice ", score ))
print(my_map)
#end day 1




#to day learn generetor

def firstn(n):
    num = 0
    while (num < n ):
        yield num
        num +=1

for i in firstn(20):
    print(i)

#generator its good for memory
#good programmer use that, then also we use that :)
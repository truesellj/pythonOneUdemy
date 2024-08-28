import random
import my_module
# print a random integer from 1 -> 10
# random_integer = random.randint(1,10)
# print(random_integer)

# print variable from imported and self-made module
# print(my_module.my_favorite_number)

#generate a number from 0.0 to 1.0 then manipulate
# to your needs
# rand_num_0_to_1 = random.random() * 10
# print(rand_num_0_to_1)

#geenrate floating point number between 1 & 10
# random_float = random.uniform(1,10)
# print(random_float)

#Coin flip progrm:

randZeroOrOne = random.randint(0,1)

if randZeroOrOne  == 1:
    print("Heads")
else:
    print("Tails")
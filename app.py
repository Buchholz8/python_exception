dragons = 'fire', 'water'
numbers = 2
try:
    wildlife = dragons + numbers
except TypeError:
    print('type error')
except:
    print('something went wrong')
finally: 
    print('finally has run')

def get_float_number():
    try:
        num = input('please enter a number :')
        num = float(num)
        return num
    except ValueError:
        print("Invalid input. Please enter a valid number.")
    except TypeError:
        print('Invalid, must be a number')
    finally:
        print('this will always run')
while(True):
    number_one = get_float_number()
    number_two = get_float_number()
    if(number_two == None or number_one == None):
        print('sorry, please try again')
    else:
        break
added_num = number_one + number_two
print(added_num)

def add_two(num_one , num_two):
    return num_one + num_two
result = add_two(10 , 20)
print(result)

x = 15

if x > 10:
    print('That is a large number!')
elif x == 10:
    print('That is the number 10!')
else:
    print('That is a small number')

fruits = ['apples' , 'pearls' , 'kiwis']

cool_list = [1,2,3,4]

for cool_list in number:

    print(number)
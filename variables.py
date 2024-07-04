#Day 2: 30 Days of python programming

first_name = 'Harry '
last_name = 'Morality '
full_name = first_name + last_name
country = 'Mainland '
city = ' lengendary'
age = 999
current_year = 2024
is_married = False
is_true = True
is_light_on = False
car_brand, car_model, manufacrtured_year, is_electric, fuel = 'Kantaka ', 'Omama ', 2024 , False , 'Disel '

print(f'My name is {full_name}. I am from {city} in the country of {country}. It is the year {current_year}. I am {age} old. {is_married}, I am not marreid')
print (car_brand, car_model, manufacrtured_year, is_electric, fuel)


print(type(first_name),
      type(last_name),
      type(full_name),
      type(country),
      type(city),
      type(age),
      type(current_year),
      type(is_married),
      type(is_true),
      type(is_light_on))
print('the length of my first name is', len(first_name))
print('the legnth of my first name is ', len(first_name), 'compared to that of my last name is', len(last_name))
num_one = 5
num_two = 4
add_num_one_and_two = num_one + num_two
sub_num_one_and_two = num_one - num_two
mul_num_one_and_two = num_one * num_two
div_num_one_and_two = num_one / num_two
mod_num_one_and_two = num_two % num_one
exp_num_one_and_two = num_one ** num_two
fdiv_num_one_and_two = num_one // num_two


#area of a circle = pir^2
#circumference of circle = 2pir
given_radius = 30
area_of_circle = 3.14 * (given_radius ** 2)
circum_of_circle = 2 * 3.14 * given_radius
user_radius = int(input('Enter a radius to calculate the area of circle: '))
area_of_circle = 3.14 * (user_radius ** 2)
print('The area of the circle is ', area_of_circle)


user_first_name = input ('Enter your first name: ')
user_last_name = input ('Enter your last name: ')
user_country = input ('Enter country of Origin: ')
user_age = int(input('How old are you ? '))
age = 68
height = 190.0
comp_numb = 4 + 2j

#area of triangle = 0.5(b * H)
base_triangle = int(input('Enter base of the triangle: '))
height_triangle = int(input('Enter height of the triangle: '))
area_triangle = 0.5 * (base_triangle * height_triangle)
print(area_triangle)

#perimeter of triangle = a + b + c
a = int(input('Enter side 1:'))
b = int(input('Enter side 2:'))
c = int(input('Enter side 3:'))
perimeter = a + b + c
print(perimeter)

#area_rect = length * width peri-rect = 2 * area _rect
length = int(input('Enter the length of the rectangle: '))
width = int(input('Enter the width of the rectangle: '))
area_rect = length * width
peri_rect = 2 * area_rect
print(f'The area of the rectangle is {area_rect} and the perimeter is {peri_rect}')

# (area = pi x r x r) and circumference (c = 2 x pi x r) where pi = 3.14
radius = int(input('Enter the radius of a circle: '))
area_circ = 3.14 * radius ** 2
circum_circ = 2 * 3.14 * radius
print (f'The area of the circle is {area_circ} and cicrcumference of the circle is {circum_circ}')

# linar eqn is y = mx + b, b is  y intercept, x intercept = -b/m where y = 0
# e.g y = 2x - 2
x_intercept = -(-2)/2
print (f'the x intercept for the eqn y = 2x -2 is ({x_intercept}, 0) and the y intercept is (0,2)')

# slope- m = y2 -y1)/(x2- x1)
#e.g. (2,2) and (6,10)
slope = (10-2)/(6-2)
print(f'the slope of points (2,2)(6,10) is {slope}')

# #quadratic +-

len_word1 = len('python')
len_word2 = len('dragon')
equal_words = len_word1 != len_word2
print(f'The length of python is {len_word1} and length of dragon is {len_word2}. Are they equal: {equal_words}')
print('is on found in both python and dragon:', 'on' in 'dragon' and 'on' in 'python')
print('check if jargon is in sentence:', 'jargon' in 'I hope this course is not full of jargon')

print(type(len_word1))
#convert to float and string
print(type(float(len_word1)))
print(type(str(len_word1)))

num = 0
if num % 2 == 0:
    print('even number')
else:
    print('not even number')

test = int(2.7)
test2 = 7//2
are_they_equal = test == test2
print ('is 7//3 == int(2.7):', are_they_equal)
print ('10' == 10)
print (int(9.8) == 10)

hours = int(input('Enter hours worked in this week: '))
hourly_rate = int(input('Enter your hourly_rate: '))

weekly_earnings = hours * hourly_rate
print(weekly_earnings)

years_lived = int(input('Enter years lived on earth: '))
seconds_lived = years_lived * 315360000
print('You have lived ', seconds_lived, 'on earth')

print ('End of program!!!')
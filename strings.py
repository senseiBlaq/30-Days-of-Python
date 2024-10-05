#concatenation
title = 'Thirty ' + 'Days ' + 'Of ' + 'Python'
title1 = 'Coding ' + 'For ' + 'All '

#declaring a variabe and initailising it with a string. Find the length
company = 'Coding For All'
print (company)
print('This is the length og the word \'company:', len(company))

# string case metods
company = company.upper()
print('All words have been capitalized: ', company)
print('All words are in lower case: ',company.lower())
print('Only first letter capitalised: ', company.capitalize())
print('The all cases of the word haS been swapped ',company.swapcase()) #initially was all caps ref line 8
print('Initial caps for each word: ',company.title())

#cutting out a part of string. Finding phrases in a string
company = company.title()
first_word = company [0:6] # slices out 'coding and stores in another variable '
print(company)
print(company.find('Coding'))
print(company.index('Coding'))
print(company.count('Coding'))
print('This replaces \'coding\' with \'python\':',company.replace('Coding', 'Python'))

#replaces a part of a string with another
company2 = 'python for everyone'.title()
print('This replaces \'everyine\' with \'all\':',company2.replace('Everyone','All'))
#another alternative - this method uses slicing and concatenation
new_text = company2[0:11] + 'All'
print(new_text)

# breaking up a string into a list using the split method
company_split = company.split(' ')
print('The sentence has been split by space into a list with the words: ',company_split)#
test_text = 'Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon'
print('The sentence has been split by comma into a list with the words: ',test_text.split(','))
company_first_char = company[0]
company_last_char = company[-1]
print(f'The first charccter in the sentence \'Coding For All\' is {company_first_char} and the last is {company_last_char}')
print(f'The character @ index 10 is {company[10]}')

# make an abbreviation
donor_phrase = 'Python For All'
abbrv = donor_phrase[0] + donor_phrase[7] + donor_phrase[11]
print('The abbreviation is ', abbrv)
donor_phrase2 = 'Coding For All'
abbrv2 = donor_phrase2[0] + donor_phrase2[7] + donor_phrase2[11]
print('The abbreviation is ', abbrv2)

#FInd the position of the occurence of character
print(donor_phrase2.find('C'))
print(donor_phrase2.find('F'))
print(donor_phrase2.rfind('l'))

donor_phrase3 ='You cannot end a sentence with because because because is a conjunction'
sample_result = donor_phrase3.find('because')
sample_result1 = donor_phrase3.rfind('because')
print(sample_result)
print(sample_result1)
print(donor_phrase3[0 : sample_result])

#Starts with
print(donor_phrase2.startswith('Coding'))
print(donor_phrase2.startswith('coding'))
donor_phrase4 = '   Coding For All      '
print(donor_phrase4.strip())

test_text = '30DaysOfPython'
test_text_2 = 'thirty_days_of_python'
print(f'''using isdentifier method 30DaysOfPython is a valid variable name: {test_text.isidentifier()}
      and thirty_days_of_python is {test_text_2.isidentifier()}''')

new_text = '#'.join(['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon'])
print(new_text)

#escapping sequence
print ('I am enjoying this challenge.\nI just wonder what is next.')
print('\nName\t Age\tCountry\tCity\nAsabeneh 250\tFinland\tHel')

#intepolationor f strings
radius = 10
area = 3.14 * radius ** 2
print(f'The area of a circle with {radius} is {area} meters square.\n')
print(f'These are results of math operators done with interpolation \n{8 + 6} \n {8 - 6} \n {8 * 6} \n {8 / 6} \n {8 % 6} \n {8 // 6} \n {8 ** 6}')


print('End of program !!!')


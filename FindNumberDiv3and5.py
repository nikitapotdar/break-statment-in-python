'''Program to find first number divisible by 3 & 5

Write a program to print the first +ve number 'n' in a given
range found to be divisiable by 3 as well as 5.
input -> two numbers for a range r1(lower) & r2(higher)
Result output -> <n> is first number divisible by 3 & 5 between <r1> & <r2>
'''
print('Find first number divisible by 3 & 5 in given range')
r1 = int(input('Enter lower range number : ') or 0)
r2 = int(input('Enter higher range number : ') or 0)
if r1 != r2:
      rng = range(r1, r2 + 1)
      for i in rng:
            if i % 3 == 0 and i % 5 == 0:
                  print(f'{i} is divisible by 3 & 5 in range {r1} to {r2}')
                  break #comment break while you uncomment the print below
            #print(f'{i} not divisible by 3 & 5')#uncomment print to understand break for study
      else:
            print(f"There's no number divisible by 3 & 5 between {r1} to {r2}")
else:
      print('not valid range')

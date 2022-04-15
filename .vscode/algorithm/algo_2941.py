alphabets = input()

pass_list = ['c=','c-','dz=','d-','lj','nj','s=','z=']

alphabets_length =len(alphabets)


for i in range(len(pass_list)):
    if pass_list[i] in alphabets:
        alphabets = alphabets.replace(pass_list[i],'a')

print(len(alphabets))
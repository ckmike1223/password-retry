password = 'a123456'
i = 3 # remaining chances
while i > 0:
	pwd = input('please input your password: ')
	if pwd == password:
		print('login successful!')
		break #break the loop
	else: 
		i = i - 1
		print('password incorrect! you still have', i, 'chances')

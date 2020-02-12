password = 'a123456'
i = 3 # remaining chances
while i > 0:
	i = i - 1
	pwd = input('please input your password: ')
	if pwd == password:
		print('login successful!')
		break #break the loop
	else: 
		print('password incorrect!')
		if i > 0:
			print('you still have', i, 'chances')
		else:
			print('account has been locked!')

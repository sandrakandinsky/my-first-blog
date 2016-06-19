def check(liczba):
	if liczba > 3:
		print('liczba jest większa od 3') 
	elif liczba == 3:
		print ('liczba jest równa 3')
	else:
		print('liczba jest mniejsza od 3')

liczby = [1,3,6]
for a in liczby:
	check(a)
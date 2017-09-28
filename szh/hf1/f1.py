# Feladat: megadni hogy a függvényben kapott szám szökőév-e

def is_leap(yr):
	if (yr % 4 == 0):
		if (yr % 100 == 0):
			if (yr % 400 == 0):
				return True
			else:
				return False
	
	else:
		return False
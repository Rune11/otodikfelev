# Feladat: a hét napjait 0-6 számokkal jelöltük, ha nem vagyunk vakáción akkor 7-kor keülnk hétköznap, hétvégén pedig 10-kor. Vakáció esetén hétköznap 10-kor, hétvégén OFF.

def alarm_clock(day, vac):
	if not vac:
		if day < 5:
			return '7:00'
		else:
			return '10:00'
	else:
		if day < 5:
			return '10:00'
		else:
			return 'OFF'
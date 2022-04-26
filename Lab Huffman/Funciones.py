import math 

def letter_count(text):
	text = text.lower()
	letters = {}
	for x in range(len(text)):
		letters[text[x]] = letters.get(text[x],0) + 1
	return letters
    

def caracter_especial(palabra):
    for letra in palabra:
        c = ord(letra)
        if (c>=97 and c<=122) or (c>=48 and c<=57) or c==241 or c==32:
            pass
        else:
            return False
    return True

def organizacion_probabilidades(conteo):
	sort_conteo = sorted(conteo.items(),key=lambda x: x[1], reverse = True)
	sort_conteo = dict(sort_conteo)

	probabilidades = list(sort_conteo.values())
	llaves = list(sort_conteo.keys())
	prob_llaves = (probabilidades,llaves)
	return prob_llaves

def huffman(keys_prob):
	prob = keys_prob[0]
	path = keys_prob[1]
	len_prob = len(prob)
	for x in range(len_prob,1,-1):
		suma = prob[x-1]+prob[x-2]
		for y in reversed(range(len(prob))):
			if prob[y] >= suma:
				prob.insert(y,suma)
				path.insert(y+1,path[x-2]+path[x-1])
				break
			elif y == 0:
				prob.insert(0,suma)
				path.insert(0,path[x-2]+path[x-1])
		x = x+1
	return path


def get_bin(keys,path):
	bina = keys
	for z in range(len(keys)):
		letter = keys[z]
		for w in range(1,len(path)):
			if path[w].rfind(keys[z]) > -1:
				if w%2 == 0:
					letter = letter+'1'
				else:
					letter = letter+'0'
		bina[z] = letter[1:]
	return bina


def longitud_promedio(probabilidades,binarios,texto):
	for x in range(len(probabilidades)):
		probabilidades[x] = probabilidades[x] / len(texto)
	lon = 0.0
	z = 0
	while z < len(probabilidades):
		lon = lon + probabilidades[z]*len(binarios[z])
		z = z + 1
	return lon


def entropia(probabilidades,texto):
	for x in range(len(probabilidades)):
		probabilidades[x] = probabilidades[x] / len(texto)
	ent = 0.0
	z = 0
	while z < len(probabilidades):
		ent = ent + (-1 * probabilidades[z]*math.log2(probabilidades[z]))
		z = z + 1
	return ent

def eficiencia(entropia,long_prom):
	eficiencia = entropia / long_prom
	eficiencia = int(eficiencia*100)
	return eficiencia

def tasa_compresion(keys,long_prom):
	r = (math.log2(len(keys)))/long_prom
	return r

def back(palabra):
	palabra1= palabra.lower()
	#
	if len(palabra1) >= 10 and len(palabra1) <= 50 : 
		#
		if caracter_especial(palabra1):
			#
			conteo = letter_count(palabra)
			keys_prob = organizacion_probabilidades(conteo)
			path = huffman(keys_prob)
			keys_prob = organizacion_probabilidades(conteo)
			binarios = get_bin(keys_prob[1],path)
			long_prom = longitud_promedio(keys_prob[0],binarios,palabra1)
			keys_prob = organizacion_probabilidades(conteo)
			ent = entropia(keys_prob[0],palabra1)
			efi = eficiencia(ent,long_prom)
			r = tasa_compresion(keys_prob[1],long_prom)
			var = dict(Long = long_prom, Entropia = ent, Eficiencia = efi, Taza_De_Comprencion = r)
			DicBin = dict(zip(keys_prob[1],binarios))
			DicBin.update(var)
			return DicBin
		else:
			return 2
	else :
		return 1

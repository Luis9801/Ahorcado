# 28/04/2022
# Laboratorio de Conmutación
# Universidad Surcolombiana
# Actividad: El Ahoracado con Python
#Estudiantes: Luis Fernando Hoyos-20151134557
#			  Juan Camilo Gualteros-20152140521

#Se definen las funciones que se utilizaran durante el programa
import random
import os
#Se crea una lista "AHORACADO" que contiene las diferentes fases representativas del muñeco del juego.

AHORCADO = ['''
      +---+
      |   |
          |
          |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
          |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
      |   |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
     /|   |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
     /|\  |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
     /|\  |
     /    |
          |
    =========''', '''
      +---+
      |   |
      O   |
     /|\  |
     / \  |
          |
    =========''']
#Se  crea la variable "palabra", que tiene como valor una cadena de texto.
palabras = 'valoracion aprenderpython comida juego python web imposible variable curso volador cabeza reproductor mirada escritor billete lapicero celular valor revista gratuito disco voleibol anillo estrella'.split()#cada palabra separada por un espacio se toma como un elemento independiente formando una lista de palabras.
"""La siguiente funcion se encarga de escoger al azar una palabra aleatoria"""
def buscarPalabraAleat(listaPalabras):#se crea una funcion con argumento listaPalabras
	'''se escoge una palabra aleatoria de la lista palabras con la funcion randint'''
	palabraAleatoria = random.randint(0, len(listaPalabras) - 1)
	return listaPalabras[palabraAleatoria]#La funcion retorna la palabra aleatoria
"""La siguiente funcion se encarga de mostrar en pantalla el muñeco, letras incorrectas y letras correctas"""
def displayBoard(AHORCADO, letraIncorrecta, letraCorrecta, palabraSecreta):
	print ('A H O R C A D O')#Se imprime en pantalla el titulo
	print(AHORCADO[len(letraIncorrecta)])#Se imprime en pantalla la secuencia del muñeco
	print ("")#Se imprime un espacio en blanco
	fin = ""#Se define la variable fin que tiene como valor un espacio 
	print ('Letras incorrectas:', fin)#Se imprime en pantalla un texto con espacio en blanco (fin)
	for letra in letraIncorrecta:#Se la lista de letras incorrectas
		print (letra, end=",")#Se imprime en pantalla cada letra incorrecta separada por una coma
	
	espacio = '_' * len(palabraSecreta)#Se generan una cantidad de raya-baja equivalentes a la longitud o numero de letras de "palabraSecreta" que es la letra que se quiere adivinar
	
	"""Se recorre con un ciclo for la palabra escogida aleatoriamente"""
	for i in range(len(palabraSecreta)):
		if palabraSecreta[i] in letraCorrecta:#Se comprueba que una letra de la cadena es igual a la digitada por el usuario
			espacio = espacio[:i] + palabraSecreta[i] + espacio[i+1:]#Se cocatena cada palabra correcta con las raya-baja anteriormente definidas como "espacio"
	
	for letra in espacio:
		print (letra, fin)

	print ("")
	#La siguiente funcion permite que el usuario digite una letra, tambien verifica que no se repitan y que se encuentre entre las letras del alfabeto.
def elijeLetra(algunaLetra):
	while True:
		print ('Adivina una letra:')
		letra = input()
		letra = letra.lower()
		os.system("cls")
		if len(letra) != 1:
			print ('Introduce una sola letra.')
		elif letra in algunaLetra:
			print ('Ya has elegido esa letra ¿Qué tal si pruebas con otra?')
		elif letra not in 'abcdefghijklmnopqrstuvwxyz':
			print ('Elije una letra.')
		else:
			return letra#La funcion retorna la letra digitada por el usuario
#La funcion empeza, se encarga de continuar reiniciar el juego o cerrarlo		
def empezar():
	print ('Quieres jugar de nuevo? (Si o No)')#Se imprime en pantalla un texto
	return input().lower().startswith('s')#El usuario digita por teclado y luego es convertido a minuscula con el metodo lower, verificando que lo digitado comienza con la letra "s" y se retorna en la funcion
	
"""Se crean las variables letraIncorrecta y letraCorrecta con valor espacio"""
letraIncorrecta = ""
letraCorrecta = ""
palabraSecreta = buscarPalabraAleat(palabras)#Se inicializa la funcion por medio de la variable "palabraSecreta"
finJuego = False#Se crea una variable booleana con valor "False"
"""Por medio de un ciclo while, se ejecuta la funcion displayBoard y se generan las condiciones que permiten conocer las letras acertadas y la finalizacion del juego"""
while True:#Se ejecuta el ciclo mientras la condicion sea "True"
	
	displayBoard(AHORCADO, letraIncorrecta, letraCorrecta, palabraSecreta)#Se ejecuta la funcion
	letra = elijeLetra(letraIncorrecta + letraCorrecta)#Se inicializa la funcion "elijeLetra" y el valor que retorna es almacenado en la variable "letra"
	#Se crea una condicion donde se determina si la letra ingresada se encuentra la palabra secreta
	if letra in palabraSecreta:
		#Por cada letra correcta, se van almacenando en la variable letraCorrecta poara que no se repita
		letraCorrecta = letraCorrecta + letra
		letrasEncontradas = True#Se define letrasEncontradas con True para continuar la ejecucion del programa

		for i in range(len(palabraSecreta)):
			#Si la letra no se encuentra en la palabra que se esta adivinando, se coloca falso y se rompe el ciclo.
			if palabraSecreta[i] not in letraCorrecta:
				letrasEncontradas = False
				break#Se rompe el ciclo for con break y se continua con la ejecucion del programa en la siguiente linea  
		"""Al terminar de encontrar las palabras, imprime en pantalla la palabra acertada y se finaliza el ciclo"""
		if letrasEncontradas:
			print ('¡Muy bien! La palabra secreta es "' + palabraSecreta + '"! ¡Has ganado!')
			finJuego = True
		"""Si lo anterior no se cumple , se almacena cada letra incorrecta en la variable letraIncorrecta"""
	else:

		letraIncorrecta = letraIncorrecta + letra
		#Si la cantidad de letras incorrectas es igual a la longitud de la lista "AHORACADO", es decir, llega a 7, se ejecuta las instrucciones siguientes
		if len(letraIncorrecta) == len(AHORCADO) - 1:

			displayBoard(AHORCADO, letraIncorrecta, letraCorrecta, palabraSecreta)#Se llama la funcion displayBoard
			print ('¡Se ha quedado sin letras!\nDespues de ' + str(len(letraIncorrecta)) + ' letras erroneas y ' + str(len(letraCorrecta)) + ' letras correctas, la palabra era "' + palabraSecreta + '"')#Se imprime en pantalla la cantidad de letras correctas e incorrectas al superar el numero de fallos(7) y se finaliza el juego
			finJuego = True
		#Si la letra es adivinada correctamente, se finaliza el juego	
	if finJuego:
		"""Se crea una condicion que tiene como argumento la funcion empezar, la cual le pregunta al usuario si desea reiniciar el juego."""
		if empezar():#Si se cumple que el usuario quiere volver a jugar, se reinician las variables nuevamente vacias y finJuego como False
			# os.system("cls")	
			letraIncorrecta = ""
			letraCorrecta = ""
			finJuego = False
			palabraSecreta = buscarPalabraAleat(palabras)#Se vueve a iniciar el programa llamando la funcion
		else:
				
			break#Se termina el ciclo While con el break

def normalize(s):
	replacements = (
		("á", "a"),
		("é", "e"),
		("í", "i"),
		("ó", "o"),
		("ú", "u"),
	)
	for a, b in replacements:
		s = s.replace(a, b).replace(a.upper(), b.upper())
	return s
def apa():
	seleccion = input("Seleccione que quiere ingresar escribiendo una de las siguientes opciones: \n info: para informacion \n libros: para Libros y otras monografias \n capitulos: para Capítulo de libro\n revista: para articulos de revista\n informe: para Informe técnico y de investigación\n webs: para Páginas y sitios web\n redes: para Redes sociales\n legislacion: para Legislación                           \n\n Escriba su opcion: ")



	if seleccion == "info":
		print('Dos o mas trabajos en un mismo paréntesis: \n Cuando dentro de un mismo paréntesis queremos citar varios trabajos, se ordenan cronológicamente si son documentos de un mismo autor. Se cita una vez el apellido del autor y para cada trabajo citado sólo indicamos el año. Los trabajos sin fecha se ordenarían los primeros y los artículos "en prensa" al final. Si son autores distintos, se ordenan alfabéticamente separados por punto y coma \n')
		print('Autor corporativo: Cuando citamos nombres de grupos que actúan como autores (instituciones, asociaciones, corporaciones, etc.), puede ocurrir que tengan una abreviatura comúnmente conocida. No es obligatorio utilizar su forma abreviada pero podemos emplearla si con ello evitamos repeticiones engorrosas a lo largo de nuestro texto. La primera vez que lo citemos en el texto, escribiremos su nombre completo seguido de su abreviatura. En trabajos que tengan tres o más autores corporativos, incluiremos en la cita el nombre del primero seguido de "et al."\n')
		print('')
		print('')
		var = input("Para usar otra funcion escriba siguiente: ")
		if(str(var) == "siguiente"):
			apa()
		else:
			exit()


	elif(normalize(seleccion) == "libros"):
		apellido = input("Escriba el apeliido: ")
		nombre = input("N. del autor: ")
		año = input("año: ")
		titulo = input("Título del libro: ")
		edicion = input("Numero de edicion o subtitulo: ")
		editorial = input("Editorial o fuente: ")
		print("")
		print("Resultado:")
		print(str(apellido) + ", " + nombre + ". " + "(" + str(año) + "). " +  str(titulo) + ": " + str(edicion) + ". " + str(editorial))
		print("")
		var = input("Para usar otra funcion escriba siguiente: ")
		if(str(var) == "siguiente"):
			apa()
		else:
			exit()

	elif(normalize(seleccion) == "capitulos"):
		apellido = input("Escriba el apeliido: ")
		fl = input("N. del autor del capítulo: ")
		año = input("año: ")
		titulocap = input("Título del capítulo: ")
		subtitulo = input("Subittulo del capítulo: ")
		cooredit = input("En N. Apellido del coordinador/editor del libro (Coord./ Ed./Eds.): ")
		titulolib = input("Título del libro: ")
		subtitlib = input("Subtítulo: ")
		volumen = input("Numero de editorial, volumen, primera pagina y ultima pagina: ")
		editorial = input("Editorial: ")
		print("")
		print("Resultado:")
		print(str(apellido) + ", " + str(fl) + ". (" + str(año) + "). " + str(titulocap) + ". " + str(subtitulo) + ". " + str(cooredit) + ", " + str(titulolib) + ": " + str(subtitlib) + "(" + str(volumen) + ")" + str(editorial) + ".")
		print("")
		var = input("Para usar otra funcion escriba siguiente: ")
		if(str(var) == "siguiente"):
			apa()
		else:
			exit()

	elif(normalize(seleccion) == "revista"):
		apellido = input("Escriba el apeliido: ")
		nombre = input("N. del autor: ")
		año = input("año: ")
		tituloa = input("Título del articulo: ")
		subtita = input("Subtitulo del articulo: ")
		titulor = input("Titulo completo de la revista: ")
		subtitr = input("Subitutulo de la revista: ")
		nvol = input("Numero de volumen: ")
		nfas = input("Numero de facículo: ")
		pag = input("Primera pagina - ultima pagina del articulo: ")
		print("")
		print("Resultado:")
		print(str(apellido) + ", " + nombre + ". " + "(" + str(año) + "). " +  str(tituloa) + ": " + str(subtita) + ". " + str(titulor) + ": " + str(subtitr) + ", " + str(nvol) + "(" + str(nfas) + "), " + str(pag))
		print("")
		var = input("Para usar otra funcion escriba siguiente: ")
		if(str(var) == "siguiente"):
			apa()
		else:
			exit()

	elif(normalize(seleccion) == "informe"):
		apellido = input("Escriba el apeliido: ")
		nombre = input("N. del autor: ")
		año = input("año: ")
		titulo = input("Título del informe: ")
		ninf = input("Numero del informe: ")
		agencia = input("Organizmo o agencia editora: ")
		print("")
		print("Resultado:")
		print(str(apellido) + ", " + nombre + ". " + "(" + str(año) + "). " +  str(titulo) + "(" + str(ninf) + "). " + str(agencia))
		print("")
		var = input("Para usar otra funcion escriba siguiente: ")
		if(str(var) == "siguiente"):
			apa()
		else:
			exit()

	elif(normalize(seleccion) == "webs"):
		nombre = input("Escriba el nombre completo del autor: ")
		act = input("Fecha de la ultima actualizacion: ")
		titulo = input("Título del trabajo: ")
		subt = input("Subtitulo: ")
		web = input("Nombre del sitio web: ")
		link = input("Enlace al sitio web: ")
		print("")
		print("Resultado:")
		print(str(nombre) + ". " + "(" + str(act) + "). " +  str(titulo) + ": " + str(subt) + ". " + str(web) + ". " + str(link))
		print("")
		var = input("Para usar otra funcion escriba siguiente: ")
		if(str(var) == "siguiente"):
			apa()
		else:
			exit()

	elif(normalize(seleccion) == "redes"):
		autor = input("Escriba el nombre del autor: ")
		arroba = input("Nombre de usuario: ")
		año = input("Escriba el año: ")
		post = input("Contenido de la publicacion (maximo 20 plabras): ")
		web = input("Nombre del sitio web: ")
		link = input("Enlace al sitio web: ")
		print("")
		print("Resultado:")
		print(str(autor) + "[" + arroba + "]. " + "(" + str(año) + "). " +  str(post) + ". " + str(web) + ". " + str(link))
		print("")
		var = input("Para usar otra funcion escriba siguiente: ")
		if(str(var) == "siguiente"):
			apa()
		else:
			exit()

	elif(normalize(seleccion) == "legislacion"):
		titulo = input("Escriba el Titulo de la ley: ")
		año = input("año: ")
		pub = input("Nombre de la publicacion oficial: ")
		num = input("Numero de la publicacion oficial: ")
		sec = input("Seccion de la publicacion: ")
		fec = input("Fecha de la publicacion: ")
		pag = input("Pagina inicial - pagina final: ")
		link = input("Enlace a la ley: ")
		print("")
		print("Resultado:")
		print(str(titulo) + ". (" + str(año) + "). " + str(pub) + ", " + str(num) + ", " + str(sec) + ", " + str(fec) + ", " + str(pag) + ". " + str(link))
		print("")
		var = input("Para usar otra funcion escriba siguiente: ")
		if(str(var) == "siguiente"):
			apa()
		else:
			exit()

	else:
		print("\n\nSu busqueda no coincidio con ninguna de las opciones vuelva a intentarlo\n")

apa()
'''def func(a,b):
    a=a+2.0
    b.append('1')
    print(a , b) 

#func(2,3)
#func(2,'3')
func(2,[2])
func(2,[])
'''

'''Funciones (def) 

 Una función es un bloque de código que tiene asociado un nombre, 
de manera que cada vez que se quiera ejecutar el bloque de código basta con invocar el nombre de la función.
Para declarar una función se utiliza la siguiente sintaxis:

    def <nombre-funcion> (<parámetros>):
        bloque código
        return <objeto>
---------------------------------------------------------------------------

Parámetros de una función
Una función puede recibir valores cuando se invoca a través de unas variables conocidas
como parámetros que se definen entre paréntesis en la declaración de la función. En el cuerpo de la función se pueden usar estos
parámetros como si fuesen variables
 '''




def bienvenidos(nombre):
        print('¡Bienvenido a Python', nombre + '!')
        return

bienvenidos("Alumnos")


'''
  Argumentos de la llamada a una función
Los valores que se pasan a la función en una llamada o invocación concreta de ella se 
conocen como argumentos y se asocian a los parámetros de la declaración de la función.
Los argumentos se pueden indicar de dos formas:

• Argumentos posicionales: Se asocian a los parámetros de la función en el mismo orden que aparecen
en la definición de la función.

• Argumentos por nombre: Se indica explícitamente el nombre del parámetro al que se asocia un argu‑
mento de la forma parametro = argumento
'''

def bienvenidos1(nombre,apellido):
        print('¡Bienvenido a Python', nombre ,apellido + '!')
        return

bienvenidos1("Sebastian","herrera")

'''
Retorno de una función
Una función puede devolver un objeto de cualquier tipo tras su invocación. 
Para ello el objeto a devolver debe escribirse detrás de la palabra reservada return. 
Si no se indica ningún objeto, la función no devolverá nada. '''

def area_triangulo(base, altura):
    area=base * altura / 2
    return area

area=area_triangulo(2,3)
print(area)
print(type(area))

'''
Puede devolver mas de un valor 
'''

def rectangulo(base,altura):
       area=base*altura
       perimetro=2*base+2*altura
       return area,perimetro
       

a,p=rectangulo(2,2) 
print("el area es :",a)
print("el perimetro es:",p)    

'''
Pasar un número indeterminado de argumentos
Es posible pasar un número variable de argumentos a un parámetro. Esto se puede hacer de dos
formas:
    • *parametro: Se antepone un asterisco al nombre del parámetro y en la invocación de la función se
pasa el número variable de argumentos separados por comas. Los argumentos se guardan en una lista
que se asocia al parámetro.
• **parametro: Se anteponen dos asteriscos al nombre del parámetro y en la invocación de la función
se pasa el número variable de argumentos por pares nombre = valor, separados por comas. Los
argumentos se guardan en un diccionario que se asocia al parámetro.
'''
'''
def menu(*platos):
    print('Hoy tenemos: ', end=' ')
    for plato in platos:
          print(plato, end=', ')

menu('pasta', 'pizza', 'ensalada')
'''
print(' ')
'''
Otra manera de hacerlo seria con listas o tuplas 
'''
def menu1(comidas):
      print('Hoy tenemos:')
      for plato in comidas:
            print(plato)
            

comidas=['pasta','pizza','ensalada']      
menu1(comidas)
print(type(comidas))

'''
Ámbito de los parámetros y variables de una función

Los parámetros y las variables declaradas dentro de una función son de ámbito local, 
mientras que las definidas fuera de ella son de ámbito ámbito global.

Tanto los parámetros como las variables del ámbito local de una función sólo están 
accesibles durante la ejecución de la función, es decir, cuando termina la ejecución 
de la función estas variables desaparecen y no son accesibles desde fuera de la función
'''


def bienvenida(nombre):
    lenguaje='Python'
    print('¡Bienvenido a', lenguaje, nombre + '!')
          
#bienvenida("Sebastian")

#print(lenguaje)   #Me tira un erros porque lenguaje solo existe entro de la funcion 

'''por ejemplo :

'''

lenguaje='java'
bienvenida("sebastian")
print(lenguaje) 


'''
   Paso de argumentos por referencia
En Python el paso de argumentos a una función es siempre por referencia, es decir, se pasa una 
referencia al objeto del argumento, de manera que cualquier cambio que se haga dentro de la 
función mediante el parámetro asociado afectará al objeto original, siempre y cuando este sea mutable.
'''

primer_curso = ['Matemáticas', 'Física'] #Una lista es mutable 
print(primer_curso)

def añade_asignatura(curso, asignatura):
      '''Funcion que me añade una asignatura'''
      curso.append(asignatura)
      #return


añade_asignatura(primer_curso, 'Química')
print(primer_curso)

#help(añade_asignatura)

'''que pasa si paso un tupla ?'''
'''

otro_curso=('lengua', 'geografia ')
añade_asignatura(otro_curso, 'civica')
print(otro_curso)
'''

'''
 !5=5*4*3*2*1=120
 !3=3*2*1=6
 El factorial de un numero negativo no existe
 el factorial de 0 es igual a 1
'''
''' Ejemplo de una funcion factorial '''
def factorial(numero):
              if numero<0:
                    print("No existe el factorial de un numero negativo")
              
              elif numero==0:
                    return 1
              
              else:
                    auxfact=1
                    while(numero>1):
                           auxfact=auxfact*numero 
                           numero=numero-1
                    return auxfact

fact=factorial(3)
print(factorial(3))
print(factorial(5))

'''Factorial usando recursividad '''

def factorialRe(numero):
       if numero<0:
            print("No existe el factorial de un numero negativo")
       elif numero==0:
                    return 1
       else:
            return numero * factorialRe(numero-1)


print(factorialRe(3))
print(factorialRe(10))

'''Ojo con la recursividad consume mucha memoria '''


'''Programación funcional
En Python las funciones son objetos de primera clase, es decir, que pueden pasarse como argumentos 
de una función, al igual que el resto de los tipos de datos.'''

def aplica(funcion, argumento):
    return funcion(argumento)

def cuadrado(numero):
       return numero*numero

def cubo(numero):
       return numero**3

print(aplica(cuadrado, 5))

print(aplica(cubo, 5))


''' Aplicar una función a todos los elementos de una colección iterable (map)

map(f,c) : Devuelve una objeto iterable con los resultados de aplicar la función f a los 
elementos de la colección c. Si la función f requiere n argumentos entonces deben pasarse n 
colecciones con los argumentos.Para convertir el objeto en una lista, tupla o diccionario hay que aplicar 
explícitamente las funciones list(), tuple() o dic() respectivamente.'''

a=tuple(map(cuadrado, [1, 2, 3]))
print(a)
print(type(a))


''' Funciones anónimas (lambda)
Existe un tipo especial de funciones que no tienen nombre asociado y se conocen como funciones
anónimas o funciones lambda.
La sintaxis para definir una función anónima es:
          
        lambda <parámetros> : <expresión>
Estas funciones se suelen asociar a una variable o parámetro desde la que hacer la llamada'''

area1 = lambda base, altura : base * altura


print(area1(10,10))








              

              
















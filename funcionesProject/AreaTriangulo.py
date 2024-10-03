# Ejemplo para calcular el area del triangulo

# Variables de entrada
base = int(input("Ingrese la base: "))
altura = int(input("Ingrese la altura: "))

# Proceso
def calcularAreaTriangulo(b,a):
    area = (b*a/2)
    return area

# Invocar la funcion
resultado = calcularAreaTriangulo(base,altura)
print("El area del triangulo es: ",resultado)

#Salida
print(f"El angulo cuya base {base} y altura {altura} es {resultado}")

# Funcion con argumentos predeterminados
def my_function(country = "Colombia"):
    print("I am from " +country)

# Invocar la funcion
my_function()
my_function("Sweden")

# Carros
def mostrarCarros(csrro1, carro2, carro3):
    print("El carro es: " +carro2)

mostrarCarros(csrro1= "BMW", carro3= "ferrari", carro2= "ford" )

# Kwargs
def mostrarCliente(**kwargs):
    print("Su apellido es: " +kwargs["apellido"])

mostrarCliente(nombre = "Tobias", apellido = "Refsnes")

# Pass
def miFuncion():
    pass

# Funciones integradas
x = min(5, 10, 25)
y = max(5, 10, 25)

print(x)
print(y)

num1 = pow(7, 4)

print(num1)

# Math
import math

num2 = math.sqrt(34)

print(num2)

# Ceil, Floor
import math

num3 = math.ceil(7.8)
num4 = math.floor(7.8)

print(num3) # returns 8
print(num4) # returns 7


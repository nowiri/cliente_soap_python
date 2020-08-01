'''
CLIENTE SOAP
requirements: zeep (pip install zeep)

Debe tener proyecto javalin-demo corriendo para probar
https://github.com/vacax/javalin-demo

'''
from zeep import Client 
import json

class Estudiante:
  def __init__(self, nombre, matricula, carrera):
    self.nombre = nombre
    self.matricula = matricula
    self.carrera = carrera

#Source
url = "http://localhost:7000/ws/EstudianteWebServices?wsdl"
#Creating client
client = Client(url)

#LISTANDO TODOS LOS ESTUDIANTES
print("-------------------------------------------------")
print("Consultando todos los estudiantes disponibles:")
lista_estudiantes = client.service.getListaEstudiante();

for e in lista_estudiantes:
	print("Nombre: "+e.nombre+". Matricula: "+str(e.matricula));


#CONSULTAR ESTUDIANTE
print("-------------------------------------------------")
matricula = 20160277;
print("Consultando estudiante con matricula: "+str(matricula))

estudiante = client.service.getEstudiante(matricula)

try:
	print("Estudiante encontrado: Nombre: "+estudiante.nombre+". Matricula: "+str(estudiante.matricula))
except Exception as e:
	print("Estudiante no encontrado . . .")

#CREAR NUEVO ESTUDIANTE
print("-------------------------------------------------")
print("Creando estudiante con matricula: 20160277")

#PARA QUE LO ACEPTE SE DEBE PASAR A JSON Y PARSEARLO ANTES DE MANDAR,
#SUPONGO QUE DEBER SER ALGO DEL FORMATO DE LA CLASE
estudiante = Estudiante("Jesus Rosario", "20160277", "ITT")
aux = json.dumps(estudiante.__dict__)
client.service.crearEstudiante(json.loads(str(aux)))
print("Creado con exito!")
print("-------------------------------------------------")

#CONSULTAR ESTUDIANTE DE NUEVO
print("-------------------------------------------------")
matricula = 20160277;
print("Volviendo a consultar estudiante con matricula: "+str(matricula))

try:
	print("Estudiante encontrado: Nombre: "+estudiante.nombre+". Matricula: "+str(estudiante.matricula))
except Exception as e:
	print("Estudiante no encontrado . . .")

print("-------------------------------------------------")

#BORRAR ESTUDIANTE

matricula = 20160277;
print("Borrando estudiante con matricula: "+str(matricula))


try:
	#OJO - EL WEBSERVICE NO ESTA CREADO EN EL PROYECTO
	estudiante = client.service.borrarEstudiante(matricula)
	print("Estudiante borrado con exito!.")
except Exception as e:
	print(e)

print("-------------------------------------------------")





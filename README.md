
# Tipos de pruebas 

-Pruebas manuales
-Pruebas unitarias 
-Pruebas de Integracion
 pruebas de que todos los componentes juntos funcionan

# Instalacion del entorno virtual
python3 -m venv venv 

# Activar el entorno virtual
source venv/bin/activate 


# Instalacion y Configuracion del entorno de Pruebas

libreria que permite detener la ejecucion del programa
y poder revisar las variables 

pip3 install ipdb

python3 -m unittest discover -s tests

modo verbose 
python3 -m unittest discover -v -s tests

# Uso de TearDown para limpiar data en UnitTest

Se añadira un archivo log para que registre
por cada transaccion que se realice en la 
clase BankAccount , y mediante pruebas 
unitarias se verificara que se escriba en el log







# Articulos de interes

https://www.youtube.com/watch?v=cSn7Ut4lysY

 

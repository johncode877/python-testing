
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


# Suites

Para organizar mejor nuestro conjunto de pruebas
utilizamos suites. Esta se crea de forma automatica
cuando usamos el comando discover al lanzar 
nuestras pruebas por consola 

python3 -m unittest discover -v -s tests

Especifica la variable PYTHONPATH para poder ejecutar
las pruebas definidas en la suite

PYTHONPATH=. python3 tests/test_suites.py

Tambien podemos ejecutar una prueba especificas desde la terminal
python3 -m unittest tests.test_calculator.CalculatorTests.test_multiply

Para ejecutar todas las pruebas de la clase
python3 -m unittest tests.test_calculator.CalculatorTests



# Articulos de interes

https://www.youtube.com/watch?v=cSn7Ut4lysY

https://www.pythontutorial.net/python-unit-testing/python-unittest-skip-test/


 
 
 
 

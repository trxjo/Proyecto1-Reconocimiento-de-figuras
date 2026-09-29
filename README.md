# Proyecto 1. Reconocimiento de Figuras

## Integrantes 
- Aguilar Rosas Carlos
- Cortes Leon Luis Gustavo
- Trejo Garcia Ozkar Mauricio

## Academico
- **Materia:** Modelado y Programacion
- **Grupo:** 7078 
- **Profesor:** Jose de Jesus Galaviz Casas
- **Ayudante:** Brenda Ayala Flores
- **Ayudante de laboratorio:** Jose Eduardo Cruz Campos

## Objetivo
Desarrollar una solucion funcional que procese imagenes `.bmp` y sea capaz de:
1. Leer una imagen proporcionada dentro de la lista de 'dataset_figuras'
2. Detectar cada figura presente en la imagen
3. Determinar el color de cada figura
4. Convertir el color detectado en hexadecimal
5. Clasificar cada figura en una de las categorias definidas 

## Tecnologias utilizadas
El proyecto esta desarrollado en **Python** y usamos librerias de vision por computadora

Principales herramientas:
- Python 
- OpenCV
- NumPy
- Pathlib
- Github para la creacion de ramas

***OpenCV*** se utiliza para el procesamiento de las imagenes, y obtencion de caracteristas necesarias para realizar la clasificacion.
***NumPy*** se utilizo para guardar algunos datos en matrices para poder manipularlas
***Pathlib*** Se utilizo para trabajar con las rutas de los sistemas de archivos

## Requisitos
Se recomienda utilizar el ***entorno virtual*** Python en la ultima version 

### Iniciar entorno virtual en python
```bash
python -m venv .venv 
```

Activar el entorno virtual 
En Linux/macOS:
```bash
source .venv/bin/activate
```

En Windows
```bash
.venv\Scripts\activate
```

Despues instalamos las dependecias de `OpenCV` Y `NumPy` con `pip`
```bash
pip install opcencv-python numpy
```

## Instalar el proyecto
Clonar el repositorio 

```bash
git clone https://github.com/trxjo/Proyecto1-Reconocimiento-de-figuras.git
cd Proyecto1-Reconocimiento-de-figuras
```

Se ejecuta
```bash 
python main.py
```

## Clasificacion de las figuras 
| Categoria | Figuras |
|  ---      |   ---   |
| `C` Cuadrilateros| Cuadrados, rectangulos, rombos y trapezoides |
| `T` Triangulos | Equilateros, isoceles, escalenos y rectangulos |
| `O` Circulos | Circulos|
| `X`| Otras figuras |

## Entrada 
El programa recibe la ruta de una imagen `.bmp` que puede contener una o mas figuras geometricas 
Cada imagen cumple con los requisitos solicitados 
- El fondo es de un solo color 
- Cada figura tiene un color solido 
- Los colores de las figuras son distintos entre si 
- Las figuras no se traslapan 
- El tamano, la posicion y la rotacion de las figuras puede variar

## Salida
Por cada figura detectada, el programa regresa
- Categoria de la figura(`C`, `T`, `O`, `X`)
- Colo de la figura en hexadecimal

## Manejo de errores
El programa te avisa cuando exista algun error
- La ruta de la imagen no existe 
- El archivo no puede abrirse 
- El archivo no tiene el formato esperado
- No se detectan figuras validas

**Universidad Nacional Autonoma de Mexico**
**Facultad de Ciencias**



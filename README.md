[![Open in MATLAB Online](https://www.mathworks.com/images/responsive/global/open-in-matlab-online.svg)](https://matlab.mathworks.com/)

# Práctica 2: Sistema cardiovascular

## Información del estudiante

Zulema Guadalupe Tirado Manzo [23210724]; l23210724@tijuana.tecnm.mx

Modelado de Sistemas Fisiológicos

Ingeniería Biomédica

## Docente

Dr. Paul Antonio Valle Trujillo; paul.valle@tectijuana.edu.mx

Departamento de Ingeniería Eléctrica y Electrónica, Tecnológico Nacional de México / Instituto Tecnológico de Tijuana, Blvd. Alberto Limón Padilla s/n, Tijuana, C.P. 22454, B.C., México.

## Descripción de la asignatura

Modelado de Sistemas Fisiológicos integra conceptos de Ingeniería de Control, Electrónica Analógica, Ciencias de la Computación y Fisiología para representar sistemas biológicos mediante modelos matemáticos y circuitos eléctricos equivalentes. A través de simulaciones *in silico*, se estudia su comportamiento dinámico y se diseñan estrategias de control.

## Objetivos

1. Identificar las variables y los parámetros hemodinámicos del modelo Windkessel de cuatro elementos.
2. Obtener las ecuaciones de estado y la función de transferencia del sistema cardiovascular.
3. Determinar el error en estado estacionario y analizar la estabilidad mediante los polos.
4. Simular los estados hipotenso, normotenso e hipertenso en MATLAB/Simulink y Simscape Electrical.
5. Comparar las respuestas en lazo abierto utilizando la misma señal aleatoria de entrada.
6. Diseñar y sintonizar dos controladores PID independientes para los casos hipotenso e hipertenso, tomando como referencia el estado normotenso.
7. Comparar las respuestas en lazo abierto y cerrado en MATLAB y Python.
8. Elaborar un diagrama biológico del sistema cardiovascular y documentar los resultados.

## Descripción detallada del sistema

La práctica utiliza el **modelo Windkessel de cuatro elementos**, que representa el comportamiento arterial mediante la impedancia característica **Z**, la inertancia **L**, la resistencia periférica **R** y la distensibilidad **C**. Es un sistema de segundo orden cuya entrada es la presión arterial $P_a(t)$ y cuya salida es la presión $P_p(t)$.

Se analizan tres condiciones cardiovasculares modificando únicamente la distensibilidad arterial:

| Parámetro | Hipotenso | Normotenso | Hipertenso |
|---|---:|---:|---:|
| Z | 0.010 | 0.010 | 0.010 |
| L | 0.001 | 0.001 | 0.001 |
| R | 1.000 | 1.000 | 1.000 |
| C | 3.500 | 1.500 | 1.000 |

La función de transferencia utilizada es:

$$
G(s)=\frac{P_p(s)}{P_a(s)}=\frac{LRs+RZ}{CLRZs^2+(LR+LZ)s+RZ}.
$$

Las simulaciones se realizan durante **15 s**, con una señal de excitación aleatoria común a los tres modelos. El estado normotenso se toma como referencia para ajustar dos controladores PID y comparar las respuestas antes y después del control. Los resultados se reproducen en MATLAB/Simulink y Python. Esta práctica es exclusivamente computacional y académica.

**Palabras clave:** Sistema cardiovascular; Windkessel; Controlador PID; Hipotensión; Hipertensión; MATLAB; Simulink; Python.

## Lista de archivos incluidos en el repositorio

1. Cuaderno computacional de MATLAB (`.mlx`).
2. Modelo de Simulink (`.slx`).
3. Código de Python (`.py`).
4. Señal de entrada utilizada en las simulaciones (`.xlsx`).
5. Imágenes y PDF de las simulaciones en lazo abierto(`.pdf`).
6. Capturas de las ganancias y la sintonización de ambos controladores PID.
7. Desarrollo matemático: ecuaciones de estado, funciones de transferencia, estabilidad y error en estado estacionario.
8. Diagrama biológico del sistema cardiovascular elaborado en BioRender.
9. Archivo `README.md` y archivo de citación `CITATION.cff`.

## Referencias

[1] P. A. Valle, *Syllabus para Modelado de Sistemas Fisiológicos*, Tecnológico Nacional de México / Instituto Tecnológico de Tijuana. Disponible en: https://biomath.xyz/course/

[2] M. C. Khoo, *Physiological Control Systems: Analysis, Simulation, and Estimation*, 2nd ed., IEEE Press, 2018.

[3] F. C. Hoppensteadt y C. S. Peskin, *Modeling and Simulation in Medicine and the Life Sciences*, Springer.

[4] J. E. Hall, *Guyton and Hall Textbook of Medical Physiology*, 14th ed., Elsevier, 2021.

[5] N. S. Nise, *Control Systems Engineering*, 8th ed., John Wiley & Sons, 2020.

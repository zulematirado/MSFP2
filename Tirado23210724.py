"""
Práctica 2: Sistema Cardiovascular

Departamento de Ingeniería Eléctrica y Electrónica, Ingeniería Biomédica
Tecnológico Nacional de México [TecNM - Tijuana]
Blvd. Alberto Limón Padilla s/n, C.P. 22454, Tijuana, B.C., México

Nombre del alumno: Zulema Guadalupe Tirado Manzo
Número de control: 23210724
Correo institucional: l23210724@tectijuana.edu.mx

Asignatura: Modelado de Sistemas Fisiológicos
Docente: Dr. Paul Antonio Valle Trujillo; paul.valle@tectijuana.edu.mx
"""
import control as ctrl
import numpy as np
import matplotlib.pyplot as plt
from scipy import signal
import pandas as pd

# Datos generales de la simulacion
x0 = 0
t0 = 0
tend = 15
dt = 1e-2
w = 10
h = 5
u = np.array(pd.read_excel('signal.xlsx', header=None))
u = u.flatten()
N = round((tend - t0) / dt) + 1
t = np.linspace(t0, tend, N)
u = signal.resample(u, len(t))

# Funcion del sistema cardiovascular
def cardio(Z, L, R, C):
    num = [L * R, R * Z]
    den = [C * L * R * Z, L * R + L * Z, R * Z]

    sys = ctrl.tf(num, den)

    polos = np.roots(den)

    return sys, polos

# Funcion de transferencia: Hipotenso
Z, L, R, C = 0.010, 0.001, 1.00, 3.500

syshipo, polos = cardio(Z, L, R, C)

print(f'Funcion de transferencia del hipotenso:\n{syshipo}')
print(f'Polos del sistema: L1 = {polos[0]:.3e}, L2 = {polos[1]:.3e}\n')

# Funcion de transferencia: Normotenso
Z, L, R, C = 0.010, 0.001, 1.00, 1.500

sysnormo, polos = cardio(Z, L, R, C)

print(f'Funcion de transferencia del normotenso:\n{sysnormo}')
print(f'Polos del sistema: L1 = {polos[0]:.3e}, L2 = {polos[1]:.3e}\n')

# Funcion de transferencia: Hipertenso
Z, L, R, C = 0.010, 0.001, 1.00, 1.000

syshiper, polos = cardio(Z, L, R, C)

print(f'Funcion de transferencia del hipertenso:\n{syshiper}')
print(f'Polos del sistema: L1 = {polos[0]:.3e}, L2 = {polos[1]:.3e}\n')

def controlador(kP, kI, kD, sys):

    Cr = 1E-6

    Re = 1 / (kI * Cr)
    Rr = kP * Re
    Ce = kD / Rr

    numPID = [
        Re * Rr * Ce * Cr,
        Re * Ce + Rr * Cr,
        1
    ]

    denPID = [
        Re * Cr,
        0
    ]

    PID = ctrl.tf(numPID, denPID)

    sysPID = ctrl.feedback(
        ctrl.series(PID, sys),
        1,
        sign=-1
    )

    return sysPID

hipoPID = controlador(
    458.438,
    1112094.736,
    0.00627,
    syshipo
)
print(
    f'Funcion de transferencia del hipotenso '
    f'en lazo cerrado:\n{hipoPID}\n'
)
hiperPID = controlador(
    126.595,
    293327.703,
    0.00140,
    syshiper
)
print(
    f'Funcion de transferencia del hipertenso '
    f'en lazo cerrado:\n{hiperPID}\n'
)

# Funcion de sistema en lazo abierto
def openloop(t, sys, u):

    _, y = ctrl.forced_response(
        sys,
        t,
        u,
        x0
    )

    return y

# Funcion de sistema en lazo cerrado
def closedloop(t, sys, u):

    _, y = ctrl.forced_response(
        sys,
        t,
        u,
        x0
    )

    return y

# Señal de entrada
Pa = u
# Respuestas en lazo abierto
PpL = openloop(t, syshipo, Pa)
PpN = openloop(t, sysnormo, Pa)
PpH = openloop(t, syshiper, Pa)
# Respuestas en lazo cerrado
PIDL = closedloop(t, hipoPID, Pa)
PIDH = closedloop(t, hiperPID, Pa)

clr1 = np.array([255,0,0])/255
clr2 = np.array([0,0,255])/255
clr3 = np.array([0,128,0])/255

def grafica(numero,y1,y2,y3,label1,label2,label3,archivo):
    fg = plt.figure(numero)
    fg.set_size_inches(w,h)
    plt.rcParams['font.size'] = 11
    plt.rcParams['font.family'] = 'serif'
    plt.rcParams['font.serif'] = ['Times New Roman']
    plt.plot(t,y1,'-',color=clr1,linewidth=0.3,label=label1)
    plt.plot(t,y2,'-',color=clr2,linewidth=0.3,label=label2)
    plt.plot(t,y3,'-',color=clr3,linewidth=0.3,label=label3)
    plt.xlim(0,15)
    plt.xticks(np.arange(0,16,1))
    plt.xlabel('t [s]')
    plt.ylabel('Vi(t) [V]')

    plt.legend(
        bbox_to_anchor=(0.5,-0.25),
        loc='upper center',
        ncol=3,
        frameon=False
    )

    fg.savefig(archivo,bbox_inches='tight')
    plt.show()

grafica(
    1,
    PpN,PpL,PpH,
    'Normotenso','Hipotenso','Hipertenso',
    'Lazo_abierto_python.pdf'
)
grafica(
    2,
    PpN,PpL,PIDL,
    'Normotenso','Hipotenso','PID Controlador',
    'Hipotenso_python.pdf'
)
grafica(
    3,
    PpN,PpH,PIDH,
    'Normotenso','Hipertenso','PID Controlador',
    'Hipertenso_python.pdf'
)
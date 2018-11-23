import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

tfinal = 20

dt = 0.1

Nbac = 20

M = 4

Ki = 18

Ka = 30000

Kr = 1

Kb = 1

A = -2.5

m0 = 1

N = 10 #cluster size


bacteria = pd.DataFrame(0, index = range(0,Nbac), columns = ['a', 'l', 'm', 'L', 'x', 'y', 'vx', 'vy'])

evolucao = pd.DataFrame(columns = ['t']+list(bacteria.columns))


bacteria['m'] = np.random.randint(0,M+1,Nbac)

def fm(m):
    return A*(m-m0)

def fL(t):
    if t<=10:
        return 0
    else:
        return 10
    
def a(fm, L):
    return np.exp(-N*fm)*(1 + L/Ka) / ((1 + L/Ka)**N + np.exp(-N*fm)*(1 + L/Ka)**N)
    
i = 0

def DinamicaInterna(t):
    L = fL(t)
    bacteria['L'] = L
    bacteria['a'] = a(bacteria.m,L)
    #print(t, "\n", bacteria.mean())
    
def DinamicaExterna(t):
    
    
for t in np.arange(0,tfinal,dt):
    DinamicaInterna(t)
    DinamicaExterna(t)
    evolucao.loc[i] = [t]+list(bacteria.mean(axis=0))
    i = i + 1
    
plt.plot(evolucao['t'], evolucao['a'])
plt.xlabel('Tempo (s)')
plt.ylabel('Atividade Média')
plt.show()

plt.plot(evolucao['t'], evolucao['m'])
plt.xlabel('Tempo (s)')
plt.ylabel('Metilização')
plt.show()

plt.plot(evolucao['t'], evolucao['L'])
plt.xlabel('Tempo (s)')
plt.ylabel('Concentração de Ligantes')
plt.show()

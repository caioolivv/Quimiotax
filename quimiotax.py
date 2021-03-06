import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

tfinal = 5

dt = 0.1

Nbac = 5

M = 4

Ki = 18

Ka = 30000

Kr = 1

Kb = 1

A = -2.5

m0 = 1

N = 1 #cluster size


bacteria = pd.DataFrame(0, index = range(0,Nbac), columns = ['a', 'l', 'm', 'L', 'x', 'y', 'vx', 'vy'])

#evolucao = pd.DataFrame(columns = ['t']+list(bacteria.columns))
evolucao = pd.DataFrame()

bacteria['m'] = np.random.rand(Nbac)*M

def fm(m):
    return A*(m-m0)

def fL(t):
    if t<=1000:
        return 0
    else:
        return 10
    
def a(m, L):
    efm = np.exp(-N*fm(m))*(1 + L/Ka)**N
    return 1 / (1 + (1 + L/Ki)**N/efm)

    
i = 0

def DinamicaInterna(dt):
    L = fL(t)
    bacteria['L'] = L
    bacteria['a'] = a(bacteria.m,L)
    dmdt = Kr - (Kr + Kb)*bacteria.a    
    bacteria['m'] += dmdt*dt
    bacteria.loc[bacteria.m >= M, 'm'] = M
    #print(t, "\n", bacteria.mean())
    
def DinamicaExterna(dt):
    pass
    
for t in np.arange(0,tfinal,dt):
    #print(t)
    DinamicaInterna(dt)
    DinamicaExterna(dt)
    #evolucao.loc[i] = [t]+list(bacteria.mean(axis=0))
    novalinha = bacteria.mean(axis=0)
    novalinha['t'] = t
    novalinha = novalinha.append(pd.Series(bacteria.m.values, 'm'+bacteria.index.astype(str)))
    novalinha = novalinha.append(pd.Series(bacteria.a.values, 'a'+bacteria.index.astype(str)))
    evolucao = evolucao.append(pd.DataFrame(novalinha).T)
    i = i + 1
    
plt.plot(evolucao['t'], evolucao['a'], 'o')
plt.plot(evolucao['t'], evolucao['m'], 'o')
plt.xlabel('Tempo (s)')
plt.ylabel('Atividade Média')
plt.show()

plt.plot(evolucao['t'], evolucao['m'], 'o')
plt.xlabel('Tempo (s)')
plt.ylabel('Metilização')
plt.show()

plt.plot(evolucao['t'], evolucao['L'], 'o')
plt.xlabel('Tempo (s)')
plt.ylabel('Concentração de Ligantes')
plt.show()

for m in np.char.array('m')+np.arange(Nbac).astype(str):
    #print(evolucao[m])
    plt.plot(evolucao['t'], evolucao[m])
plt.show()  

for a in np.char.array('a')+np.arange(Nbac).astype(str):
    plt.plot(evolucao.t, evolucao[a])
plt.show()

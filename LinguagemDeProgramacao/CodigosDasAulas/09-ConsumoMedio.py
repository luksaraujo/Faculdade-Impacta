distanciaPercorrida = int(input())
combustivelGasto = float(input())
consumoMedio = float(distanciaPercorrida / combustivelGasto)

print('{:.3f} km/l'.format(consumoMedio))

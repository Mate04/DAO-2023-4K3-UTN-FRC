from Class.Caja import Caja
from Class.Packing import Packing
from Class.Bidon import Bidon
from Class.Camion import Camion
from Class.Carga import Carga


def main():
    nt = Caja('comida',9)
    caja = Bidon('petroleo',76,8)
    packing = Packing('metales',10,10,20)
    bidon = Bidon('coca',7,2)
    mengo = Camion(780,'ABC321')
    mengo.subirCargar(nt)
    mengo.subirCargar(caja)
    mengo.subirCargar(bidon)
    mengo.subirCargar(packing)
    mengo.partir()
main()
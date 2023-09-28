from Class.Caja import Caja
from Class.Packing import Packing
from Class.Bidon import Bidon
from Class.Camion import Camion
from Class.Carga import Carga


def main():
    caja = Caja('sexo',8.8)
    packing = Packing('metales',10,10,20)
    bidon = Bidon('coca',7,2)
    mengo = Camion(133,'ABC321')
    mengo.subirCargar(bidon)
    mengo.subirCargar(packing)
main()
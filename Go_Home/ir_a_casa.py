import datetime
import time
from datetime import datetime
def hora():
    tiempo = datetime.now()
    print("Son las", tiempo.time().strftime("%H:%M:%S"))
    if tiempo.time().hour >= 7:
        print("Ya son mas de las 7, ve a casa")
    elif tiempo.time().hour < 7:
        print("Quedan",7 - tiempo.time().hour ,"horas para salir")
import threading
import time
import random

#Los semafotos
SantaSem = threading.Semaphore(0)#Santa semaforo
ReindeerSem = threading.Semaphore(0)#Remo semaforo
ElfSemH = threading.Semaphore(3)#Elfos piden ayuda (3) semaforo
ElfSem = threading.Semaphore(0)#Elfos ayudados

#Las variables
ReindeerCount = 0 # Variables para contabilizar el numero de renos que han llegado
ren = 0 # Variable que contabiliza el numero total de renos para implmentar el orden correcto de los prints
ElvesCount = 0 # Variable para contabilizar el numero de elfos que han llegado
elfs = 0 # Variable que contabiliza el trio de elfos en problemas
turn= 1 # Variables para contabilizar los turnos de preguntas

#Los constantes
Reindeer = 9 # Numero total de renos
Elves = 9 # Numero total de elfos
ElvesHelped = 3 #Numero de elfos ayudados
To_Wake_UP = 7 # Numero de veces que Santa se despierta
TO_HELP = 2 # Numero de veces que los elfos piden ayuda

ReindeerNames=["JUNIOR","GUINO","ROMARIO","FRANK","OBLITAS","MARIO","MARTIN","CRISTIAN","JUAN"]
ElfNames=["gasparin", "timoteo","rodolfo","pinocho","popeye","jesus","pancho","judas","miguel"]

# Definicion del proceso Santa: Santa duerme y le despertaran cuando hayan llegado 3 elfos o 9 renos.
# Si tres elfos piden ayuda, Santa los ayudará, liberará otros tres elfos que piden ayuda (ElfSemH.release())
# y despues liberara (ElfSem, release()) los tres elfos ayudados. Si los 9 renos despiertan a Santa, Santa prepara 
# el trineo y los liberara (ReindeerSem.release()). Santa se despertara 7 veces, 1 por los renos y 6 por los elfos.

def santa():
    global ReindeerCount
    global elfs
    global turn
    print("----- SANTA DICE: Estoy cansado")
    print("----- SANTA DICE: VOY A DORMIR")
    for i in range(To_Wake_UP):
        SantaSem.acquire() # Santa espera
        print("----- SANTA DICE: Estoy despierto HO HO HO")
        if elfs ==  ElvesHelped:
            elfs = 0
            print("----- SANTA DICE: ¿CUÁL ES EL PROBLEMA?")
            for i in range(ElvesHelped):
                print("----- SANTA AYUDA AL DUENDE {} DE 3".format(i + 1))
                ElfSemH.release() # desbloqueas para la llegada de 3 elfos mas
            print("----- SANTA TERMINA EL TURNO {}".format(turn))
            turn += 1
            for i in range(ElvesHelped):
                ElfSem.release()
        elif ReindeerCount == Reindeer: 
            ReindeerCount = 0
            preparesleigh()
            for i in range(Reindeer):
                ReindeerSem.release()

# Definicion del proceso reno: los renos van llegando y se van bloqueando (ReindeerSem.acquire()).
# Cuando llegan los 9 renos despiertan a Santa (SantaSem.release()).
# Despues Santa los prepara y los ata al trineo solo una vez, y los libera.

def reindeer():
    global ReindeerCount
    global ren
    num = ReindeerCount
    ReindeerCount += 1 
    print("      {} aqui!".format(ReindeerNames[num]))
    time.sleep(random.randint(5, 7))

    ren += 1
    if ren == 9:
        print("     Reno {} Soy el {}".format(ReindeerNames [num], ren))
        SantaSem.release() # Santa se despierta
    else:
        print("     Reno {} llega".format(ReindeerNames [num]))
    
    ReindeerSem.acquire()
    print("     {}Listo y enganchado". format(ReindeerNames [num]))
    print("     Reno {} termina".format(ReindeerNames [num]))

#Definicion del proceso elfo: come se puede apreciar los elfos van llegando y pediran ayuda dos veces cada uno. (TO_HELP=2) 
# #Una vez hayan llegado tres elfos, los siguientes que lleguen seran bloqueados (ElfSemH.acquire()) hasta que Santa los libere.
# Solo cuando tres elfos pidan ayuda Santa se despertara (SantaSem.release()).
# Los tres elfos que piden ayuda estarán bloqueados (ElfSem.acquire()) hasta que Santa los ayude y los libere.
# Cuando cada elfo haya sido ayudado dos veces acabaran.
def elf():
    global ElvesCount
    global elfs

    num = ElvesCount
    ElvesCount += 1
    print("hola soy elfo {}".format(ElfNames [num]))

    for i in range(TO_HELP):
        time.sleep(random.randint(1,5))
        ElfSemH.acquire() # dejara pasar 3 elfos
        elf = elfs + 1
        elfs += 1
        if elf < 3:
            print("Elfo {} dice: tengo una pregunta soy el {} esperando".format(ElfNames[num], elf))
        elif elf == ElvesHelped:
            print("Elfo {} dice: tengo una pregunta soy el {} SANTAAAA!".format(ElfNames[num], elf))
            SantaSem.release()
        ElfSem.acquire() 
        print("Elfo {} está siendo ayudado".format(ElfNames[num]))
    print("Elfo {} terminando".format(ElfNames [num]))
    
    # Santa preprara el trineo y se va a dormir
def preparesleigh():
    print("----- SANTA DICE: LOS JUGUETES ESTÁN LISTOS")
    print("----- SANTA CARGA LOS JUGUETES")
    print("----- SANTA DICE: HASTA LA PRÓXIMA NAVIDAD")
    print("----- SANTA DICE: VOY A DORMIR")

def main():
    # Array de hilos 
    threads = []
    # Santa
    s = threading.Thread(target=santa)
    threads.append(s)

    #Elfo
    for i in range(Elves):
        e = threading. Thread(target=elf) 
        threads.append(e)

    # Reno
    for i in range(Reindeer):
        r = threading.Thread (target=reindeer) 
        threads.append(r)
    
    # Iniciamos todos los hilos
    for t in threads:
        t.start()

    # Esperamos a que se completen todos los hilos 
    for t in threads:
        t.join()

    print("TERMINA LA NAVIDAD")
if __name__=="__main__":
    main()




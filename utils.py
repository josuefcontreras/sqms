import re
import csv
import Person
import Queue
from colorama import init
from termcolor import colored
from tabulate import tabulate

# use Colorama to make Termcolor work on Windows too
init()


def validateInput(regex, inputName, regexDesc):
    value = None

    while True:
        value = input(f'{inputName}:')
        if value == "mp":
            value = "0"
            break
        elif not re.match(regex, value):
            print(colored(f'❌❌❌ ERROR: >>>> {regexDesc}', "white", "on_red"))
        else:
            break

    return value


def showMenu():
    tableHeaders = ["OPCIONES", "DESCRIPCION"]
    tableData = [["a", "Agrega un elemento a la cola"], ["acvs", "Agrega elementos a la cola utilizando un archivo .csv"], ["c", "Muestra todos los elementos en la cola"], ["o", "Muestra las opciones."], [
        "r", "Reinicia la cola.\n(elimina elementos del queue y reinicia el siguiente turno  disponible a 1)"], ["s", "Muestra el siguiente en la cola."], ["v", "Vacía la cola.\n(Eliminina todos los elementos del queue, no reicicia el valor del siguiente turno  disponible)"], ["exit", "Termina el programa."]]
    print(tabulate(tableData, tableHeaders, tablefmt="grid"), "\n")


def collectInfo():
    print("Introduzca los datos de la persona o mp para volver al menû principal: ")
    name = validateInput(
        r"^([a-zA-Z]+[,.]?[ ]?|[a-zA-Z]+['-]?)+$", "Nombre", "Nombre inválido.")
    if name == "0":
        return "mp"
    idNumber = re.sub(r"\D", "", validateInput(
        r"^\d{3}[-\s]?\d{7}[-\s]?\d{1}$", "Cédula", "Su cédula debe contener 11 dígitos."))
    if idNumber == "0":
        return "mp"
    phoneNumber = re.sub(r"\D", "", validateInput(
        r"\(?(809|829|849)\)?[-\s]?\d{3}[-\s]?\d{4}$", "Teléfono", "Por favor, introduzca un numero telefonico de 10 digitos que empiece con 809, 829 u 849"))
    if phoneNumber == "0":
        return "mp"
    priority = validateInput(
        r"1|2", "Prioridad", "Por favor, introduzca un numero de prioridad: 1 (Alta) 2")
    if priority == "0":
        return "mp"

    return {"name": name, "idNumber": idNumber, "phoneNumber": phoneNumber, "priority": priority}


def confirmInput(action):
    confirmation = None
    while True:
        confirmation = input(f"⚠ ¿Desea {action}? (S / N) ").lower()
        if confirmation == "s" or confirmation == "n":
            break
    if confirmation == "s":
        confirmation = True
    else:
        confirmation = False
    return confirmation


def iniciar():
    print(
        colored(f"{'='*80} \n  Sistema de turnos iniciado. \n{'='*80}", "cyan"))

    queue = Queue.Queue()

    showMenu()

    while queue.open:
        choice = input(">>> ").lower()

        if choice == "a":
            info = collectInfo()
            if info == "mp":
                continue
            persona = Person.Person(**info)
            queue.add(persona)
            print(
                colored(f"✔✔✔ Agregada! \n Total en queue: {len(queue)}", "green"))
        elif choice == "acsv":
            filePath = input(
                'Introduzca la RUTA ABSOLUTA del archivo .csv o mp para volver al menû principal: ')
            if filePath == "mp":
                continue
            queue.addCsv(filePath)
        elif choice == "c":
            queue.show()
        elif choice == "o":
            showMenu()
            continue
        elif choice == "r":
            if confirmInput("reiniciar la cola"):
                queue.reset()
        elif choice == "s":
            queue.next()
        elif choice == "v":
            if confirmInput("vaciar la cola"):
                queue.empty()
        elif choice == "exit":
            if confirmInput("terminar el programa"):
                queue.open = False
        else:
            continue

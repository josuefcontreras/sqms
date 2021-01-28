import datetime
import Person
from termcolor import colored
from tabulate import tabulate


class Queue:
    def __init__(self):
        self.items = []
        self.nextAvailableTurn = 1
        self.open = True

    def __len__(self):
        return len(self.items)

    def add(self, item):
        item.turn = self.nextAvailableTurn
        item.arrivedAt = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        self.items = [*self.items, item]
        self.nextAvailableTurn += 1
        return len(self.items)

    def addCsv(self, filePath):
        length = 0
        try:
            peoplecsv = open(filePath)
            for index, line in enumerate(peoplecsv):
                if index == 0:
                    continue
                else:
                    [name, idNumber, phoneNumber] = line.replace(
                        "\"", "").split(",")
                    self.add(Person.Person(name, idNumber, phoneNumber))
                    length += 1
            print(colored(
                f'✔✔ {length} nuevos elementos agregados. \n Total en queue: {len(self)}.', "green"))
        except:
            peoplecsv = None
            print(colored(
                "Algo salió mal al cargar el archivo. Asegurese de introducir una RUTA ABSOLUTA", "white", "on_red"))
        finally:
            if peoplecsv is not None:
                peoplecsv.close()

    def next(self):
        if len(self.items) == 0:
            print(colored("No hay elementos en cola.", "yellow"))
        else:
            head = self.items[0]
            print("⏭ ", colored(f'Siguiente en fila', "cyan"))
            tableHeaders = ["Turno #", "Nombre",
                            "Cédula", "Teléfono", "Fecha de regístro"]
            tableData = [[head.turn, head.name, head.idNumber,
                          head.phoneNumber, head.arrivedAt]]
            print(tabulate(tableData, tableHeaders, tablefmt="grid"))
            print("\n")
            self.items = self.items[1:]

    def show(self):
        if len(self.items) == 0:
            print(colored("No hay elementos en cola.", "yellow"))
        else:
            print("=" * 50)
            print('📢📢 ', colored(f'{len(self.items)} en cola.', "cyan"))
            tableData = []
            tableHeaders = ["Turno #", "Nombre",
                            "Cédula", "Teléfono", "Fecha de regístro"]
            for item in self.items:
                tableData.append(
                    [item.turn, item.name, item.idNumber, item.phoneNumber, item.arrivedAt])

            print(tabulate(tableData, tableHeaders, tablefmt="grid"))
            print("\n")

    def empty(self):
        self.items = []

    def reset(self):
        self.items = []
        self.nextAvailableTurn = 1

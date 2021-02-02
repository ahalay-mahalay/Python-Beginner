# 4. Начните работу над проектом «Склад оргтехники».
# Создайте класс, описывающий склад.
# А также класс «Оргтехника», который будет базовым для классов-наследников.
# Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
# В базовом классе определить параметры, общие для приведенных типов.
# В классах-наследниках реализовать параметры, уникальные для каждого типа оргтехники.
#
# 5. Продолжить работу над первым заданием.
# Разработать методы, отвечающие за приём оргтехники на склад и
# передачу в определенное подразделение компании.
# Для хранения данных о наименовании и количестве единиц оргтехники,
# а также других данных, можно использовать любую подходящую структуру, например словарь.
#
# 6. Продолжить работу над вторым заданием.
# Реализуйте механизм валидации вводимых пользователем данных.
# Например, для указания количества принтеров, отправленных на склад,
# нельзя использовать строковый тип данных.

# Подсказка: постарайтесь по возможности реализовать в проекте «Склад оргтехники»
# максимум возможностей, изученных на уроках по ООП.
import json
from colorama import Fore, Style, init

init()


class Warehouse:
    __name__ = "Office Equipment Warehouse"

    def __init__(self, racks, length, height, width):
        self.racks = racks
        self.length = length
        self.height = height
        self.width = width
        self.capacity = length * height * width * racks
        self.goods = {}

    def __add__(self, other):
        if other.__name__ != self.__name__:
            try:
                self.goods.__getitem__(other.__name__)
            except KeyError:
                self.goods.__setitem__(other.__name__, {other.name: other.quantity})
                self.__setattr__("capacity", (self.capacity - other.size))
                return f"{Fore.LIGHTGREEN_EX}{Style.BRIGHT}+++{Style.RESET_ALL} New addition of {other.__name__}s:" \
                       f" '{other.name}' - {other.quantity}! {self.capacity} capacity left.\n" \
                       f"{json.dumps(self.goods, indent=4, sort_keys=True)}"
            else:
                try:
                    self.goods.__getitem__(other.__name__).__getitem__(other.name)
                except KeyError:
                    self.goods[other.__name__].__setitem__(other.name, other.quantity)
                    self.__setattr__("capacity", (self.capacity - other.size))
                    return f"{Fore.LIGHTGREEN_EX}{Style.BRIGHT}+++{Style.RESET_ALL} New addition of " \
                           f"{other.__name__}s: '{other.name}' - {other.quantity}! {self.capacity} capacity left.\n" \
                           f"{json.dumps(self.goods, indent=4, sort_keys=True)}"
                else:
                    self.goods[other.__name__][other.name] += other.quantity
                    self.__setattr__("capacity", (self.capacity - other.size))
                    return f"{Fore.LIGHTGREEN_EX}{Style.BRIGHT}+++{Style.RESET_ALL} Replenishment of " \
                           f"{other.__name__}s stock: '{other.name}' - {other.quantity}! {self.capacity} " \
                           f"capacity left.\n{json.dumps(self.goods, indent=4, sort_keys=True)}"
        else:
            return f"{Fore.LIGHTYELLOW_EX}{Style.BRIGHT}The Warehouse cannot be folded with itself.{Style.RESET_ALL}"

    def __sub__(self, other):
        if other.__name__ != self.__name__:
            try:
                self.goods.__getitem__(other.__name__).__getitem__(other.name)
            except KeyError:
                return f"{Fore.LIGHTYELLOW_EX}{Style.BRIGHT}!!!{Style.RESET_ALL} {other.__name__}s '{other.name}'" \
                       f" weren't delivered to the warehouse."
            else:
                if self.goods[other.__name__][other.name] == 0:
                    return f"{Fore.LIGHTYELLOW_EX}{Style.BRIGHT}!!!{Style.RESET_ALL} Sorry! We don't have any " \
                           f"{other.__name__}s '{other.name}' now!"
                elif self.goods[other.__name__][other.name] - other.quantity < 0:
                    return f"{Fore.LIGHTYELLOW_EX}{Style.BRIGHT}!!!{Style.RESET_ALL} Sorry! " \
                           f"You ask for {other.quantity} {other.__name__}s '{other.name}', " \
                           f"but we have only {self.goods[other.__name__][other.name]}"
                else:
                    self.__setattr__("capacity", (self.capacity + other.size))
                    self.goods[other.__name__][other.name] -= other.quantity
                    return f"{Fore.LIGHTRED_EX}{Style.BRIGHT}---{Style.RESET_ALL} Left the warehouse: " \
                           f"{other.__name__} '{other.name}' - {other.quantity}! {self.capacity} capacity left.\n" \
                           f"{json.dumps(self.goods, indent=4, sort_keys=True)}"
        else:
            return f"{Fore.LIGHTYELLOW_EX}{Style.BRIGHT}The Warehouse cannot be unfolded with itself.{Style.RESET_ALL}"


class OfficeEquipment:
    def __init__(self, name, length, height, width, quantity=1):
        self.name = name
        self.length = length
        self.height = height
        self.width = width
        self.quantity = quantity

    @property
    def size(self):
        size = self.length * self.height * self.width * self.quantity
        return size


class Printer(OfficeEquipment):
    __name__ = "Printer"

    @property
    def to_print(self):
        return f"{self.__name__} '{self.name}' is printing..."


class Scanner(OfficeEquipment):
    __name__ = "Scanner"

    @property
    def to_scan(self):
        return f"{self.__name__} '{self.name}' is scanning..."


class CopyMachine(OfficeEquipment):
    __name__ = "CopyMachine"

    @property
    def to_copy(self):
        return f"{self.__name__} '{self.name}' is copying..."


warehouse = Warehouse(10, 500, 200, 100)
printer = Printer("HP", 50, 30, 30)
scanner = Scanner("Canon", 40, 20, 30)
copy_machine = CopyMachine("Xerox", 50, 50, 40)
batch_of_printers_in = Printer("Canon", 50, 30, 30, 10)
batch_of_printers_out = Printer("Canon", 50, 30, 30, 11)
print(warehouse + warehouse)
print(warehouse - warehouse)
print(warehouse + printer)
print(warehouse + batch_of_printers_in)
print(warehouse - printer)
print(warehouse - printer)
print(warehouse - batch_of_printers_out)
print(warehouse - scanner)
print(warehouse + scanner)
print(warehouse + copy_machine)
print(warehouse - copy_machine)
print(warehouse - copy_machine)
print(warehouse + printer)
print(printer.to_print)
print(scanner.to_scan)
print(copy_machine.to_copy)

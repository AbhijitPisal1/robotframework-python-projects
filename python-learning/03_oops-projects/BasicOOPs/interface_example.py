# Interface:
# Defines a contract of methods that implementing classes must provide,
# usually via abstract base classes in Python for formal interface behavior.

from abc import ABC, abstractmethod

class Printable(ABC):
    @abstractmethod
    def print_data(self):
        pass

class Scannable(ABC):
    @abstractmethod
    def scan_data(self):
        pass

class MultiFunctionPrinter(Printable, Scannable):
    def print_data(self):
        print("Printing document")

    def scan_data(self):
        print("Scanning document")

mfp = MultiFunctionPrinter()
mfp.print_data()
mfp.scan_data()

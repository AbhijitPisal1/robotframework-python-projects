from abc import ABC, abstractmethod

class Document(ABC):
    @abstractmethod
    def open(self):
        pass

    @abstractmethod
    def save(self):
        pass

class WordDocument(Document):
    def open(self):
        print("Opening Word document.")

    def save(self):
        print("Saving Word document.")

class PDFDocument(Document):
    def open(self):
        print("Opening PDF document.")

    def save(self):
        print("Saving PDF document.")

# Usage
def handle_document(doc: Document):
    doc.open()
    doc.save()

handle_document(WordDocument())
handle_document(PDFDocument())

"""

Abstraction – "Expose only what’s necessary"

Abstraction means hiding the complex implementation and showing only the necessary features. For example, when editing a document, users just open or save — they don’t need to know how the data is processed under the hood.

You create abstract base classes with method declarations but no actual implementation. Subclasses must provide the actual behavior. This enforces a consistent interface across unrelated classes.

Abstraction helps define a template for families of classes and ensures consistency while still allowing flexibility in implementation.

"""
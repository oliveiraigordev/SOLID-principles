from abc import ABC, abstractmethod


# class Document(ABC):  # generic
#     # pdf, txt, excel
#     @abstractmethod
#     def load(self): pass

#     @abstractmethod
#     def view(self): pass

#     @abstractmethod
#     def format(self): pass

#     @abstractmethod
#     def calculate(self): pass


# class Pdf(Document):
#     def load(self):
#         print('load in pdf')

#     def view(self):
#         print('view informations')

#     def format(self):
#         print('no use')

#     def calculate(self):
#         print('no use')


# document1 = Pdf()
# document1.load()


class DocumentPdf(ABC):  # ISP
    @abstractmethod
    def load(self): pass

    @abstractmethod
    def view(self): pass


class DocumentTxt(ABC):  # ISP
    @abstractmethod
    def load(self): pass

    @abstractmethod
    def format(self): pass


class DocumentExcel(ABC):  # ISP
    @abstractmethod
    def load(self): pass

    @abstractmethod
    def calculate(self): pass

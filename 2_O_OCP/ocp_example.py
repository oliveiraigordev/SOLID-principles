from typing import Any


# class Company:
#     def do_work(self, worker: int) -> None:
#         if worker == 1:
#             print('Programmer creating code')
#         elif worker == 2:
#             print('Seller selling the product')
#         elif worker == 3:
#             print('Human Resources hiring new devs')
#         elif worker == 4:
#             print('Frontend raising bugs for production')
#         else:
#             print('Error, no Worker!')


class Programmer:
    def make(self):
        print('Programmer creating code')


class Seller:
    def make(self):
        print('Seller selling the product')


class HR:
    def make(self):
        print('Human Resources hiring new devs')


class Company:
    def do_work(self, worker: Any) -> None:
        worker.make()


company = Company()
programmer = Programmer()
seller = Seller()
hr = HR()
company.do_work(programmer)
company.do_work(seller)
company.do_work(hr)

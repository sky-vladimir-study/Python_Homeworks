from address import Address
from mailing import Mailing

to_address = Address("606000", "Нижний Новгород", "Пирогова", "18", "4")
from_address = Address("458985", "Москва", "Студенческая", "78", "35")

mailing = Mailing("9578458", from_address, to_address, 450)

print(mailing)

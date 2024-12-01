from smartphone import Smartphone

catalog = [
    Smartphone("Nokia", "3310", +79307854565),
    Smartphone("Iphone", "4", +79307854565),
    Smartphone("Motorola", "Razer v3", +79307858865),
    Smartphone("SonyEricsson", "7100", +79307457865),
    Smartphone("Sumsung", "s55", +79307458635)
]

for smartphone in catalog:
    print(f"{smartphone.marka} - {smartphone.model} - {smartphone.number}")

import qrcode
import pandas as pd
from termcolor import colored


def generate_qr(address, place):
    link = "https://www.google.com/maps/search/?api=1&query=" + address.replace(" ", "_") + "_" + place
    link.replace(",", "")
    qr = qrcode.QRCode()
    qr.add_data(link)
    qr.make(fit=True)
    img = qr.make_image()
    img.show()


class QRGenerator:
    def __init__(self, file_name):
        self.df = pd.read_excel(file_name, sheet_name="Sheet1")

    def get_address(self, name):
        if name in self.df["Ime"].values + " " + self.df["Priimek"].values:
            return self.df.loc[self.df["Ime"] + " " + self.df["Priimek"] == name,
            "Ulica in hišna številka"].iloc[0].split(",", 1)[0]

        else:
            return None


if __name__ == '__main__':
    qr_generator = QRGenerator("osebe.xlsx")
    kraj = input("Vnesite IME KRAJA kjer se nahajate: ")
    if kraj == "":
        print("Izbran je defaul: Ljubljana")
        kraj = "Ljubljana"
    else:
        print(f"Izbran je kraj {kraj}")

    while True:
        ime = input("Vnesite ime in priimek osebe: ")
        naslov = qr_generator.get_address(ime)
        if naslov and naslov != "exit":
            print("Naslov osebe je:", naslov)
            generate_qr(naslov, kraj)
        elif ime == "exit":
            print("Končujem program...")
            break
        else:
            print("Oseba ni bila najdena.")

    print("Program končan.")

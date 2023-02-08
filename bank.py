from konto import Konto

k = Konto()
k.wplata(3700)
print(k)
k.wyplata(2000)
print(k)
k.wyplata(9999)  # wypłata przekraczająca saldo
print(k)

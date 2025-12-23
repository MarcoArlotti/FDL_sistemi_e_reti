import math
import random

p = 2357
q = 2351
N = p*q

v = (p-1)*(q-1)


mcd = 1
while mcd == 1:
    chiave_privata = random.randint(1,999)
    mcd = math.gcd(chiave_privata,v) != 1

key_privata = (N,chiave_privata)

for chiave_pubblica in range(1,v):
    if(chiave_privata * chiave_pubblica) % v == 1:
        break
key_pubblica = (N,chiave_pubblica)

print(key_privata)
print(key_pubblica)

messaggio_non_criptografato = input("\nInseNci il messaggio (numero < N): ")

while True:
    try:
        messaggio_non_criptografato = int(messaggio_non_criptografato)
        if messaggio_non_criptografato < N:
          break
        messaggio_non_criptografato = input("Il numero intero deve essere minore di N: ")
    except:
        messaggio_non_criptografato = input("Il messaggio deve essere un numero intero: ")

cifrato = pow(messaggio_non_criptografato, key_pubblica[1], N)
print("\nMessaggio cifrato:", cifrato)

m_decifrato = pow(cifrato, key_privata[1], N)
print("Messaggio decifrato:", m_decifrato)
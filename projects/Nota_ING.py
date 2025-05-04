# Programa para calcular a nota de Ingles
"""
Critérios de avaliação:
Oralidade: 20%
Produção Oral: 25%
Compreenção Escrita: 35%
Produção Escrita: 20%
by DRAS
"""

Compreenção_Oral = float(input("Nota da Compreenção Oral: "))
if Compreenção_Oral > 20:
    Compreenção_Oral /= 10
print ((Compreenção_Oral * 0.2), "\n")

Produção_Oral = float(input("Nota da Produção Oral: "))
if Produção_Oral > 20:
    Produção_Oral /= 10
print((Produção_Oral * 0.25), "\n")

Compreenção_Escrita = float(input("Nota da Compreenção Escrita: "))
if Compreenção_Escrita > 20:
    Compreenção_Escrita /= 10
print ((Compreenção_Escrita * 0.35), "\n")

Produção_Escrita = float(input("Nota da Produção Escrita: "))
if Produção_Escrita > 20:
    Produção_Escrita /= 10
print (round(Produção_Escrita * 0.2), "\n")

Nota = ((Compreenção_Oral * 0.2) + (Produção_Oral * 0.25) + (Compreenção_Escrita * 0.35) + (Produção_Escrita * 0.2))

print (f"A tua nota final desta avaliação é {round(Nota, 2)} valores")
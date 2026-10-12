
import math

# Donnees du sujet
charge = [
    120, 80, 60, 50, 50, 70, 150, 300,
    520, 640, 700, 680, 600, 620, 650, 700,
    560, 400, 300, 250, 200, 180, 150, 130
]

CAP = 100
PRIX = 0.5

# 1. Simulation sans marge de securite
statique = math.ceil(max(charge) / CAP)
h_statique = statique * len(charge)
h_elastique = sum(math.ceil(c / CAP) for c in charge)

print("=== Simulation initiale ===")
print("Nombre de serveurs statiques :", statique)
print("Serveur-heures statique :", h_statique)
print("Serveur-heures elastique :", h_elastique)
print("Cout statique :", h_statique * PRIX, "EUR")
print("Cout elastique :", h_elastique * PRIX, "EUR")
print("Economie : {:.2f} %".format(
    100 * (1 - h_elastique / h_statique)
))

# 2. Simulation avec une marge de securite de 20 %
marge = 1.2
statique = math.ceil(max(charge) * marge / CAP)
h_statique = statique * len(charge)
h_elastique = sum(math.ceil(c * marge / CAP) for c in charge)

print("\n=== Simulation avec marge de 20 % ===")
print("Nombre de serveurs statiques :", statique)
print("Serveur-heures statique :", h_statique)
print("Serveur-heures elastique :", h_elastique)
print("Cout statique :", h_statique * PRIX, "EUR")
print("Cout elastique :", h_elastique * PRIX, "EUR")
print("Economie : {:.2f} %".format(
    100 * (1 - h_elastique / h_statique)
))
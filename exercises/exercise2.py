total_premium = 780000.00

# Percentagens para cada ganhador
porcentage_first = 0.46
porcentage_second = 0.32

# Cálculo dos prêmios para cada ganhador
premium_first = total_premium * porcentage_first
premium_second = total_premium * porcentage_second
premium_third = total_premium - premium_first - premium_second

# Exibição dos prêmios para cada ganhador
print("Prêmio do primeiro ganhador: R$", premium_first)
print("Prêmio do segundo ganhador: R$", premium_second)
print("Prêmio do terceiro ganhador: R$", premium_third)
# Formula de Calculo
# volume_base (ou volume_acido) = diferenca_ph * fator_base (ou fator_acido)

# Entrada de dados e definição de variaveis
ph_atual = float(input("Digite o pH atual da solução: "))

ph_limite_acido = 6.0
ph_limite_basico = 8.0
fator_base = 15.5
fator_acido = 12.0

# Caso 1: Solução Ácida (pH abaixo do limite ácido)
if ph_atual < ph_limite_acido:
    diferenca_ph = 7.0 - ph_atual
    volume_neutralizante = diferenca_ph * fator_base

    print(f"STATUS: ÁCIDO (pH {ph_atual:.2f}). Necessita de BASE.")
    print(f"Ação: Dosar {volume_neutralizante:.2f} Litros de agente neutralizante BÁSICO.")

# Caso 2: Solução Básica (pH acima do limite básico)
elif ph_atual > ph_limite_basico:
    diferenca_ph = ph_atual - 7.0
    volume_neutralizante = diferenca_ph * fator_acido

    print(f"STATUS: BÁSICO (pH {ph_atual:.2f}). Necessita de ÁCIDO.")
    print(f"Ação: Dosar {volume_neutralizante:.2f} Litros de agente neutralizante ÁCIDO.")

# Caso 3: pH na faixa aceitável
else:
    print(f"STATUS: ACEITÁVEL. O pH {ph_atual:.2f} está na faixa de tolerância.")
    print("Ação: Manter monitoramento. Nenhuma dosagem é necessária no momento.")
# Inicializando as listas (que funcionam como os vetores/arrays)
vet_pesos = []
vet_fretes = []

# Constante para definir o tamanho do lote
TOTAL_PACOTES = 10

print("=== SISTEMA ECOSORT - PROCESSAMENTO DE LOTE ===")

# Laço de repetição para processar os 10 pacotes
for i in range(TOTAL_PACOTES):
    print(f"\n--- Transação do Pacote {i + 1} ---")

    # 1. VALIDAÇÃO DO PESO (Simulando o "Do-While" com 'while True')
    while True:
        try:
            peso = float(input(f"Digite o peso do pacote {i + 1} (em kg): "))
            if peso > 0:
                break  # Dado correto, sai do laço de validação
            else:
                print("[ERRO] O peso não pode ser negativo ou zero. Tente novamente.")
        except ValueError:
            print("[ERRO] Entrada inválida. Por favor, digite um número.")

    # 2. VALIDAÇÃO DO DESTINO
    while True:
        destino = input("O destino é (N)acional ou (I)nternacional?: ").strip().upper()
        if destino in ['N', 'I']:
            break  # Destino correto, sai do laço
        else:
            print("[ERRO] Opção inválida. Digite apenas 'N' ou 'I'.")

    # Armazenando o peso validado na memória (Array de Pesos)
    vet_pesos.append(peso)

    # 3. ESTRUTURAS DE DECISÃO (Regras de Negócio para o Preço Base)
    if peso <= 2:
        frete_base = 10.00
    elif peso <= 10:
        frete_base = 20.00
    else:
        frete_base = 30.00

    # Aplicando a taxa de logística internacional (+20%), se aplicável
    if destino == 'I':
        frete_final = frete_base * 1.20
    else:
        frete_final = frete_base

    # Armazenando o frete calculado na memória (Array de Fretes)
    vet_fretes.append(frete_final)

# 4. CONSOLIDAÇÃO DOS DADOS (Fechamento do Lote)
# Usamos funções nativas do Python para somar os valores guardados nas listas
carga_total = sum(vet_pesos)
faturamento_bruto = sum(vet_fretes)
ticket_medio = faturamento_bruto / TOTAL_PACOTES

# 5. EXIBIÇÃO DO RELATÓRIO FINAL
print("\n========== RESULTADO FINAL ==========")
print(f"> Total de pacotes: {TOTAL_PACOTES}")
print(f"Carga total acumulada: {carga_total:.2f} kg")
print(f"Faturamento bruto do lote: R$ {faturamento_bruto:.2f}")
print(f"Ticket médio por pacote: R$ {ticket_medio:.2f}")
print("====================================")

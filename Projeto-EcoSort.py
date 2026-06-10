vet_pesos = []
vet_fretes = []

TOTAL_PACOTES = 10

print("=== SISTEMA ECOSORT - PROCESSAMENTO DE LOTE ===")

for i in range(TOTAL_PACOTES):
    print(f"\n--- Transação do Pacote {i + 1} ---")
while True:
        try:
            peso = float(input(f"Digite o peso do pacote {i + 1} (em kg): "))
            if peso > 0:
                break  # Dado correto, sai do laço de validação
            else:
                print("[ERRO] O peso não pode ser negativo ou zero. Tente novamente.")
        except ValueError:
            print("[ERRO] Entrada inválida. Por favor, digite um número.")

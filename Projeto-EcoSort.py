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
while True:
     destino = input("O destino é (N)acional ou (I)nternacional?: ").strip().upper()
     if destino in ['N', 'I']:
          break
     else:
         print("[ERRO] Opção inválida. Digite apenas 'N' ou 'I'.")

vet_pesos.append(peso)

if peso <= 2:
     frete_base = 10.00
elif peso <= 10:
     frete_base = 20.00
else:
     frete_base = 30.00
if destino == 'I':
     frete_final = frete_base * 1.20
else:
     frete_final = frete_base

vet_fretes.append(frete_final)

carga_total = sum(vet_pesos)
faturamento_bruto = sum(vet_fretes)
ticket_medio = faturamento_bruto / TOTAL_PACOTES


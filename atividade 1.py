'''Construa o algoritmo de um caixa de mercado. O programa deve funcionar num laço
infinito, apresentando um menu de produtos e solicitando ao usuário que digite o código do
produto desejado, regras e Fluxo:
1. Apresente o menu usando um único print: 1 - Banana (R$ 2.50) | 2 - Arroz (R$ 20.00) | 3 -
Feijão (R$ 8.50) | 0 - Finalizar Compra.
2. Use a estrutura match-case para adicionar o valor correto do produto a uma variável
acumuladora (o total do carrinho).
3. Se o usuário digitar um código inválido, exiba um aviso e pule para a próxima leitura do
laço (sem somar nada).
4. O laço só deve ser abortado quando o usuário digitar 0.
5. Após o laço, solicite ao usuário um "Código de Cupom" (texto).
6. Se a palavra "DESC" estiver dentro do cupom digitado (independente de
maiúsculas/minúsculas) E o total da compra for maior ou igual a R$ 50.00, aplique 15% de
desconto no total.
7. Use o Operador Ternário para decidir uma variável chamada frete: "Grátis" se a compra
for superior a R$ 100.00, ou "R$ 15.00" caso contrário.
8. Imprima o resumo: Total final da compra e o status do frete.'''
total_carrinho = 0
valor = 0
desconto = 0
while True:
    print("\nMenu de compras:\n1 - Banana (R$ 2.50)\n2 - Arroz (R$ 20.00)\n3 - Feijão (R$ 8.50)\n0 - Finalizar Compra.\n")
    choice = int(input("Escolha o produto: "))
    quantidade = int(input("Quantos produtos deseja comprar: "))
    match choice:
        case 1:
            valor = 2.50 * quantidade
            total_carrinho += valor
            print(f"{quantidade}x Banana(s) adicionada(as).")
        case 2:
            valor = 20 * quantidade
            total_carrinho += valor
            print(f"{quantidade}x Arroz adicionado(os).")
        case 3:
            valor = 8.50 * quantidade
            total_carrinho += valor
            print(f"{quantidade}x Feijão adicionado(os).")
        case 0:
            print("Finalizando carrinho...")
            break
        case _:
            print("Produto invalido!\n")
            continue
cupom = input("\nInforme o código do cupom (ou aperte ENTER para pular): ").lower()
if "desc" in cupom and total_carrinho > 50:
    print("Cupom Válido! Aplicado 15% de desconto.")
    desconto = total_carrinho * 0.15
frete = 'Grátis' if total_carrinho >= 100 else 15
total_carrinho -= desconto

print(f"[Resumo da compra]\nR$ {total_carrinho:.2f}\n"
      f"Frete: {frete}")
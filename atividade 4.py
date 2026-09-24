'''Crie um programa matemático desafiador que testa divisores e soma de valores baseados nas escolhas do usuário.
Regras e Fluxo:
1. Solicite ao usuário um número inteiro que seja o "limite" da busca (ex: 20).
2. Utilize um laço for para percorrer todos os números de 1 até o número que o usuário
digitou (incluindo ele).
3. Se o número que estiver sendo testado for múltiplo de 3 OU múltiplo de 5, some este
número em uma variável acumuladora. Se não for, ignore.
4. Após o final do laço, imprima o valor total que foi somado.
5. Agora, verifique se esse número somado final é um número "Primo" ou "Perfeito".
    a). Imprima "É par e não é perfeito" se for par. (Nota simplificada: em vez do algoritmo
    completo de perfeição/primo visto na lista anterior, faça apenas uma verificação de
    Paridade ou Ímpar para o resultado final nesta versão).
    b). Crie uma lógica final: Se o somatório total for maior que 100 E for Ímpar, imprima
    "Temos um Ímpar Mágico gigante!". Caso contrário, imprima "Número comum.".'''
limite = int(input("Digite um número que servirar como limitador: "))
contador = 0
for l in range(1, limite + 1):
    if l % 3 == 0 or l % 5 == 0:
        contador += l
        print(l)
    else:
        continue
print(f"A soma de todos os múltiplos de 3 ou 5 encontrados foi: {contador}")
if contador % 2 == 0:
    print("É par e não é perfeito")
else:
    if contador > 100:
        print("Temos um Ímpar Mágico gigante!")
    else:
        print("Número comum.")

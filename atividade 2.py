'''
Crie um sistema que permita ao usuário tentar criar uma senha segura, com um limite máximo de 4 tentativas.
Você deve obrigatoriamente usar um laço for com a função range() para controlar esse limite.
Regras de Validação:
1. A cada rodada do laço, peça para o usuário digitar uma senha.
2. A senha será considerada inválida se acontecer uma das duas coisas a seguir:
a). Tiver menos que 6 caracteres (use a função len()).
b). A palavra "admin" (em qualquer formato) ou a sequência "123" estiverem dentro da
senha.
3. Se a senha for inválida, exiba "Senha fraca! Tente novamente." e o laço deve continuar
normalmente para a próxima tentativa. Dica: Opcionalmente, você pode usar continue.
4. Se o usuário digitar uma senha forte, o programa deve exibir "Senha cadastrada com
sucesso!" e abortar o laço imediatamente (para não consumir as tentativas restantes).
5. Se o laço terminar e o usuário tiver gasto todas as suas 4 tentativas sem sucesso, exiba
"Conta bloqueada por excesso de tentativas falhas.".
'''
status = ""
tentativas = 4
for t in range(tentativas, 0, -1):
    senha = input("Diga sua senha: ")
    if len(senha) < 6 or ("admin" in senha or "123" in senha) :
        print("Senha fraca!Tente novamente.")
        print(f"Total de tentativas restantes: {t-1}\n")
        status = "Falha"
        continue
    else:
        print("\nSenha cadastrada com sucesso!")
        status = "Sucesso"
        break

if status == "Falha":
    print("Conta bloqueada por excesso de tentativas falhas.")
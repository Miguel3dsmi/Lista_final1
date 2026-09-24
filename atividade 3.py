'''O setor de Recursos Humanos precisa triar candidatos. O programa deve receber dados
continuamente até que uma condição de parada (sentinela) seja alcançada.
Regras e Fluxo:
1. O programa deve solicitar a Idade (inteiro) de um candidato. Se a idade digitada for menor
que 0, o programa deve abortar o laço imediatamente.
2. Em seguida, solicite o Sexo ('M' ou 'F') e os Anos de Experiência (inteiro).
3. Se o sexo for diferente de 'M' ou 'F', avise "Sexo inválido, ficha descartada" e pule para o
próximo candidato usando continue.
4. Regra de Aprovação: O candidato será somado a um "contador de aprovados" SE:
    a). For do sexo 'M' e tiver idade entre 25 e 40 anos (inclusive).
    b). OU for do sexo 'F' e tiver mais de 3 anos de experiência.
5. Some também todos os candidatos lidos com sucesso em um "contador de total de fichas".
6. Quando o laço acabar, calcule a porcentagem de candidatos aprovados em relação ao
total.
7. Para evitar erro matemático, antes de calcular a porcentagem, verifique com um if se
nenhuma ficha foi lida, avisando "Nenhum dado cadastrado.".'''
candidatos_ap, candidatos_rp = 0, 0
while True:
    idade = int(input("Digite sua idade (Digite 0  ou negativo para sair): "))
    if idade <= 0:
        break
    sexo = input("Qual seu sexo (M/F): ").upper()[0:1]
    if sexo != "M" and sexo != "F":
        print("Sexo inválido, ficha descartada.")
        continue
    experincia = int(input("Anos de experiência: "))
    if sexo == "M" and 25 <= idade <= 40:
        stts = "APROVADO"
        candidatos_ap += 1
    elif sexo == "F" and experincia > 3:
        stts = "APROVADO"
        candidatos_ap += 1
    else:
        stts = "REPROVADO"
        candidatos_rp += 1
    print(f"Candidato(a) {stts} na triagem\n")
candidatos_totais = candidatos_rp + candidatos_ap
porcentagem_aprovacao = ((candidatos_ap * 100)/candidatos_totais)
print(f"\n[Relatório final RH]\n"
      f"Total de fichas válidas: {candidatos_totais}\n"
      f"Aprovados: {candidatos_ap}\n"
      f"Percentual de Sucesso: {porcentagem_aprovacao:.2f}%")


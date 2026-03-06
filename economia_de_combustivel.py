import os

def limpar_tela():
  os.system("cls" if os.name == "nt" else "clear")


def calcular_minimo():

  print()
  print("=====[Vamos calcular o valor mínimo para compensar a ida ao posto mais barato]=====")
  print()

  consumo = float(input("Qual o consumo do seu veículo em km por litro? : ").replace(",", "."))
  print()

  gasolina_cara = float(input("Qual o valor da gasolina no posto caro? : ").replace(",", "."))
  print()

  gasolina_barata = float(input("Qual o valor da gasolina no posto barato? : ").replace(",", "."))
  print()

  distancia_barata = float(input("Quantos km você está do posto mais barato? : ").replace(",", "."))
  print()

  if consumo <= 0 or distancia_barata <= 0:
    print("Consumo ou distância inválidos.")
  else:

    if gasolina_cara <= gasolina_barata:
      print("O posto mais barato não é realmente mais barato.")

    else:

      diferenca_preco = gasolina_cara - gasolina_barata

      custo_km_cara = gasolina_cara / consumo
      custo_km_barata = gasolina_barata / consumo

      valor_pv = (custo_km_cara * distancia_barata) + (custo_km_barata * distancia_barata)
      valor_sv = custo_km_barata * (distancia_barata * 2)

      minimo_litros_pv = valor_pv / diferenca_preco
      minimo_litros_sv = valor_sv / diferenca_preco

      minimo_valor_pv = minimo_litros_pv * gasolina_barata
      minimo_valor_sv = minimo_litros_sv * gasolina_barata

      limpar_tela()

      print("=====[Se a gasolina do tanque NÃO for do posto barato]=====")
      print("Você precisa colocar no mínimo R$%.2f (%.2f litros)\n" % (minimo_valor_pv, minimo_litros_pv))

      print("=====[Se a gasolina do tanque JÁ for do posto barato]=====")
      print("Você precisa colocar no mínimo R$%.2f (%.2f litros)\n" % (minimo_valor_sv, minimo_litros_sv))


def calcular_compensa():

  print()
  print("=====[Vamos calcular se compensa abastecer]=====")
  print()

  qual_vez = input("A gasolina do tanque já é do posto barato? (sim/não): ").lower()
  print()

  valor_abastecer = float(input("Qual valor pretende abastecer? : ").replace(",", "."))
  print()

  consumo = float(input("Qual o consumo do veículo? : ").replace(",", "."))
  print()

  gasolina_cara = float(input("Valor da gasolina no posto caro? : ").replace(",", "."))
  print()

  gasolina_barata = float(input("Valor da gasolina no posto barato? : ").replace(",", "."))
  print()

  distancia_barata = float(input("Quantos km até o posto barato? : ").replace(",", "."))
  print()


  if consumo <= 0 or distancia_barata <= 0:
    print("Consumo ou distância inválidos.")

  else:

    if gasolina_cara <= gasolina_barata:
      print("O posto mais barato não é realmente mais barato.")

    else:

      diferenca_preco = gasolina_cara - gasolina_barata

      custo_km_cara = gasolina_cara / consumo
      custo_km_barata = gasolina_barata / consumo

      valor_pv = (custo_km_cara * distancia_barata) + (custo_km_barata * distancia_barata)
      valor_sv = custo_km_barata * (distancia_barata * 2)

      minimo_litros_pv = valor_pv / diferenca_preco
      minimo_litros_sv = valor_sv / diferenca_preco

      minimo_valor_pv = minimo_litros_pv * gasolina_barata
      minimo_valor_sv = minimo_litros_sv * gasolina_barata

      quanto_economizara_pv = ((valor_abastecer - minimo_valor_pv) / gasolina_barata) * diferenca_preco
      quanto_economizara_sv = ((valor_abastecer - minimo_valor_sv) / gasolina_barata) * diferenca_preco

      limpar_tela()

      if qual_vez == "sim":

        if valor_abastecer > minimo_valor_sv:
          print("Você fará economia.")
          print("Economia: R$%.2f" % quanto_economizara_sv)

        elif valor_abastecer < minimo_valor_sv:
          print("Não compensa abastecer esse valor.")

        else:
          print("Economia exata.")

      elif qual_vez == "nao" or qual_vez == "não":

        if valor_abastecer > minimo_valor_pv:
          print("Você fará economia.")
          print("Economia: R$%.2f" % quanto_economizara_pv)

        elif valor_abastecer < minimo_valor_pv:
          print("Não compensa abastecer esse valor.")

        else:
          print("Economia exata.")


def menu():

  limpar_tela()

  print("=====[Você quer saber]=====")
  print("1 - Valor mínimo para compensar ir ao posto barato")
  print("2 - Se o valor que pretende abastecer compensa\n")

  escolha = int(input("Escolha 1 ou 2: "))

  if escolha == 1:
    calcular_minimo()

  elif escolha == 2:
    calcular_compensa()

  else:
    print("Opção inválida.")


menu()

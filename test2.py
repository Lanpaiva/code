# n1 = int(input("send number:"))
# n2 = int(input("send another number:"))
# sum = n1 + n2

# print(n1, " + ", n2, "soma igual a", sum)


def valorPagamento(valor_prestacao, dias_atraso):
    # Verificar se há atraso
    if dias_atraso <= 0:
        return valor_prestacao
    else:
        # Calcular o valor com multa e juros
        multa = valor_prestacao * 0.03
        juros = valor_prestacao * 0.001 * dias_atraso
        valor_total = valor_prestacao + multa + juros
        return valor_total


def main():
    # Solicitar ao usuário o valor da prestação e o número de dias em atraso
    valor_prestacao = float(input("Digite o valor da prestação: "))
    dias_atraso = int(input("Digite o número de dias em atraso: "))

    # Calcular o valor a ser pago e exibir o resultado
    valor_a_pagar = valorPagamento(valor_prestacao, dias_atraso)
    print(f"O valor a ser pago é: R$ {valor_a_pagar:.2f}")


if __name__ == "__main__":
    main()

package main

import "fmt"

// func valorPagamento(valPrestacao float64, diasAtraso int) float64 {
// 	if diasAtraso <= 0 {
// 		return valPrestacao
// 	} else {
// 		multa := valPrestacao * 0.003
// 		juros := valPrestacao * 0.001 * float64(diasAtraso)
// 		valortotal := valPrestacao + multa + juros
// 		return valortotal
// 	}

// }

func main() {
	// var valPrestacao float64
	// var diasAtraso int

	// fmt.Print("Digite o valor da prestação: ")
	// fmt.Scan(&valPrestacao)

	// fmt.Print("Digite o número de dias em atraso: ")
	// fmt.Scan(&diasAtraso)

	// // Calcular o valor a ser pago e exibir o resultado
	// valor_a_pagar := valorPagamento(valPrestacao, diasAtraso)
	// fmt.Printf("O valor a ser pago é: R$ %.2f\n", valor_a_pagar)
	var qtde1 int
	fmt.Scan(&qtde1)
	count := qtde1 / 15
	fmt.Println(count)

}

package Exercícios;

import java.util.Scanner;

public class ex03 {

	public static void main(String[] args) {
		// Informar um saldo e imprimir o saldo com reajuste de 1%.

		double saldo, ajuste;

		Scanner sc = new Scanner(System.in);

		System.out.print("Insira o seu saldo: R$");
		saldo = sc.nextDouble();

		ajuste = saldo * 0.01;
		saldo = saldo - ajuste;

		System.out.println("O seu saldo com reajuste é igual a R$" + saldo);
	}

}

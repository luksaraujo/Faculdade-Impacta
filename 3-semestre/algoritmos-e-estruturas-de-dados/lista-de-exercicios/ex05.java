package Exercícios;

import java.util.Scanner;

public class ex05 {

	public static void main(String[] args) {

		/*
		 * Crie um algoritmo que leia o valor do salário mínimo e o valor do salário de
		 * um usuário, calcule a quantidade de salários mínimos esse usuário ganha e
		 * imprima o resultado. (1SM=R$788,00)
		 */

		Scanner sc = new Scanner(System.in);

		int salarioUser, totalSalarios;

		System.out.print("Insira seu salário: R$");
		salarioUser = sc.nextInt();

		totalSalarios = salarioUser / 788;

		System.out.println("Você ganha aproximadamente " + totalSalarios + " Salários mínimos");

	}

}

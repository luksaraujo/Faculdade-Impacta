package Exerc�cios;

import java.util.Scanner;

public class ex05 {

	public static void main(String[] args) {

		/*
		 * Crie um algoritmo que leia o valor do sal�rio m�nimo e o valor do sal�rio de
		 * um usu�rio, calcule a quantidade de sal�rios m�nimos esse usu�rio ganha e
		 * imprima o resultado. (1SM=R$788,00)
		 */

		Scanner sc = new Scanner(System.in);

		int salarioUser, totalSalarios;

		System.out.print("Insira seu sal�rio: R$");
		salarioUser = sc.nextInt();

		totalSalarios = salarioUser / 788;

		System.out.println("Voc� ganha aproximadamente " + totalSalarios + " Sal�rios m�nimos");

	}

}

package Exerc�cios;

import java.util.Scanner;

public class ex09 {

	public static void main(String[] args) {
		/*
		 * Escreva um programa que verifique a validade de uma senha fornecida pelo
		 * usu�rio. A senha v�lida � o n�mero 1234. Devem ser impressas as seguintes
		 * mensagens: ACESSO PERMITIDO caso a senha seja v�lida. ACESSO NEGADO caso a
		 * senha seja inv�lida
		 */

		Scanner sc = new Scanner(System.in);

		int senha;

		System.out.println("Por favor, insira a senha para acessar a conta");
		senha = sc.nextInt();

		if (senha == 1234) {
			System.out.println("ACESSO PERMITIDO");
		} else {
			System.out.println("ACESSO NEGADO");
		}
	}

}

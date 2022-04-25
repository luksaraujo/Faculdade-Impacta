package Exercícios;

import java.util.Scanner;

public class ex20 {

	public static void main(String[] args) {
		// Faça um programa que peça ao usuário um número entre 12 e 20. Se a pessoa
		// digitar um número diferente, mostrar a mensagem "entrada inválida" e
		// solicitar o número novamente. Se digitar correto mostrar o número digitado.

		Scanner sc = new Scanner(System.in);

		int n;

		System.out.println("Digite um valor entre 12 e 20!");
		n = sc.nextInt();

		while (n < 12 || n > 20) {
			System.out.println("entrada invalida!!");
			System.out.println();
			System.out.println("Digite um valor entre 12 e 20!");
			n = sc.nextInt();
		}
		System.out.println();
		System.out.println(n);

	}

}

package Exerc�cios;

import java.util.Scanner;

public class ex07 {

	public static void main(String[] args) {
		// Escreva um programa para ler 2 valores (considere que n�o ser�o informados
		// valores iguais) e escrever o maior deles.

		Scanner sc = new Scanner(System.in);

		int n1, n2;

		System.out.println("Insira dois valores");
		n1 = sc.nextInt();
		n2 = sc.nextInt();

		System.out.print("\n");

		if (n1 > n2) {
			System.out.println("O maior valor inserido � " + n1 + ".");
		}
		if (n2 > n1) {
			System.out.println("O maior valor inserido � " + n2 + ".");
		}

	}

}

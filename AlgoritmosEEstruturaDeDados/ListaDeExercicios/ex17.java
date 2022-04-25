package Exercícios;

import java.util.Scanner;

public class ex17 {

	public static void main(String[] args) {
		/*
		 * Escreva um programa que lê o tamanho do lado de um quadrado e imprime um
		 * quadrado daquele tamanho com asteriscos. Seu programa deve funcionar para
		 * quadrados com lados de todos os tamanhos entre 1 e 20. Para lado igual a 5:
		 *****
		 *****
		 *****
		 *****
		 *****
		 */

		Scanner sc = new Scanner(System.in);

		int lado;

		System.out.println("Insira o lado");
		lado = sc.nextInt();

		for (int i = lado; i > 0; i--) {
			for (int y = lado; y > 0; y--) {
				System.out.print(" * ");
			}
			System.out.println();
		}

	}

}

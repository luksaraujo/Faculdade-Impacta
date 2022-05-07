package Exercícios;

import java.util.Scanner;

public class ex11 {

	public static void main(String[] args) {
		// Escreva um programa para ler 3 valores inteiros (considere que não serão
		// lidos valores iguais) e escrevê-los em ordem crescente.
		Scanner sc = new Scanner(System.in);

		int n1, n2, n3;

		System.out.println("Insira 3 valores");
		n1 = sc.nextInt();
		n2 = sc.nextInt();
		n3 = sc.nextInt();

		System.out.println();

		if (n1 < n2 && n1 < n3) {
			System.out.println(n1);
			if (n2 < n3) {
				System.out.println(n2);
				System.out.println(n3);
			}
			if (n3 < n2) {
				System.out.println(n3);
				System.out.println(n2);
			}
		}
		if (n2 < n1 && n2 < n3) {
			System.out.println(n2);
			if (n1 < n3) {
				System.out.println(n1);
				System.out.println(n3);
			}
			if(n3 < n1) {
				System.out.println(n3);
				System.out.println(n1);
			}
		}
		if (n3 < n2 && n3 < n1) {
			System.out.println(n3);
			if (n2 < n1) {
				System.out.println(n2);
				System.out.println(n1);
			}
			if (n1 < n2) {
				System.out.println(n1);
				System.out.println(n2);
			}

		}
	}
}
package Exercícios;

import java.util.Scanner;

public class ex06 {

	public static void main(String[] args) {
		// Desenvolva um algoritmo em Java que leia um número inteiro e imprima o seu
		// antecessor e seu sucessor.

		Scanner sc = new Scanner(System.in);

		int numero, s, a;

		System.out.print("Insira um valor: ");
		numero = sc.nextInt();

		a = numero - 1;
		s = numero + 1;

		System.out.println("O antecessor de " + numero + " é " + a + " e seu sucessor é " + s + ".");

	}

}

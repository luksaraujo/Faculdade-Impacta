package Exercícios;

import java.util.Scanner;

public class ex18 {

	public static void main(String[] args) {
		// Ler 10 números e imprimir quantos são pares e quantos são ímpares.

		Scanner sc = new Scanner(System.in);

		int[] vet = new int[10];
		int par = 0, impar = 0;

		for (int i = 0; i < 10; i++) {
			System.out.println("Digite um número");
			vet[i] = sc.nextInt();
		}

		for (int i = 0; i < 10; i++) {
			if (vet[i] % 2 == 0) {
				par++;
			} else {
				impar++;
			}

		}
		System.out.println(par + " números são pares.\n" + impar + " números são ímpares.");
	}
}

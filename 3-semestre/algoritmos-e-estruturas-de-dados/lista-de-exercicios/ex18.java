package Exerc�cios;

import java.util.Scanner;

public class ex18 {

	public static void main(String[] args) {
		// Ler 10 n�meros e imprimir quantos s�o pares e quantos s�o �mpares.

		Scanner sc = new Scanner(System.in);

		int[] vet = new int[10];
		int par = 0, impar = 0;

		for (int i = 0; i < 10; i++) {
			System.out.println("Digite um n�mero");
			vet[i] = sc.nextInt();
		}

		for (int i = 0; i < 10; i++) {
			if (vet[i] % 2 == 0) {
				par++;
			} else {
				impar++;
			}

		}
		System.out.println(par + " n�meros s�o pares.\n" + impar + " n�meros s�o �mpares.");
	}
}

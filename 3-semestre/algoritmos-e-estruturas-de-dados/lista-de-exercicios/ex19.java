package Exercícios;

import java.util.Scanner;

public class ex19 {

	public static void main(String[] args) {
		// Utilizando a estrutura de repetição for, faça um programa em Java que receba
		// 10 números e conte quantos deles estão no intervalo [10,20] e quantos deles
		// estão fora do intervalo, escrevendo estas informações.

		int[] vet = new int[10];
		Scanner sc = new Scanner(System.in);
		int fora = 0, intervalo = 0;
		for (int i = 0; i < 10; i++) {
			System.out.println("Digite um número");
			vet[i] = sc.nextInt();
		}
		for (int i = 0; i < 10; i++) {
			if (vet[i] >= 10 && vet[i] <= 20) {
				intervalo++;
			} else {
				fora++;
			}

		}
		System.out.println("Verificando quais números se encontram no intervalo [10,20].....");
		System.out.println();
		System.out.println("Números dentro do intervalo: " + intervalo + "\nNúmeros fora do intervalo: " + fora);

	}

}

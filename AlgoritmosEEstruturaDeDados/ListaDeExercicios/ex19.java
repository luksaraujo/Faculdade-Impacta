package Exerc�cios;

import java.util.Scanner;

public class ex19 {

	public static void main(String[] args) {
		// Utilizando a estrutura de repeti��o for, fa�a um programa em Java que receba
		// 10 n�meros e conte quantos deles est�o no intervalo [10,20] e quantos deles
		// est�o fora do intervalo, escrevendo estas informa��es.

		int[] vet = new int[10];
		Scanner sc = new Scanner(System.in);
		int fora = 0, intervalo = 0;
		for (int i = 0; i < 10; i++) {
			System.out.println("Digite um n�mero");
			vet[i] = sc.nextInt();
		}
		for (int i = 0; i < 10; i++) {
			if (vet[i] >= 10 && vet[i] <= 20) {
				intervalo++;
			} else {
				fora++;
			}

		}
		System.out.println("Verificando quais n�meros se encontram no intervalo [10,20].....");
		System.out.println();
		System.out.println("N�meros dentro do intervalo: " + intervalo + "\nN�meros fora do intervalo: " + fora);

	}

}

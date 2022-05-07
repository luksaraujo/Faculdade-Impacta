package Exercícios;

import java.util.Scanner;

public class ex13 {

	public static void main(String[] args) {
		/*Escreva um programa para ler o número de lados de um polígono regular e a
		* medida do lado (em cm). 
		* Calcular e imprimir o seguinte:  
		* Se o número de lados for igual a 3 escrever TRIANGULO e o valor da área
		* Se o número de lados for igual a 4 escrever: QUADRADO e o valor da sua área.
		* Se o número de lados for igual a 5 escrever PENTÁGONO.
		*/ 

		Scanner sc = new Scanner(System.in);

		int nLados, mLados, area;

		System.out.println("Insira o número de lados do polígono");
		nLados = sc.nextInt();

		System.out.println("Insira a medida dos lados");
		mLados = sc.nextInt();

		if (nLados == 3) {
			System.out.println("\nTRIÂNGULO");
			area = (mLados * mLados) / 2;
			System.out.println("A área do triângulo é igual a " + area);
		}
		if (nLados == 4) {
			System.out.println("\nQUADRADO");
			area = mLados * mLados;
			System.out.println("A área do quadrado é igual a " + area);
		}
		if (nLados == 5) {
			System.out.println("PENTÁGONO");
		}
	}
}

package Exerc�cios;

import java.util.Scanner;

public class ex13 {

	public static void main(String[] args) {
		/*Escreva um programa para ler o n�mero de lados de um pol�gono regular e a
		* medida do lado (em cm). 
		* Calcular e imprimir o seguinte:  
		* Se o n�mero de lados for igual a 3 escrever TRIANGULO e o valor da �rea
		* Se o n�mero de lados for igual a 4 escrever: QUADRADO e o valor da sua �rea.
		* Se o n�mero de lados for igual a 5 escrever PENT�GONO.
		*/ 

		Scanner sc = new Scanner(System.in);

		int nLados, mLados, area;

		System.out.println("Insira o n�mero de lados do pol�gono");
		nLados = sc.nextInt();

		System.out.println("Insira a medida dos lados");
		mLados = sc.nextInt();

		if (nLados == 3) {
			System.out.println("\nTRI�NGULO");
			area = (mLados * mLados) / 2;
			System.out.println("A �rea do tri�ngulo � igual a " + area);
		}
		if (nLados == 4) {
			System.out.println("\nQUADRADO");
			area = mLados * mLados;
			System.out.println("A �rea do quadrado � igual a " + area);
		}
		if (nLados == 5) {
			System.out.println("PENT�GONO");
		}
	}
}

package Exercícios;

import java.util.Scanner;

public class ex14 {

	public static void main(String[] args) {
		/*Acrescente as seguintes mensagens à solução do exercício anterior conforme o caso.
		*Caso o número de lados seja inferior a 3 escrever: NÃO É UM POLÍGONO.
		*Caso o número de lados seja superior a 5 escrever: POLÍGONO NÃO IDENTIFICADO.
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
		if (nLados < 3) {
			System.out.println("NÃO É UM POLÍGONO");
		}
		if (nLados > 5) {
			System.out.println("POLÍGONO NÃO IDENTIFICADO");
		}
	}
}

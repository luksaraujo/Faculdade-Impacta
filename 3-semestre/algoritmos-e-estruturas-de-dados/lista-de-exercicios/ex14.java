package Exerc�cios;

import java.util.Scanner;

public class ex14 {

	public static void main(String[] args) {
		/*Acrescente as seguintes mensagens � solu��o do exerc�cio anterior conforme o caso.
		*Caso o n�mero de lados seja inferior a 3 escrever: N�O � UM POL�GONO.
		*Caso o n�mero de lados seja superior a 5 escrever: POL�GONO N�O IDENTIFICADO.
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
		if (nLados < 3) {
			System.out.println("N�O � UM POL�GONO");
		}
		if (nLados > 5) {
			System.out.println("POL�GONO N�O IDENTIFICADO");
		}
	}
}

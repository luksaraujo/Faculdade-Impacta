package Exerc�cios;

import java.util.Scanner;

public class ex10 {

	public static void main(String[] args) {
		/*
		 * As ma��s custam R$ 0,30 cada se forem compradas menos do que uma d�zia, e R$
		 * 0,25 se forem compradas pelo menos doze. Escreva um programa que leia o
		 * n�mero de ma��s compradas, calcule e escreva o valor total da compra.
		 */

		Scanner sc = new Scanner(System.in);

		int qtdMacas;
		float valorTotal;

		System.out.println("Quantas ma��s voc� deseja comprar?");
		qtdMacas = sc.nextInt();

		if (qtdMacas < 12) {
			valorTotal = (float) (qtdMacas * 0.30);
			System.out.println("Valor total das ma��s: R$" + valorTotal);
		} else {
			valorTotal = (float) (qtdMacas * 0.25);
			System.out.println("Valor total das ma��s: R$" + valorTotal);
		}

	}

}

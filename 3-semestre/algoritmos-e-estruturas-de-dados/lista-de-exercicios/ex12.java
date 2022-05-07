package Exercícios;

import java.util.Scanner;

public class ex12 {

	public static void main(String[] args) {
		/*
		 * Tendo como entrada a altura e o sexo (codificado da seguinte forma:
		 * 1:feminino 2:masculino) de uma pessoa, construa um programa que calcule e
		 * imprima seu peso ideal, utilizando as seguintes Fórmulas: - para homens:
		 * (72.7 * Altura) – 58 - para mulheres: (62.1 * Altura) – 44.7
		 */

		Scanner sc = new Scanner(System.in);

		int sexo;
		double altura, peso;

		System.out.print("Qual seu gênero?\n1-Feminino\n2-Masculino\n");
		sexo = sc.nextInt();

		System.out.print("\nInsira sua altura\n");
		altura = sc.nextFloat();

		if (sexo == 1) {
			peso = (62.1 * altura) - 44.7;
			System.out.print("O seu peso ideal é de aproximadamente ");
			System.out.format("%.1f", peso);
			System.out.print(" Kgs");
		}
		if (sexo == 2) {
			peso = (72.7 * altura) - 58;
			System.out.print("O seu peso ideal é de aproximadamente ");
			System.out.format("%.1f", peso);
			System.out.print(" Kgs");
		}
	}
}

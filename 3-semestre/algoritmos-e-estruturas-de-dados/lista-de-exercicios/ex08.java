package Exerc�cios;

import java.util.Scanner;

public class ex08 {

	public static void main(String[] args) {

		/* Escreva um programa para ler o ano de nascimento de uma pessoa e escrever uma
		*mensagem que diga se ela poder� ou n�o votar este ano (n�o � necess�rio
		considerar o m�s em que ela nasceu).
		*/ 

		Scanner sc = new Scanner(System.in);

		int ano, idade;

		System.out.println("Em qual ano voc� nasceu? ");
		ano = sc.nextInt();

		idade = 2022 - ano;

		if (idade < 16) {
			System.out.println("Voc� n�o ainda n�o possui idade para votar!");
		} else {
			System.out.println("Voc� j� pode votar!");
		}
	}
}

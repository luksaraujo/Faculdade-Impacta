package Exercícios;

import java.util.Scanner;

public class ex08 {

	public static void main(String[] args) {

		/* Escreva um programa para ler o ano de nascimento de uma pessoa e escrever uma
		*mensagem que diga se ela poderá ou não votar este ano (não é necessário
		considerar o mês em que ela nasceu).
		*/ 

		Scanner sc = new Scanner(System.in);

		int ano, idade;

		System.out.println("Em qual ano você nasceu? ");
		ano = sc.nextInt();

		idade = 2022 - ano;

		if (idade < 16) {
			System.out.println("Você não ainda não possui idade para votar!");
		} else {
			System.out.println("Você já pode votar!");
		}
	}
}

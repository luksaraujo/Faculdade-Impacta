package Exercícios;

import java.util.Scanner;

public class ex01 {

	public static void main(String[] args) {
		// Faça um algoritmo que leia a idade de uma pessoa expressa em anos, meses e
		// dias e mostre-a expressa em dias. Leve em consideração o ano com 365 dias e o
		// mês com 30. (Ex: 3 anos, 2 meses e 15 dias = 1170 dias.)
		
		int idade, mes, dia, dia2, mes2, total;
		
		Scanner sc = new Scanner(System.in);
		
		System.out.print("Qual sua idade? ");
		idade = sc.nextInt();
		
		System.out.print("Qual mês você nasceu? ");
		mes = sc.nextInt();
		
		System.out.print("E em qual dia? ");
		dia = sc.nextInt();
		
		dia2 = (idade * 365);
		mes2 = (mes * 30);
		total = (mes2 + dia2 + dia);
		
		System.out.println(idade + " anos, " + mes + " meses e " + dia + " dias = " + total + " dias." );
		
	}

}

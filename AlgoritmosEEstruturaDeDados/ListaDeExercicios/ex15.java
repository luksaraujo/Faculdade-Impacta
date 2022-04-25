package Exercícios;

import java.util.Scanner;

public class ex15 {

	public static void main(String[] args) {
		// Escreva um programa para ler 3 valores inteiros e escrever o maior deles.
		// Considere que o usuário não informará valores iguais.
		
		Scanner sc = new Scanner(System.in);
		
		int n1, n2, n3;
		
		System.out.println("Insira 3 valores");
		n1 = sc.nextInt();
		n2 = sc.nextInt();
		n3 = sc.nextInt();
		
		System.out.println();
		
		if(n1 > n2 && n1 > n3) {
			System.out.println(n1);
		}
		if(n2 > n1 && n2 > n3) {
			System.out.println(n2);
		}
		if(n3 > n1 && n3 > n2) {
			System.out.println(n3);
		}
		
		

	}

}

package Exerc�cios;

import java.util.Scanner;

public class ex20 {

	public static void main(String[] args) {
		// Fa�a um programa que pe�a ao usu�rio um n�mero entre 12 e 20. Se a pessoa
		// digitar um n�mero diferente, mostrar a mensagem "entrada inv�lida" e
		// solicitar o n�mero novamente. Se digitar correto mostrar o n�mero digitado.

		Scanner sc = new Scanner(System.in);

		int n;

		System.out.println("Digite um valor entre 12 e 20!");
		n = sc.nextInt();

		while (n < 12 || n > 20) {
			System.out.println("entrada invalida!!");
			System.out.println();
			System.out.println("Digite um valor entre 12 e 20!");
			n = sc.nextInt();
		}
		System.out.println();
		System.out.println(n);

	}

}

package Exerc�cios;

import java.util.Scanner;

public class ex04 {

	public static void main(String[] args) {
		/*
		 * Escrever um algoritmo que l�: 
		 * a porcentagem do IPI a ser acrescido no valor das pe�as - o c�digo da pe�a 1, valor unit�rio da pe�a 1, quantidade de pe�as
		 * 1 - o c�digo da pe�a 2, valor unit�rio da pe�a 2, quantidade de pe�as 2 O
		 * algoritmo deve calcular o valor total a ser pago e apresentar o resultado.
		 * F�rmula : (valor1*quant1 + valor2*quant2)*(IPI/100 + 1)
		 */

		Scanner sc = new Scanner(System.in);

		double ipi, valor1, valor2, valorTotal;
		int codigo1, qtd1, codigo2, qtd2;

		System.out.println("Insira a porcentagem do IPI");
		ipi = sc.nextInt();

		System.out.println("\nInsira o c�digo, valor unit�rio e quantidade da 1� pe�a");
		codigo1 = sc.nextInt();
		valor1 = sc.nextDouble();
		qtd1 = sc.nextInt();

		System.out.println("\nInsira o c�digo, valor unit�rio e quantidade da 2� pe�a\n");
		codigo2 = sc.nextInt();
		valor2 = sc.nextDouble();
		qtd2 = sc.nextInt();
		valorTotal = (valor1 * qtd1 + valor2 * qtd2) * (ipi / 100 + 1);

		System.out.println("Aqui est�o os detalhes do seu pedido" + "\n1� pe�a" + "\nC�digo da pe�a:" + codigo1
				+ "\nValor unit�rio: R$" + valor1 + "\nQuantidade: " + qtd1 + "\n");
		System.out.println("Aqui est�o os detalhes do seu pedido" + "\n2� pe�a" + "\nC�digo da pe�a: " + codigo2
				+ "\nValor unit�rio: R$" + valor2 + "\nQuantidade: " + qtd2 + "\n");
		System.out.println("Valor total do pedido" + "\nR$" + valorTotal);

	}

}

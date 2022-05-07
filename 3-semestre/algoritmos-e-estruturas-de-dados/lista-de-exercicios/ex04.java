package Exercícios;

import java.util.Scanner;

public class ex04 {

	public static void main(String[] args) {
		/*
		 * Escrever um algoritmo que lê: 
		 * a porcentagem do IPI a ser acrescido no valor das peças - o código da peça 1, valor unitário da peça 1, quantidade de peças
		 * 1 - o código da peça 2, valor unitário da peça 2, quantidade de peças 2 O
		 * algoritmo deve calcular o valor total a ser pago e apresentar o resultado.
		 * Fórmula : (valor1*quant1 + valor2*quant2)*(IPI/100 + 1)
		 */

		Scanner sc = new Scanner(System.in);

		double ipi, valor1, valor2, valorTotal;
		int codigo1, qtd1, codigo2, qtd2;

		System.out.println("Insira a porcentagem do IPI");
		ipi = sc.nextInt();

		System.out.println("\nInsira o código, valor unitário e quantidade da 1° peça");
		codigo1 = sc.nextInt();
		valor1 = sc.nextDouble();
		qtd1 = sc.nextInt();

		System.out.println("\nInsira o código, valor unitário e quantidade da 2° peça\n");
		codigo2 = sc.nextInt();
		valor2 = sc.nextDouble();
		qtd2 = sc.nextInt();
		valorTotal = (valor1 * qtd1 + valor2 * qtd2) * (ipi / 100 + 1);

		System.out.println("Aqui estão os detalhes do seu pedido" + "\n1° peça" + "\nCódigo da peça:" + codigo1
				+ "\nValor unitário: R$" + valor1 + "\nQuantidade: " + qtd1 + "\n");
		System.out.println("Aqui estão os detalhes do seu pedido" + "\n2° peça" + "\nCódigo da peça: " + codigo2
				+ "\nValor unitário: R$" + valor2 + "\nQuantidade: " + qtd2 + "\n");
		System.out.println("Valor total do pedido" + "\nR$" + valorTotal);

	}

}

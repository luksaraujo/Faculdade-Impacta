package Exerc�cios;

public class ex02 {

	
	public static void main(String[] args) {
		
		/*Fazer um programa que imprima a m�dia aritm�tica dos n�meros 8,9 e 7. 
		 *A m�dia dos n�meros 4, 5 e 6. A soma das duas m�dias. A m�dia das m�dias. 
		 */
		 
		double n1, n2, n3, n4, n5, n6, soma, media, media2, media3;
		
		media = (8 + 9 + 7) / 3;
		media2 = (4 + 5 + 6) / 3;
		soma = media + media2;
		media3 = soma / 2;
				
		System.out.println("O resultado da opera��o � igual a " + media3);
		
	}

}

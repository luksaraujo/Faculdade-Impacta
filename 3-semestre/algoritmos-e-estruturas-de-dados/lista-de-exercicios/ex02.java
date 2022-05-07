package Exercícios;

public class ex02 {

	
	public static void main(String[] args) {
		
		/*Fazer um programa que imprima a média aritmética dos números 8,9 e 7. 
		 *A média dos números 4, 5 e 6. A soma das duas médias. A média das médias. 
		 */
		 
		double n1, n2, n3, n4, n5, n6, soma, media, media2, media3;
		
		media = (8 + 9 + 7) / 3;
		media2 = (4 + 5 + 6) / 3;
		soma = media + media2;
		media3 = soma / 2;
				
		System.out.println("O resultado da operação é igual a " + media3);
		
	}

}

package pilha;

import java.util.*;

public class UsaNo {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		RefNo ref = new RefNo();
		int op;
		cria_lista(ref);
		while (true) {
			System.out.println("====================================");
			System.out.println("Escolha a sua opção");
			System.out.println("1 - Inserir elementos na pilha");
			System.out.println("2 - Remover elementos da pilha");
			System.out.println("3 - Imprimir todos os elementos da pilha");
			System.out.println("4 - Sair");
			System.out.println("====================================");
			System.out.println("");
			System.out.print("Digite uma opção: ");
			op = sc.nextInt();
			if (op == 1)
				insere_fim(ref);
			if (op == 2)
				remove_fim(ref);
			if (op == 3)
				imprime_lista(ref);
			if (op == 4) {
				System.exit(0);
			}
		}
	}

	// Construtor da lista
	public static void cria_lista(RefNo ref) {
		ref.inicio = ref.fim = null;
	}

	// Opção 01 - Insere no fim da pilha
	public static void insere_fim(RefNo ref) {
		No novo = new No();
		Scanner sc = new Scanner(System.in);
		System.out.print("Digite um valor a ser inserido na pilha: ");
		novo.info = sc.nextInt();
		System.out.println("");
		novo.prox = null;
		if (ref.fim == null)
			ref.inicio = ref.fim = novo;
		else {
			ref.fim.prox = novo;
			ref.fim = novo;
		}
	}

	// Opção 02 - Remove no fim da pilha
	public static void remove_fim(RefNo ref) {
		No aux;
		aux = ref.inicio;
		if (ref.inicio != ref.fim) {
			//System.out.println("entrei");
			while (aux.prox != ref.fim) {
				//System.out.println(aux.info);
				aux = aux.prox;
			}
			System.out.println();
			System.out.println("Removendo o número: " + ref.fim.info);
			System.out.println();
			ref.fim = aux;
			ref.fim.prox = null;
		} else if (ref.inicio == ref.fim) {
			if (ref.inicio == null) {
				System.out.println();
				System.out.println("Pilha vazia");
				System.out.println();
			} else {
				System.out.println();
				System.out.println("Removendo o último elemento da pilha!");
				System.out.println("Removendo o elemento: " + ref.inicio.info);
				System.out.println();
				ref.inicio = ref.fim = null;
			}
		}
	}

	// Opção 03 - Imprimir a lista do início ao fim
	public static void imprime_lista(RefNo ref) {
		No aux2;
		aux2 = ref.inicio;
		System.out.println("");
		System.out.println("Elementos da pilha:");
		while (aux2 != null) {
			System.out.println("aux.info " + aux2.info);
			aux2 = aux2.prox;
		}
		System.out.println("");
	}
}

package fila;

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
			System.out.println("1 - Adicionar número na fila");
			System.out.println("2 - Remover número da fila");
			System.out.println("3 - Imprimir a fila do inicio ao fim");
			System.out.println("4 - Sair");
			System.out.println("====================================");
			System.out.println("");
			System.out.print("Digite uma opção: ");
			op = sc.nextInt();
			if (op == 1)
				insere_fim(ref);
			if (op == 2)
				remove_inicio(ref);
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

	// Opção 01 - Insere no fim da lista
	public static void insere_fim(RefNo ref) {
		No novo = new No();
		Scanner sc = new Scanner(System.in);
		System.out.print("Digite o valor a ser inserido na fila: ");
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

	// Opção 02 - Remove no início da lista
	public static void remove_inicio(RefNo ref) {
		if (ref.inicio != ref.fim) {
			System.out.println();
			System.out.println("Removendo o número: " + ref.inicio.info);
			System.out.println();
			ref.inicio = ref.inicio.prox;
		} else if (ref.inicio == ref.fim) {
			if (ref.inicio == null) {
				System.out.println();
				System.out.println("ATENÇÃO!");
				System.out.println("Não foi possível remover um elemento porque a fila está vazia!");
				System.out.println("Antes de remover elementos, adicione-os na fila.");
				System.out.println();
			} else {
				System.out.println();
				System.out.println("Removendo o último elemento presente na fila!");
				System.out.println("Removendo o número: " + ref.inicio.info);
				System.out.println();
				ref.inicio = ref.fim = null;
			}
		}
	}

	// Opção 03 - Imprimir a lista do início ao fim
	public static void imprime_lista(RefNo ref) {
		if (ref.inicio == null) {
			System.out.println();
			System.out.println("ATENÇÃO!");
			System.out.println("Não foi possível exibir os elementos da fila porque a fila está vazia!");
			System.out.println();
		} else {
			No aux2;
			aux2 = ref.inicio;
			System.out.println();
			System.out.println("Números presentes na fila, respectivamente na ordem em que aparecem:");
			while (aux2 != null) {
				System.out.println("Valor: " + aux2.info);
				aux2 = aux2.prox;
			}
			System.out.println();
		}
	}
}

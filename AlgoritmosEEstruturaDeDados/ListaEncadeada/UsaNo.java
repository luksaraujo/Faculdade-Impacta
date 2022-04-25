package lista_encadeada;

import java.util.*;

public class UsaNo {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		RefNo ref = new RefNo();
		int op;
		cria_lista(ref);
		while (true) {
			System.out.println("Escolha a sua opção");
			System.out.println("1 - Inserir no inicio da lista");
			System.out.println("2 - Remover no inicio da lista");
			System.out.println("3 - Inserir no fim da lista");
			System.out.println("4 - Remover no fim da lista");
			System.out.println("5 - Inserir no meio da lista (digite o valor cujo qual você quer inserir um número após)");
			System.out.println("6 - Imprimir a lista do inicio ao fim");
			System.out.println("7 - Sair");
			op = sc.nextInt();
			if (op == 1)
				insere_inicio(ref);
			if (op == 2)
				remove_inicio(ref);
			if (op == 3)
				insere_fim(ref);
			if (op == 4)
				remove_fim(ref);
			if (op == 5)
				insere_meio(ref);
			if (op == 6)
				imprime_lista(ref);
			if (op == 7) {
				System.exit(0);
			}
		}
	}

	// Construtor da lista
	public static void cria_lista(RefNo ref) {
		ref.inicio = ref.fim = null;
	}

	// Opção 01 - Insere no início da lista
	public static void insere_inicio(RefNo ref) {
		No novo = new No();
		Scanner sc = new Scanner(System.in);
		System.out.println("Digite um valor");
		novo.info = sc.nextInt();
		novo.prox = null;
		if (ref.inicio == null) {
			ref.inicio = ref.fim = novo;
		} else {
			novo.prox = ref.inicio;
			ref.inicio = novo;
		}
	}

	// Opção 02 - Remove no início da lista
	public static void remove_inicio(RefNo ref) {
		if (ref.inicio != ref.fim) {
			System.out.println("Removendo o elemento");
			System.out.println(ref.inicio.info);
			ref.inicio = ref.inicio.prox;
		} else if (ref.inicio == ref.fim) {
			if (ref.inicio == null)
				System.out.println("Lista vazia");
			else {
				System.out.println("Removendo o último elemento");
				System.out.println(ref.inicio.info);
				ref.inicio = ref.fim = null;
			}
		}
	}

	// Opção 03 - Insere no fim da lista
	public static void insere_fim(RefNo ref) {
		No novo = new No();
		Scanner sc = new Scanner(System.in);
		System.out.println("Digite um valor");
		novo.info = sc.nextInt();
		novo.prox = null;
		if (ref.fim == null)
			ref.inicio = ref.fim = novo;
		else {
			ref.fim.prox = novo;
			ref.fim = novo;
		}
	}

	// Opção 04 - Remove no fim da lista
	public static void remove_fim(RefNo ref) {
		No aux;
		aux = ref.inicio;
		if (ref.inicio != ref.fim) {
			System.out.println("entrei");
			while (aux.prox != ref.fim) {
				System.out.println(aux.info);
				aux = aux.prox;
			}
			System.out.println("Removendo o elemento");
			System.out.println(ref.fim.info);
			ref.fim = aux;
			ref.fim.prox = null;
		} else if (ref.inicio == ref.fim) {
			if (ref.inicio == null)
				System.out.println("Lista vazia");
			else {
				System.out.println("Removendo o último elemento");
				System.out.println(ref.inicio.info);
				ref.inicio = ref.fim = null;
			}
		}
	}

	// Opção 05 - Inserir no meio da lista
	public static void insere_meio(RefNo ref) {
		No aux, aux2 = null;
		int var, achei = 0;
		Scanner sc = new Scanner(System.in);
		System.out.println("Digite o valor de referência");
		var = sc.nextInt();
		aux = ref.inicio;
		while (aux != ref.fim) {
			if (aux.info == var) {
				achei = 1;
				aux2 = aux;
			}
			aux = aux.prox;
		}
		if (achei == 0)
			System.out.println("Elemento não encontrado");
		else {
			No novo = new No();
			System.out.println("Digite um valor");
			novo.info = sc.nextInt();
			novo.prox = aux2.prox;
			aux2.prox = novo;
		}
	}

	// Opção 06 - Imprimir a lista do início ao fim
	public static void imprime_lista(RefNo ref) {
		No aux2;
		aux2 = ref.inicio;
		while (aux2 != null) {
			System.out.println("aux.info " + aux2.info);
			aux2 = aux2.prox;
		}
	}
}

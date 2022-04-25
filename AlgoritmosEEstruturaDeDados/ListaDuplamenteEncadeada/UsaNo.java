package lista_duplamente_ligada;

import java.util.Scanner;

public class UsaNo {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        RefNo ref = new RefNo();
        No aux;
        int opcao;

        inicializaLista(ref);

        // Loop de opcoes
        while(true){
            System.out.println("\nEscolha uma opcao");
            System.out.println("1 - Imprimir Lista do Inicio");
            System.out.println("2 - Inserir no inicio da lista");
            System.out.println("3 - Remover no inicio da lista");
            System.out.println("4 - Imprimir Lista apartir do fim");
            System.out.println("5 - Inserir no fim da lista");
            System.out.println("6 - Remover no fim da lista");
            System.out.println("7 - Inserir no meio da lista");
            System.out.println("8 - Remover no meio da lista");
            System.out.println("Sair");
            opcao = sc.nextInt();

            switch (opcao){
                case 1:
                    imprimirListaInicio(ref);
                    break;
                case 2:
                    inserirInicio(ref);
                    break;
                case 3:
                    removeInicio(ref);
                    break;
                case 4:
                    imprimirListaFim(ref);
                    break;
                case 5:
                    inserirFim(ref);
                    break;
                case 6:
                    removeFim(ref);
                    break;
                case 7:
                    inserirMeio(ref);
                    break;
                case 8:
                    removerMeio(ref);
                    break;
                default:
                    System.exit(0);
                    break;
            }
        }
    }

    public static void inicializaLista(RefNo ref){
        ref.inicio = ref.fim = null;
    }

    public static int inserirValor() {
        System.out.println("\nDigite um Valor:");
        Scanner sc = new Scanner(System.in);
        return sc.nextInt();
    }

    public static void imprimirListaInicio(RefNo ref) {
        No aux;
        aux = ref.inicio;
        System.out.println("\nLista a partir do inicio");
        while(aux!=null) {
            System.out.println("valor: " + aux.info);
            aux = aux.prox;
        }
    }

    public static void inserirInicio(RefNo ref) {
        No newNo = new No();
        newNo.info = inserirValor();
        newNo.anterior = null;
        newNo.prox = null;

        if (ref.inicio == null) {
            ref.inicio = ref.fim = newNo;
        } else {
            newNo.prox = ref.inicio;
            ref.inicio.anterior = newNo;
            ref.inicio = newNo;
        }
    }

    public static void removeInicio(RefNo ref) {
        if(ref.inicio != ref.fim) {
            System.out.println("\nRemovendo Valor do inicio: " + ref.inicio.info);
            ref.inicio = ref.inicio.prox;
            ref.inicio.anterior = null;
        } else {
            if(ref.inicio == null) {
                System.out.println("Lista vazia");
            } else {
                System.out.println("\nRemovendo Valor do inicio: " + ref.inicio.info);
                ref.inicio = ref.fim = null;
            }
        }
    }

    public static void imprimirListaFim(RefNo ref) {
        No aux;
        aux = ref.fim;
        System.out.println("\nLista a partir do final");
        while(aux!=null) {
            System.out.println("valor: " + aux.info);
            aux = aux.anterior;
        }
    }

    public static void inserirFim(RefNo ref) {
        No newNo = new No();
        newNo.info = inserirValor();
        newNo.prox = null;

        if (ref.fim == null)
            ref.inicio = ref.fim = newNo;
        else {
            newNo.anterior = ref.fim;
            ref.fim.prox = newNo;
            ref.fim = newNo;
        }
    }

    public static void removeFim(RefNo ref) {
        if (ref.inicio != ref.fim) {
            System.out.println("\nRemovendo Valor do fim: " + ref.fim.info);
            ref.fim = ref.fim.anterior;
            ref.fim.prox = null;
        } else {
            if (ref.inicio == null)
                System.out.println("Lista vazia");
            else {
                System.out.println("\nRemovendo Valor do fim: " + ref.fim.info);
                ref.inicio = ref.fim = null;
            }
        }
    }

    public static void inserirMeio(RefNo ref) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Digite o valor de referência");
        int varBusca = sc.nextInt();

        No noLoop, noBusca = null;
        noLoop = ref.inicio;

        while (noLoop != ref.fim) {
            if (noLoop.info == varBusca) {
                noBusca = noLoop;
            }
            noLoop = noLoop.prox;
        }

        if (noBusca == null) {
            System.out.println("item nao encontrado");
        } else {
            No newNo = new No();
            newNo.info = inserirValor();

            System.out.println("Inserir em qual lado?");
            System.out.println("1 - esquerda");
            System.out.println("2 - direita");

            int lado = sc.nextInt();
            switch (lado){
                case 1:
                    newNo.prox = noBusca;
                    newNo.anterior = noBusca.anterior;
                    noBusca.anterior = newNo;
                    noBusca.anterior.anterior.prox = newNo;
                    break;
                case 2:
                    newNo.anterior = noBusca;
                    newNo.prox = noBusca.prox;
                    noBusca.prox = newNo;
                    break;
            }
        }
    }

    private static void removerMeio(RefNo ref) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Digite o valor de referÃªncia");
        int varBusca = sc.nextInt();

        No noLoop, noBusca = null;
        noLoop = ref.inicio;

        while (noLoop != ref.fim) {
            if (noLoop.info == varBusca) {
                noBusca = noLoop;
            }
            noLoop = noLoop.prox;
        }

        if (noBusca == null) {
            System.out.println("Lista vazia");
        } else {
            noBusca.anterior.prox = noBusca.prox;
            noBusca.prox.anterior = noBusca.anterior;
        }
    }
}
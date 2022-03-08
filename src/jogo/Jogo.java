package jogo;

import jogo.ambiente.Ambiente;
import jogo.ambiente.Evento;
import jogo.personagem.Personagem;

public class Jogo {
    // Instanciar as classes Ambiente e Personagem, entregando à personagem o
    // ambiente instanciado.
    private static Ambiente ambiente = new Ambiente();
    private static Personagem personagem = new Personagem(ambiente);

    public static void main(String[] args) {
        executar();
    }

    /*
     * Executa os métodos "executar" da classe Personagem e "evoluir" da classe
     * Ambiente.
     * Este código vai manter-se em loop até que o método "getEvento" da classe
     * Ambiente retorne o evento TERMINAR;
     */
    private static void executar() {
        do {
            personagem.executar();
            ambiente.evoluir();
        } while (ambiente.getEvento() != Evento.TERMINAR);
    }
}

package jogo;

import jogo.ambiente.Ambiente;
import jogo.ambiente.Evento;
import jogo.personagem.Personagem;

/**
 * O jogo consiste num ambiente onde a personagem tem por objetivo registar a
 * presença de animais através de fotografias tiradas por uma personagem.
 */

public class Jogo {
    // Cria uma instancia da classe "Ambiente". É neste ambiente que a personagem
    // vai atuar.
    private static Ambiente ambiente = new Ambiente();

    // Cria uma instancia da classe "Personagem", entregando o Ambiente onde a
    // personagem vai atuar.
    private static Personagem personagem = new Personagem(ambiente);

    public static void main(String[] args) {
        executar();
    }

    /**
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

package jogo.src.jogo.personagem;

import jogo.src.jogo.ambiente.Evento;

public class Percepcao {
    private Evento evento; // Evento perceptido pela personagem - entregue ao construtor na criação de uma
                           // instancia da classe

    /**
     * Construtor da classe Percepcao.
     * Recebe um argumento (Evento) e atribui o mesmo ao atributo global "evento"
     * @param evento
     */
    public Percepcao(Evento evento) {
        this.evento = evento;
    }

    /**
     * Retorna o atributo Evento da classe
     * @return Evento
     */
    public Evento getEvento() {
        return evento;
    }

}

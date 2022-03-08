package jogo.src.jogo.personagem;

import jogo.src.jogo.ambiente.Ambiente;

public class Personagem {
    private Controlo controlo = new Controlo(); // Controlo
    private Ambiente ambiente; // Atributo entregue pela classe Jogo na criação da Personagem

    public Personagem(Ambiente ambiente) {
        this.ambiente = ambiente;
    }

    /**
     * Obtém a variável percepcao através do método "percepcionar".
     * Esta variável é entregue ao método "processar" da classe Controlo, retornando
     * uma variável do tipo Accao que é então usada como argumento do método
     * "actuar".
     */
    public void executar() {
        Percepcao percepcao = percepcionar();
        Accao accao = controlo.processar(percepcao);
        actuar(accao);
    }

    /**
     * Cria e retorna uma variável do tipo Percepcao dependendo do evento entregue
     * 
     * @return Percepcao percepcao
     */
    private Percepcao percepcionar() {
        return new Percepcao(ambiente.getEvento());
    }

    /**
     * Vai permitir à personagem atuar conforme a ação (Enum) entregue como
     * argumento
     * 
     * @param accao
     */
    private void actuar(Accao accao) {

    }

}

package jogo.personagem;

import jogo.ambiente.Ambiente;

public class Personagem {
    // Classe controlo permite processar a percepcao da personagem e retorna uma
    // accao
    private Controlo controlo = new Controlo();
    // Atributo entregue pela classe Jogo na criação da Personagem - Ambiente onde a
    // personagem vai atuar
    private Ambiente ambiente;

    /**
     * Recebe o ambiente onde está inserido como argumento e associa à variável
     * criada anteriormente.
     * 
     * @param ambiente
     */
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
     * Cria e retorna uma variável do tipo Percepcao dependendo do evento entregue.
     * Permite percepcionar o que está em redor da personagem
     * 
     * @return Percepcao
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
        if (accao != null)
            System.out.printf("Accao: %s\n\n", accao);
    }

}

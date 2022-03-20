package ecr;

import jogo.personagem.Percepcao;

/**
 * Esta interface representa um estímulo.
 * Um estímulo é o que provoca uma reação e consequentemente uma resposta.
 * Um estímulo pode ser de vários tipos, como visual ou auditivo.
 */
public interface Estimulo {
    /**
     * Método vai permitir detectar a intensidade do estímulo através da percepcao
     * entregue.
     * Este método vai ser implementado noutra classe.
     * 
     * @param percepcao
     * @return float
     */
    public float detectar(Percepcao percepcao);
}

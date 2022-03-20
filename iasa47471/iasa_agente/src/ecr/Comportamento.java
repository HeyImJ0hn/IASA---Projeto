package ecr;

import jogo.personagem.Accao;
import jogo.personagem.Percepcao;

/**
 * Esta interface representa um comportamento.
 * Um comportamento é qualquer tipo de reação, relacionando padrões de percepção
 * com padrões de ação
 */
public interface Comportamento {
    /**
     * Este método vai permitir, através de uma percepcao, executar uma accao.
     * Sendo esta classe uma interface, este método vai ser implementado noutra
     * classe.
     * 
     * @param percepcao
     * @return Accao
     */
    public Accao activar(Percepcao percepcao);
}

package ecr;

import jogo.personagem.Accao;
import jogo.personagem.Percepcao;

public class Resposta {
    private Accao accao;

    /**
     * Esta classe representa a resposta a um estímulo.
     * É usada na classe "Reaccao" quando é necessário obter a resposta a um
     * estímulo.
     * 
     * @param accao
     */
    public Resposta(Accao accao) {
        this.accao = accao;
    }

    /**
     * Quando é ativado, dependendo da intensidade, é retornada a ação referente à
     * percepcao.
     * 
     * @param percepcao
     * @param intensidade
     * @return Accao
     */
    public Accao activar(Percepcao percepcao, float intensidade) {
        return null;
    }

}

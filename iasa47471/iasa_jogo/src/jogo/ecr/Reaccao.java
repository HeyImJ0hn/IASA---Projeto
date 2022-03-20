package jogo.ecr;

import jogo.personagem.Accao;
import jogo.personagem.Percepcao;

public class Reaccao implements Comportamento {
    private Estimulo estimulo;
    private Resposta resposta;

    /**
     * Esta classe representa uma reação.
     * Cada reação é composta por um estímulo, que causa a reação, e por uma
     * resposta a esse estímulo.
     * 
     * @param estimulo
     * @param resposta
     */
    public Reaccao(Estimulo estimulo, Resposta resposta) {
        this.estimulo = estimulo;
        this.resposta = resposta;
    }

    /**
     * Este método vai ser chamado quando for então detetado um estímulo por outra
     * classe.
     * É entregue a percepcao e através do método "detectar" da classe "Estimulo" é
     * possível obter a intensidade do estímulo.
     * Case a intensidade seja maior que 0 é ativada uma resposta e retornada a ação
     * para que esta seja executada.
     */
    public Accao activar(Percepcao percepcao) {
        float intensidade = estimulo.detectar(percepcao);
        if (intensidade > 0) {
            return resposta.activar(percepcao, intensidade);
        }
        return null;
    }
}

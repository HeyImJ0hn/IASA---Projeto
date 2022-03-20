package maqest;

import java.util.HashMap;
import java.util.Map;

public class Estado<EV, AC> {
    // Nome do estado
    private String nome;

    // Criação do HashMap que vai conter os eventos e as respetivas transições
    private Map<EV, Transicao<EV, AC>> transicoes = new HashMap<>();

    /**
     * Criação de um novo estado entregando o nome do mesmo.
     * Esta classe representa um estado da máquina de estados.
     * 
     * @param nome
     */
    public Estado(String nome) {
        this.nome = nome;
    }

    /**
     * Processa o evento entregue, acedendo ao HashMap de transições e retornando a
     * transição correspondente ao argumento.
     * 
     * @param evento
     * @return Transicao<EV, AC>
     */
    public Transicao<EV, AC> processar(EV evento) {
        return transicoes.get(evento);
    }

    /**
     * Permite uma transição do estado atual para o estado sucessor de acordo com o
     * evento occorido.
     * Para isto é chamado outro método com o mesmo nome e um argumento extra, neste
     * caso null, de modo a evitar repitição de código
     * 
     * @param evento
     * @param estadoSucessor
     */
    public Estado<EV, AC> transicao(EV evento, Estado<EV, AC> estadoSucessor) {
        return transicao(evento, estadoSucessor, null);
    }

    /**
     * Permite uma transição do estado atual para o estado sucessor de acordo com o
     * evento occorido e realiza uma ação
     * Insere no HashMap "transicoes", usando o evento como Key, uma nova transição
     * com o estado sucessor e a accao.
     * 
     * @param evento
     * @param estadoSucessor
     * @param accao
     */
    public Estado<EV, AC> transicao(EV evento, Estado<EV, AC> estadoSucessor, AC accao) {
        transicoes.put(evento, new Transicao<EV, AC>(estadoSucessor, accao));
        return this;
    }

    /**
     * Retorna o nome do estado
     * 
     * @return String nome
     */
    public String getNome() {
        return nome;
    }
}

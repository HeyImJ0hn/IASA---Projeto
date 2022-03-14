package jogo.maqest;

import java.util.HashMap;
import java.util.Map;

public class Estado<Evento, Accao> {
    private String nome;

    private Map<Evento, Transicao<Evento, Accao>> transicoes = new HashMap<>();

    public Estado(String nome) {
        this.nome = nome;
    }

    public Transicao<Evento, Accao> processar(Evento evento) {
        return transicoes.get(evento);
    }

    public void transicao(Evento evento, Estado<Evento, Accao> estadoSucessor) {

    }

    public void transicao(Evento evento, Estado<Evento, Accao> estadoSucessor, Accao accao) {
        
    }

    public String getNome() {
        return nome;
    }
}

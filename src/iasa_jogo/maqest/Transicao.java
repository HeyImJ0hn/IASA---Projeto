package jogo.maqest;

public class Transicao<Evento, Accao> {
    private Estado<Evento, Accao> estadoSucessor;
    private Accao ac;

    public Transicao(Estado<Evento, Accao> estadoSuccessor, Accao ac) {
        this.estadoSucessor = estadoSuccessor;
        this.ac = ac;
    }

    public Estado<Evento, Accao> getEstadoSucessor() {
        return estadoSucessor;
    }

    public Accao getAccao() {
        return ac;
    }
}

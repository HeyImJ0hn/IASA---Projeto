package jogo.maqest;

import jogo.ambiente.Evento;
import jogo.personagem.Accao;

public class MaquinaEstados {
    private Estado<Evento, Accao> estado;

    public MaquinaEstados(Estado<Evento, Accao> estado) {
        this.estado = estado;
    }

    public Accao processar(Evento evento) {
        Transicao<Evento, Accao> transicao = estado.processar(evento);
        if (transicao != null) {
            estado = transicao.getEstadoSucessor();
            return transicao.getAccao();
        }
        return null;
    }

    public Estado<Evento, Accao> getEstado() {
        return estado;
    }
}

package iasa_jogo.personagem;

import iasa_jogo.ambiente.Evento;
import iasa_jogo.maqest.Estado;
import iasa_jogo.maqest.MaquinaEstados;

public class Controlo {
    MaquinaEstados me = new MaquinaEstados(null);

    public Controlo() {
        Estado<Evento, Accao> procura = new Estado<>("Procura");
        Estado<Evento, Accao> inspeccao = new Estado<>("Inspecção");
        Estado<Evento, Accao> observacao = new Estado<>("Observação");
        Estado<Evento, Accao> registo = new Estado<>("Registo");

        procura.transicao(Evento.ANIMAL, observacao, Accao.APROXIMAR);
        procura.transicao(Evento.RUIDO, inspeccao, Accao.APROXIMAR);
        procura.transicao(Evento.SILENCIO, procura, Accao.PROCURAR);

        inspeccao.transicao(Evento.ANIMAL, observacao, Accao.APROXIMAR);
        inspeccao.transicao(Evento.RUIDO, inspeccao, Accao.PROCURAR);
        inspeccao.transicao(Evento.SILENCIO, procura);
    }

    public Estado<Evento, Accao> getEstado() {
        return null;
    }

    public Accao processar(Percepcao percepcao) {
        return me.processar(percepcao.getEvento());
    }

    public Evento getEvento() {
        return null;
    }

    private void mostrar() {

    }
}

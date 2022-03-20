package jogo.personagem;

import jogo.ambiente.Evento;
import maqest.Estado;
import maqest.MaquinaEstados;

public class Controlo {
    // Instância da classe genérica MaquinaEstados, onde são usadas as classes
    // Evento e Accao no lugar dos tipos genéricos EV e AC.
    MaquinaEstados<Evento, Accao> maqEst;

    /**
     * Construtor da classe Controlo.
     * Aqui são criados todos os estados e as suas respetivas transições.
     * No fim é iniciada a máquina de estados, que recebe como estado inicial
     * o estado "procura".
     * 
     * A transição entre estados é criada com base na função de transformação, mais
     * precisamente função de transição de estado e função de saída
     */
    public Controlo() {
        Estado<Evento, Accao> procura = new Estado<>("Procura");
        Estado<Evento, Accao> inspeccao = new Estado<>("Inspecção");
        Estado<Evento, Accao> observacao = new Estado<>("Observação");
        Estado<Evento, Accao> registo = new Estado<>("Registo");

        procura.transicao(Evento.ANIMAL, observacao, Accao.APROXIMAR)
                .transicao(Evento.RUIDO, inspeccao, Accao.APROXIMAR)
                .transicao(Evento.SILENCIO, procura, Accao.PROCURAR);

        inspeccao.transicao(Evento.ANIMAL, observacao, Accao.APROXIMAR)
                .transicao(Evento.RUIDO, inspeccao, Accao.PROCURAR)
                .transicao(Evento.SILENCIO, procura);

        observacao.transicao(Evento.ANIMAL, registo, Accao.OBSERVAR)
                .transicao(Evento.FUGA, inspeccao);

        registo.transicao(Evento.ANIMAL, registo, Accao.FOTOGRAFAR)
                .transicao(Evento.FUGA, procura)
                .transicao(Evento.FOTOGRAFIA, procura);

        maqEst = new MaquinaEstados<>(procura);
    }

    /**
     * Retorna o estado
     * 
     * @return null
     */
    public Estado<Evento, Accao> getEstado() {
        return null;
    }

    /**
     * É processado pela máquina de estádos o evento da percepcao entregue como
     * argumento e retorna uma variável do tipo Accao
     * 
     * Vai permitir à personagem atuar conforme a ação recebida da máquina de
     * estados, depois do processamento do evento.
     * 
     * @param percepcao
     * @return Accao
     */
    public Accao processar(Percepcao percepcao) {
        Accao accao = maqEst.processar(percepcao.getEvento());
        mostrar();
        return accao;
    }

    /**
     * Retorna o evento
     * 
     * @return null
     */
    public Evento getEvento() {
        return null;
    }

    /**
     * É usado para mostrar o atual estado da Máquina de Estados.
     */
    private void mostrar() {
        System.out.printf("Estado: %s\n", maqEst.getEstado().getNome());
    }
}

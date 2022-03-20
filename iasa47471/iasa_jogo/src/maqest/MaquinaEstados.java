package maqest;

public class MaquinaEstados<EV, AC> {
    private Estado<EV, AC> estado; // Estado atual da máquina de estados

    /**
     * Contrutor - Associa o estado recebido à variável "estado" da classe
     * - estado inicial da máquina de estados
     * 
     * A máquina de estados permite uma fácil troca entre os estados existentes.
     * O estado da máquina muda conforme os eventos do ambiente e provoca uma ação
     * do lado da personagem
     * 
     * @param estado
     */
    public MaquinaEstados(Estado<EV, AC> estado) {
        this.estado = estado;
    }

    /**
     * É processado o evento entregue como argumento, que retorna uma transição
     * Caso essa transição seja null, este método retorna null.
     * Caso contrário, é mudado o estado da máquina de estádos e retornado a ação da
     * transição.
     * 
     * @param evento
     * @return AC or null
     */
    public AC processar(EV evento) {
        Transicao<EV, AC> transicao = estado.processar(evento);
        if (transicao != null) {
            estado = transicao.getEstadoSucessor();
            return transicao.getAccao();
        }
        return null;
    }

    /**
     * Retorna o estado atual
     * 
     * @return Estado<EV, AC> estado
     */
    public Estado<EV, AC> getEstado() {
        return estado;
    }
}

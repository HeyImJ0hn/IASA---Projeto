package maqest;

public class Transicao<EV, AC> {
    // Estado sucessor da transição
    private Estado<EV, AC> estadoSucessor;
    // Ação da transição
    private AC accao;

    /**
     * Construtor da Transição
     * Esta classe representa uma transição e tem como objetivo guardar a informação da mesma,
     * ou seja, guardar o estado sucessor e a accao de cada transição única.
     * Recebe como argumento o estado sucessor e a accao
     * 
     * @param estadoSucessor
     * @param accao
     */
    public Transicao(Estado<EV, AC> estadoSucessor, AC accao) {
        this.estadoSucessor = estadoSucessor;
        this.accao = accao;
    }

    /**
     * Retorna o estado sucessor da transição
     * 
     * @return Estado<EV, AC>
     */
    public Estado<EV, AC> getEstadoSucessor() {
        return estadoSucessor;
    }

    /**
     * Retorna a accao da transição
     * 
     * @return AC
     */
    public AC getAccao() {
        return accao;
    }
}

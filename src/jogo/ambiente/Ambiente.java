package jogo.ambiente;

public class Ambiente {
    Evento evento;

    /**
     * Construtor
     */
    public Ambiente() {

    }

    public Evento getEvento() {
        return evento;
    }

    /**
     * Gera um novo evento através do método "gerarEvento" para evoluir o ambiente e
     * mostra o mesmo.
     */
    public void evoluir() {
        evento = gerarEvento();
        mostrar();
    }

    private Evento gerarEvento() {
        return null;
    }

    public void mostrar() {
        System.out.println(evento);
    }

}

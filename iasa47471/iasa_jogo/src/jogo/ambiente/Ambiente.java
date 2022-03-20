package jogo.ambiente;

import java.util.HashMap;
import java.util.Map;
import java.util.Scanner;

public class Ambiente {
    private Evento evento;
    private Scanner sc = new Scanner(System.in);
    private Map<String, Evento> eventos;

    /**
     * Construtor da classe Ambiente - Corrido quando é instanciado um objeto da
     * classe
     * 
     * Neste construtor é criado um HashMap que contém todos os eventos, que podem
     * ser acedidos através da respetiva string
     */
    public Ambiente() {
        eventos = new HashMap<>();
        eventos.put("s", Evento.SILENCIO);
        eventos.put("r", Evento.RUIDO);
        eventos.put("a", Evento.ANIMAL);
        eventos.put("f", Evento.FUGA);
        eventos.put("ft", Evento.FOTOGRAFIA);
        eventos.put("t", Evento.TERMINAR);
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
        System.out.print("Evento? ");
        String eventoStr = sc.next();
        return eventos.get(eventoStr);
    }

    public void mostrar() {
        System.out.printf("Evento: %s\n", evento);
    }

}

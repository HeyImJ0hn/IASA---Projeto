package jogo.ecr;

import java.util.ArrayList;
import java.util.List;

import jogo.personagem.Accao;
import jogo.personagem.Percepcao;

public class ComportComp implements Comportamento {
    private List<Comportamento> comportamentos = new ArrayList<>();

    @Override
    public Accao activar(Percepcao percepcao) {
        return null;
    }
    
}

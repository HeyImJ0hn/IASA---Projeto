from pee.mec_proc.fronteira import IAvaliador


class AvalCustoUnif(IAvaliador):
    def prioridade(self, no):
        return no.custo
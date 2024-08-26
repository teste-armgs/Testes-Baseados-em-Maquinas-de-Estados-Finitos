from pymodel.FSM import FSM
import portao

estado_inicial = portao.fechado

def teste_fsm():
    estado = estado_inicial

    estado = portao.inserir_chave(estado)
    assert estado == portao.aberto, "Erro: O portão deveria estar aberto ao inserir a chave."

    estado = portao.fechar_portao(estado)
    assert estado == portao.fechado, "Erro: O portão deveria estar fechado."

teste_fsm()



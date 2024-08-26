fechado = 'Fechado'
aberto = 'Aberto'

eventos = ['inserir_chave', 'abrir_portao', 'fechar_portao']

from pymodel.FSM import FSM

estado_inicial = fechado

def inserir_chave(estado):
    if estado == fechado:
        return aberto
    return estado

def abrir_portao(estado):
    if estado == aberto:
        return aberto
    return estado

def fechar_portao(estado):
    if estado == aberto:
        return fechado
    return estado

estados = {fechado, aberto}
acoes = {inserir_chave, fechar_portao, abrir_portao}
transicoes = {
    (fechado, inserir_chave): aberto,
    (aberto, fechar_portao): fechado,
    (aberto, abrir_portao): aberto,
}

modelo = FSM(estados, acoes, transicoes)

from datetime import datetime
from plyer import notification
import time


def verificar_horario():
    #
    numero_da_rota: str = "1B"
    horas_de_saida_da_rota_1b = [(16, 49), (16, 50), (17, 46), (18, 00), 
    (18, 00), (18, 00), (18, 00), (18, 00), (18, 00), (18, 00), 
    (18, 00), (18, 00), (18, 00), (18, 00), (18, 00), (18, 00), (18, 00), (18, 00) ] 

    horas_de_saida_da_rota_2A = [(16, 49), (16, 50), (17, 46), (18, 00), 
    (18, 00), (18, 00), (18, 00), (18, 00), (18, 00), (18, 00), 
    (18, 00), (18, 00), (18, 00), (18, 00), (18, 00), (18, 00), (18, 00), (18, 00) ] 

    horas_de_saida_da_rota_C1 = [(16, 49), (16, 50), (17, 46), (18, 00), 
    (18, 00), (18, 00), (18, 00), (18, 00), (18, 00), (18, 00), 
    (18, 00), (18, 00), (18, 00), (18, 00), (18, 00), (18, 00), (18, 00), (18, 00) ] 
    agora = datetime.now()
    # hora_de_saida = (16, 30)
    hora_atual = (agora.hour, agora.minute)

    if hora_atual == horas_de_saida_da_rota_1b[0]:
        title = "Esta saindo um Onibus"
        message = f"Esta saindo um onibus de palmares para aurora {hora_atual[0]}:{hora_atual[1]}"

        notification.notify(
        title = title,
        message = message,
        )
    elif hora_atual == horas_de_saida_da_rota_1b[1]:
        title = "Esta saindo um Onibus"
        message = f"Esta saindo um onibus de liberdade para o palmares, ROTA: 1B {hora_atual[0]}:{hora_atual[1]}"
        notification.notify(
            title = title,
            message = message
        )
    else:
        print("Nao esta saindo onibus")


#criando o loop para verificar o horario periodicamente
while True:
    verificar_horario()
    time.sleep(60)



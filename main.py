
from datetime import datetime
from plyer import notification
import time

# Defina os horários para as diferentes rotas
horario_rota01A = {
    "Liberdade": [(7, 20), (8, 5), (9, 30), (10, 30), (11, 15), (12, 0), (12, 45), (13, 30), (14, 15), (15, 45), (16, 30), (17, 15), (18, 0), (18, 30), (19, 0), (19, 30), (20, 0), (21, 15), (21, 45), (22, 15)],
    "Palmares": [(7, 35), (8, 20), (9, 45), (10, 45), (11, 30), (12, 15), (13, 0), (13, 45), (14, 30), (16, 0), (16, 45), (17, 30), (18, 15), (18, 45), (19, 15), (19, 45), (20, 15), (21, 30), (22, 0), (22, 30)],
    "Aurora": [(7, 50), (8, 35), (10, 0), (11, 45), (12, 30), (13, 15), (14, 0), (14, 45), (0, 0), (16, 15), (17, 0), (17, 45)]
}
horario_rota01B = {
     "Aurora": [(7, 54), (8, 5), (9, 30), (10, 30), (11, 15), (12, 0), (12, 45), (13, 30), (14, 50), (15, 35), (16, 20), (17, 5), (18, 35), (19, 20)],
    "Palmares": [(8, 35), (10, 0), (11, 45), (12, 30), (13, 15), (14, 0), (15, 20), (16, 5), (16, 50), (17, 35), (18, 0), (19, 5), (20, 35), (21, 5), (21, 35), (22, 5), (22, 35)],
    "Liberdade": [(7, 35), (7, 55), (8, 20), (9, 45), (10, 45), (11, 30), (12, 15), (13, 0), (13, 45), (15, 5), (15, 50), (16, 35),(17, 20), (18, 5), (18, 50), (19, 35), (20, 50), (21, 20), (21, 50), (22, 20)]
}
# vai faltar essa rota
# horario_rotaC01 = {
#     "Liberdade": [(7, 20), (8, 5), (9, 30), (10, 30), (11, 15), (12, 0), (12, 45), (13, 30), (14, 15), (15, 45), (16, 30), (17, 15), (18, 0), (18, 30), (19, 0), (19, 30), (20, 0), (21, 15), (21, 45), (22, 15)],
#     "Palmares": [(7, 35), (8, 20), (9, 45), (10, 45), (11, 30), (12, 15), (13, 0), (13, 45), (14, 30), (16, 0), (16, 45), (17, 30), (18, 15), (18, 45), (19, 15), (19, 45), (20, 15), (21, 30), (22, 0), (22, 30)],
#     "Aurora": [(7, 50), (8, 35), (10, 0), (11, 45), (12, 30), (13, 15), (14, 0), (14, 45), (0, 0), (16, 15), (17, 0), (17, 45)]
# }

def verificar_horario(rota):
    agora = datetime.now()
    hora_atual = (agora.hour, agora.minute)
    if hora_atual in horario_rota01A.get(rota, []):
        if rota == "Liberdade":
            title = "Está saindo um ônibus"
            message = f"Está saindo um ônibus de {rota} para Palmares na ROTA: 01A às {hora_atual[0]}:{hora_atual[1]}"
            notification.notify(title=title, message=message)
        if rota == "Palmares":
            title = "Está saindo um ônibus"
            message = f"Está saindo um ônibus de {rota} para Aurora na ROTA: 01A às {hora_atual[0]}:{hora_atual[1]}"
            notification.notify(title=title, message=message)
        if rota == "Aurora":
            title = "Está saindo um ônibus"
            message = f"Está saindo um ônibus de {rota} para Liberdade na ROTA: 01A às {hora_atual[0]}:{hora_atual[1]}"
            notification.notify(title=title, message=message)
            #______________ROTA B________________________
    if hora_atual in horario_rota01B.get(rota, []):
        if rota == "Liberdade":
            title = "Está saindo um ônibus"
            message = f"Está saindo um ônibus de {rota} para Palmares na ROTA: 01B às {hora_atual[0]}:{hora_atual[1]}"
            notification.notify(title=title, message=message)
        if rota == "Palmares":
            title = "Está saindo um ônibus"
            message = f"Está saindo um ônibus de {rota} para Aurora ROTA: 01B às {hora_atual[0]}:{hora_atual[1]}"
            notification.notify(title=title, message=message)
        if rota == "Aurora":
            title = "Está saindo um ônibus"
            message = f"Está saindo um ônibus de {rota} para Liberdade ROTA: 01B às {hora_atual[0]}:{hora_atual[1]}"
            notification.notify(title=title, message=message)
            #_________________ROTA C___________________
    # if hora_atual in horario_rota02.get(rota, []):
    #     if rota == "Palmares":
    #         title = "Está saindo um ônibus"
    #         message = f"Está saindo um ônibus de {rota} para Aurora às {hora_atual[0]}:{hora_atual[1]}"
    #         notification.notify(title=title, message=message)
    #     if rota == "Aurora":
    #         title = "Está saindo um ônibus"
    #         message = f"Está saindo um ônibus de {rota} para Liberdade às {hora_atual[0]}:{hora_atual[1]}"
    #         notification.notify(title=title, message=message)
    else:
        print(f"Não está saindo ônibus de {rota} no momento")

# Loop infinito para verificar o horário periodicamente
while True:
    verificar_horario("Liberdade")
    verificar_horario("Palmares")
    verificar_horario("Aurora")
    time.sleep(60)  # Verificar a cada minuto (ajuste conforme necessário)

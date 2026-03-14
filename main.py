from microbit import *
import radio
import log

# Configurar o rádio (mesmo canal dos alunos)
radio.on()
radio.config(group=42)

# Configurar o registo de dados (Data Logging)
log.set_labels('IDAluno', 'Volume', timestamp=log.SECONDS)

display.scroll("Prof")

while True:
    # Fica à escuta para ver se chega alguma mensagem de rádio
    mensagem = radio.receive()

    if mensagem:
        dados = mensagem.split(",")

        # Garantir que a mensagem está bem formada (tem 2 partes)
        if len(dados) == 2:
            id_aluno = int(dados[0])
            volume = int(dados[1])

            # 1. GUARDAR OS DADOS NO FICHEIRO
            log.add({
                'IDAluno': id_aluno,
                'Volume': volume
            })

            # 2. ACENDER O LED CORRESPONDENTE AO ALUNO
            if 1 <= id_aluno <= 25:
                x = (id_aluno - 1) % 5
                y = (id_aluno - 1) // 5
                # Acende o LED no brilho máximo (9)
                display.set_pixel(x, y, 9)

    # 3. APAGAR OS AVISOS
    if button_a.was_pressed():
        display.clear()

    sleep(20)
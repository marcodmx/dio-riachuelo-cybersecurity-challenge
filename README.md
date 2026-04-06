# 🛡️ Cybersecurity Challenge - Ransomware & Keylogger Simulation

Este repositório contém o desenvolvimento de ferramentas de simulação para fins estritamente educacionais, como parte do **Bootcamp de Cibersegurança da DIO em parceria com a Riachuelo**. O objetivo é demonstrar o funcionamento interno de malwares comuns para fortalecer mecanismos de defesa.

---

## ⚠️ Aviso Legal (Disclaimer)
> **Este projeto é destinado apenas para fins de aprendizado e conscientização sobre segurança cibernética.** O uso destas ferramentas em sistemas sem autorização explícita é ilegal e antiético. O desenvolvedor não se responsabiliza pelo uso indevido deste software.

---

## 📂 Estrutura do Projeto

O repositório está dividido em duas frentes de estudo:

### 1. 🔒 Ransomware Simulation (`/ransomware-simulation`)
Simulação de um ataque de criptografia de dados com recuperação de arquivos.
* **`ransomware.py`**: Utiliza a biblioteca `cryptography` (Fernet) para localizar e criptografar arquivos em uma pasta de teste.
* **`descriptografar.py`**: Ferramenta de recuperação que utiliza a chave gerada para restaurar os arquivos ao estado original.
* **`test_files/`**: Diretório contendo arquivos `.txt` fictícios para validar a eficácia da criptografia.

### 2. ⌨️ Keylogger Simulation (`/keylogger-simulation`)
Simulação de captura de entradas de teclado para estudo de exfiltração de dados.
* **`keylogger.py`**: Versão base que registra as teclas em um arquivo `log.txt` local.
* **`keylogger_email.py`**: Versão avançada que utiliza `smtplib` e `threading` para enviar logs periodicamente via e-mail (exfiltração remota).
* **`keylogger.pyw`**: Versão "furtiva" (Stealth) que roda em segundo plano no Windows sem abrir janela de console.

---

## 🛠️ Tecnologias Utilizadas

| Tecnologia | Finalidade |
| :--- | :--- |
| **Python** | Linguagem principal do projeto. |
| **Cryptography (Fernet)** | Criptografia simétrica robusta para o Ransomware. |
| **Pynput** | Monitoramento de eventos de entrada (teclado). |
| **Smtplib** | Protocolo de transferência de e-mail para exfiltração. |
| **Threading** | Execução paralela para envio de logs em intervalos. |

---

## 🚀 Como Executar (Ambiente de Teste)

1. **Clonar o repositório:**
2. **Instalar dependências:**
```bash
pip install cryptography pynput
```

3. **Testar o Ransomware:**

Execute python ransomware.py para criptografar a pasta test_files.

Verifique que os arquivos ficaram ilegíveis.

Execute python descriptografar.py para restaurar os dados.

4. **Testar o Keylogger:**

Execute python keylogger.py.

Digite algumas teclas e verifique o arquivo log.txt gerado.

## 🛡️ Medidas de Segurança Adotadas no Código

* **Sem Credenciais Reais:** O código utiliza *placeholders* para e-mails e senhas, seguindo as melhores práticas de segurança do GitHub e evitando a exposição de dados sensíveis.
* **Segurança de Execução:** O Ransomware possui travas de segurança (filtros de nome) para garantir que não criptografe seus próprios scripts de recuperação ou arquivos do sistema.
* **Conscientização:** Toda a documentação e estrutura do código foram desenhadas com foco estritamente defensivo, visando o entendimento técnico de ameaças para o fortalecimento de perícia e resposta a incidentes.

Desenvolvido por [Marco] para o ecossistema DIO. 🚀

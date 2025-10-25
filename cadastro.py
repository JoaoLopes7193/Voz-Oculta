from tkinter import *
from tkinter import messagebox
from datetime import datetime
COR_FUNDO = "#ECEFF1"
COR_TEXTO = "#37474F"
COR_PRINCIPAL = "#37474F"
COR_BOTAO = "#607D8B"
COR_LINK = "#1565C0"
janela = Tk()
janela.title("📢 Voz Oculta - Canal de Denúncias")
janela.geometry("600x600") 
janela.configure(bg=COR_FUNDO)
janela.resizable(False, False)
def criar_area_clicavel(parent, texto, comando, bg_color, fg_color, font_size=12):
    frame_btn = Frame(parent, bg=bg_color, relief=RAISED, bd=1)
    msg = Message(frame_btn, text=texto, width=500, 
                  bg=bg_color, fg=fg_color, justify=CENTER,
                  font=("Arial", font_size, "bold"))
    msg.pack(padx=15, pady=8)
    frame_btn.bind('<Button-1>', lambda event: comando())
    msg.bind('<Button-1>', lambda event: comando()) 
    return frame_btn
def exibir_mensagem_estatica(parent, texto, font_style=("Arial", 12), bg_color=COR_FUNDO, fg_color=COR_TEXTO, padding=10):
    msg = Message(parent, text=texto, width=500, 
                  bg=bg_color, fg=fg_color, justify=CENTER,
                  font=font_style)
    msg.pack(pady=padding)
    return msg
def limpar_tela():
    for widget in janela.winfo_children():
        widget.destroy()
def ler_denuncias_simples():
    try:
        with open("denuncias_simples.txt", "r", encoding="utf-8") as arquivo:
            conteudo = arquivo.read()
        janela_denuncias = Toplevel(janela)
        janela_denuncias.title("Denúncias Salvas (Admin)")
        janela_denuncias.geometry("500x400")
        exibir_mensagem_estatica(janela_denuncias, "RELATÓRIOS SALVOS:", font_style=("Arial", 14, "bold"), fg_color="#1565C0", bg_color="white").pack(pady=10)
        area_texto = Text(janela_denuncias, wrap=WORD, height=20, width=50, font=("Arial", 10))
        area_texto.pack(pady=10, padx=10)
        area_texto.insert(END, conteudo if conteudo else "Nenhuma denúncia encontrada.")
        area_texto.config(state=DISABLED)
    except FileNotFoundError:
        messagebox.showinfo("Arquivo", "Nenhuma denúncia foi registrada ainda.")
    except Exception as e:
        messagebox.showerror("Erro", f"Erro ao ler o arquivo: {e}")
def mostrar_tela_login():
    limpar_tela()
    exibir_mensagem_estatica(janela, "📢 Voz Oculta", font_style=("Arial", 28, "bold"), 
                             bg_color=COR_PRINCIPAL, fg_color="white", padding=10).pack(fill="x")
    exibir_mensagem_estatica(janela, "Selecione uma opção:", font_style=("Arial", 16, "bold")).pack(pady=30)
    criar_area_clicavel(janela, 
                        "FAZER DENÚNCIA (Sem Cadastro/Anônima)",
                        mostrar_tela_denuncia, 
                        "#455A64", "white", 14).pack(pady=15, padx=50)
    criar_area_clicavel(janela, 
                        "CADASTRAR NOVO USUÁRIO",
                        mostrar_tela_cadastro, 
                        COR_LINK, "white", 12).pack(pady=10, padx=50)
    exibir_mensagem_estatica(janela, "--- Acesso de Gestão/Admin ---", font_style=("Arial", 12), padding=20)
    exibir_mensagem_estatica(janela, "Usuário:", font_style=("Arial", 12), padding=0).pack()
    entrada_usuario = Entry(janela, font=("Arial", 12), width=30)
    entrada_usuario.pack(pady=5)
    exibir_mensagem_estatica(janela, "Senha:", font_style=("Arial", 12), padding=0).pack()
    entrada_senha = Entry(janela, font=("Arial", 12), show="*", width=30)
    entrada_senha.pack(pady=5)
    def fazer_login():
        usuario = entrada_usuario.get()
        senha = entrada_senha.get()
        if usuario == "admin" and senha == "1234":
            messagebox.showinfo("Sucesso", "Login de Gestão bem-sucedido!")
            ler_denuncias_simples()
        else:
            messagebox.showerror("Erro", "Usuário ou senha incorretos! Tente 'admin'/'1234'.")
    criar_area_clicavel(janela, "ENTRAR (Gestão)", fazer_login, COR_BOTAO, "white", 12).pack(pady=15, padx=50)
def mostrar_tela_cadastro():
    limpar_tela()
    exibir_mensagem_estatica(janela, "📢 Voz Oculta", font_style=("Arial", 28, "bold"), 
                             bg_color=COR_PRINCIPAL, fg_color="white", padding=10).pack(fill="x")
    exibir_mensagem_estatica(janela, "Cadastro de Novo Usuário (Apenas E-mail e Senha)", font_style=("Arial", 16, "bold")).pack(pady=20)
    exibir_mensagem_estatica(janela, "E-mail:", font_style=("Arial", 12), padding=0).pack()
    entrada_email = Entry(janela, font=("Arial", 12), width=30)
    entrada_email.pack(pady=5)
    exibir_mensagem_estatica(janela, "Senha:", font_style=("Arial", 12), padding=0).pack()
    entrada_senha = Entry(janela, font=("Arial", 12), show="*", width=30)
    entrada_senha.pack(pady=5)
    def fazer_cadastro():
        email = entrada_email.get()
        senha = entrada_senha.get()
        if email and senha:
            messagebox.showinfo("Sucesso", f"Usuário {email} cadastrado com sucesso! Use o Login de Gestão.")
            mostrar_tela_login()
        else:
            messagebox.showwarning("Aviso", "Preencha todos os campos.")
    criar_area_clicavel(janela, "CADASTRAR", fazer_cadastro, COR_BOTAO, "white", 12).pack(pady=15, padx=50)
    criar_area_clicavel(janela, "Voltar para Opções Iniciais", mostrar_tela_login, COR_FUNDO, COR_TEXTO, 10).pack(pady=10, padx=50)
def mostrar_tela_denuncia():
    limpar_tela()
    exibir_mensagem_estatica(janela, "📢 Voz Oculta", font_style=("Arial", 28, "bold"), 
                             bg_color=COR_PRINCIPAL, fg_color="white", padding=10).pack(fill="x")
    exibir_mensagem_estatica(janela, "Denúncia Anônima de Exploração", font_style=("Arial", 18, "bold")).pack(pady=20)
    exibir_mensagem_estatica(janela, "Seu anonimato é garantido. Descreva o caso abaixo:", font_style=("Arial", 12)).pack()
    caixa_texto = Text(janela, height=8, width=50, font=("Arial", 10))
    caixa_texto.pack(pady=10)
    def enviar_denuncia():
        texto = caixa_texto.get("1.0", END).strip()
        data_hora = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        if texto:
            try:
                with open("denuncias_simples.txt", "a", encoding="utf-8") as arquivo:
                    arquivo.write("=" * 40 + "\n")
                    arquivo.write(f"Denúncia Registrada em: {data_hora}\n")
                    arquivo.write(texto + "\n")
                    arquivo.write("=" * 40 + "\n\n")
                messagebox.showinfo("Sucesso", "Denúncia enviada com sucesso! Voltando para a tela inicial.")
                mostrar_tela_login()
            except Exception as e:
                messagebox.showerror("Erro", f"Falha ao salvar a denúncia: {e}")
        else:
            messagebox.showwarning("Aviso", "Por favor, escreva algo antes de enviar a denúncia.")
    criar_area_clicavel(janela, "ENVIAR DENÚNCIA", enviar_denuncia, "#455A64", "white", 12).pack(pady=15, padx=50)
    criar_area_clicavel(janela, "Voltar (Cancelar Denúncia)", mostrar_tela_login, COR_FUNDO, COR_TEXTO, 10).pack(pady=10, padx=50)
mostrar_tela_login()
janela.mainloop()

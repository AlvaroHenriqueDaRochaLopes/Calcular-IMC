import customtkinter as ctk
from tkinter import messagebox

ctk.set_appearance_mode("dark")        # Tema escuro moderno
ctk.set_default_color_theme("blue")    # Tema azul (pode mudar para: "green", "dark-blue")


def calcular_imc():
    try:
        peso = float(entry_peso.get())
        altura = float(entry_altura.get())
        imc = peso / (altura ** 2)

        if imc < 18.5:
            classificacao = "Abaixo do peso"
        elif 18.5 <= imc < 24.9:
            classificacao = "Peso normal"
        elif 25 <= imc < 29.9:
            classificacao = "Sobrepeso"
        elif 30 <= imc < 34.9:
            classificacao = "Obesidade grau 1"
        elif 35 <= imc < 39.9:
            classificacao = "Obesidade grau 2"
        else:
            classificacao = "Obesidade grau 3"

        label_resultado.configure(
            text=f"IMC: {imc:.2f}\nClassificação: {classificacao}"
        )

    except ValueError:
        messagebox.showerror("Erro", "Digite valores válidos para peso e altura!")


app = ctk.CTk()
app.title("Calculadora de IMC")
app.geometry("400x350")


# ---- TÍTULO ----
titulo = ctk.CTkLabel(app, text="Calculadora de IMC", font=("Arial", 22, "bold"))
titulo.pack(pady=15)

# ---- PESO ----
frame_peso = ctk.CTkFrame(app)
frame_peso.pack(pady=10)

label_peso = ctk.CTkLabel(frame_peso, text="Peso (kg):", font=("Arial", 16))
label_peso.pack(side="left", padx=8)

entry_peso = ctk.CTkEntry(frame_peso, width=120)
entry_peso.pack(side="left")

# ---- ALTURA ----
frame_altura = ctk.CTkFrame(app)
frame_altura.pack(pady=10)

label_altura = ctk.CTkLabel(frame_altura, text="Altura (m):", font=("Arial", 16))
label_altura.pack(side="left", padx=8)

entry_altura = ctk.CTkEntry(frame_altura, width=120)
entry_altura.pack(side="left")

# ---- BOTÃO ----
botao = ctk.CTkButton(app, text="Calcular IMC", command=calcular_imc, height=40)
botao.pack(pady=20)

# ---- RESULTADO ----
label_resultado = ctk.CTkLabel(app, text="", font=("Arial", 18))
label_resultado.pack(pady=15)

app.mainloop()

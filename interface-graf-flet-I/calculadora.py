import flet as ft

def main(page: ft.Page):
    page.title = "Calculadora"

    num1 = ft.TextField(label="Número 1", width=150)
    num2 = ft.TextField(label="Número 2", width=150)
    resultado = ft.Text()

    def calcular(op):
        try:
            a = float(num1.value)
            b = float(num2.value)
            res = {
                "+": a + b,
                "-": a - b,
                "*": a * b,
                "/": a / b if b != 0 else "Erro: divisão por zero"
            }[op]
            resultado.value = f"Resultado: {res}"
        except:
            resultado.value = "Erro: valores inválidos"
        page.update()

    botoes = [
        ft.ElevatedButton(text=op, on_click=lambda e, o=op: calcular(o))
        for op in ["+", "-", "*", "/"]
    ]

    page.add(num1, num2, *botoes, resultado)

ft.app(target=main)
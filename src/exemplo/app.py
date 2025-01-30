from cyclopts import App

app = App()


@app.default
def default(nome):
    print(f'Olá {nome}')


def main():
    app()


from flask import Flask, render_template, request, redirect, flash
from banco import Conta


app = Flask(__name__)

app.secret_key = "pybank-chave-secreta"

conta1 = None
conta2 = None


@app.route("/")
def inicio():

    if conta1 is None or conta2 is None:
        return redirect("/cadastro")

    saldo_total = conta1.saldo + conta2.saldo

    guardado_total = (
        conta1.saldo_guardado +
        conta2.saldo_guardado
    )

    return render_template(
        "index.html",
        conta1=conta1,
        conta2=conta2,
        saldo_total=saldo_total,
        guardado_total=guardado_total
    )


@app.route("/cadastro")
def cadastro():
    return render_template("cadastro.html")


@app.route("/cadastrar", methods=["POST"])
def cadastrar():

    global conta1, conta2

    titular1 = request.form["titular1"]
    numero_conta1 = request.form["numero_conta1"]
    saldo1 = float(request.form["saldo1"])

    titular2 = request.form["titular2"]
    numero_conta2 = request.form["numero_conta2"]
    saldo2 = float(request.form["saldo2"])

    conta1 = Conta(
        titular1,
        numero_conta1,
        saldo1
    )

    conta2 = Conta(
        titular2,
        numero_conta2,
        saldo2
    )

    flash("Contas cadastradas com sucesso!", "sucesso")

    return redirect("/")


@app.route("/movimentar", methods=["POST"])
def movimentar():

    conta_escolhida = request.form["conta"]
    operacao = request.form["operacao"]

    print("Conta 1:", conta1)
    print("Conta 2:", conta2)
    print("Conta escolhida:", conta_escolhida)

    try:
        valor = float(request.form["valor"])

    except ValueError:
        flash("Digite um valor válido.", "erro")
        return redirect("/")

    if conta_escolhida == "1":
        conta = conta1
    else:
        conta = conta2

    if operacao == "depositar":
        sucesso, mensagem = conta.depositar(valor)

    elif operacao == "sacar":
        sucesso, mensagem = conta.sacar(valor)

    elif operacao == "guardar":
        sucesso, mensagem = conta.guardar_dinheiro(valor)

    elif operacao == "resgatar":
        sucesso, mensagem = conta.resgatar_dinheiro(valor)

    else:
        flash("Operação inválida.", "erro")
        return redirect("/")

    if sucesso:
        flash(mensagem, "sucesso")
    else:
        flash(mensagem, "erro")

    return redirect("/")


@app.route("/resetar")
def resetar():

    global conta1, conta2

    conta1 = None
    conta2 = None

    flash("Contas resetadas.", "sucesso")

    return redirect("/cadastro")


if __name__ == "__main__":
    app.run()

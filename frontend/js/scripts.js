
const consultas_div = document.querySelector(".consultas")
const form = document.querySelector("form")
const mensagemDiv = document.getElementById("mensagem");
const div_resultado = document.querySelector(".consulta_atual")
const tituloHistorico = document.querySelector(".titulo_historico");

function formatar_moeda(valor) {
    return valor.toLocaleString("pt-BR", {
        style: "currency",
        currency: "BRL"
    });
}

function formatar_data(data) {
    return data.toLocaleString("pt-BR", {
        day: "2-digit",
        month: "2-digit",
        year: "numeric",
        hour: "2-digit",
        minute: "2-digit"
    });
}

function mostrar_mensagem(texto, tipo = "erro") {
    mensagemDiv.textContent = texto;
    mensagemDiv.className = `mensagem ${tipo}`;
    mensagemDiv.style.display = "block";


    setTimeout(() => {
        mensagemDiv.style.display = "none";
    }, 2000);
}

function criar_card_consulta(tipo_cliente, valor_pago, cashback, data) {
    const div = document.createElement("div")
    div.classList.add("consulta");
    div.innerHTML = `
        <p>Tipo de cliente: <span>${tipo_cliente}</span></p>
        <p>Valor pago: <span>${formatar_moeda(valor_pago)}</span></p>
        <p>Cashback concedido: <span>${formatar_moeda(cashback)}</span></p>
        <p>Data de consulta: <span>${formatar_data(data)}</span></p>
    `
    consultas_div.appendChild(div);
}

function criar_card_resultado(tipo_cliente, valor_pago, cashback, data) {
    div_resultado.innerHTML = `
        <p class="fechar">X</p>
        <p>Tipo de cliente: <span>${tipo_cliente}</span></p>
        <p>Valor pago: <span>${formatar_moeda(valor_pago)}</span></p>
        <p>Cashback concedido: <span>${formatar_moeda(cashback)}</span></p>
        <p>Data de consulta: <span>${formatar_data(data)}</span></p>
    `
    div_resultado.classList.remove("disable")
    mostrar_mensagem("Consulta realizada com sucesso!", "sucesso");
}


async function carregar_historico() {

    consultas_div.innerHTML = "";

    try {
        const response = await fetch("/cashback/listar", {
            method: "GET"
        })

        const data = await response.json()

        if (data.length === 0) {
            tituloHistorico.textContent = "Nenhuma consulta anterior realizada ainda";
            return;
        } 
        else if (data.length === 1) {
            tituloHistorico.textContent = `Abaixo você pode ver sua última consulta`;

        }
        else {
            tituloHistorico.textContent = `Abaixo você pode ver suas ${data.length} últimas consultas`;
        }

        data.forEach((consulta) => {
            criar_card_consulta(consulta.tipo_cliente, consulta.valor_pago, consulta.cashback, new Date(consulta.created_at))
        })
    }
    catch (err) {
        console.error(err)
    }
}

div_resultado.addEventListener("click", (e) => {
    if (e.target.classList.contains("fechar")) {
        div_resultado.classList.add("disable");
    }
});

form.addEventListener("submit", async (e) => {
    e.preventDefault()



    try {
        await carregar_historico();
        const form_data = new FormData(form)
        const valor = Number(form_data.get("valor"))
        const tipo = form_data.get("tipo_cliente")
        const response = await fetch("/cashback/calcular", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                valor_pago: valor,
                tipo_cliente: tipo
            })
        })

        if (!response.ok) {
            throw new Error("Erro ao calcular cashback");
        }

        const data = await response.json()



        criar_card_resultado(data.tipo_cliente, data.valor_pago, data.cashback, new Date());
    }
    catch (error) {
        mostrar_mensagem("Erro ao realizar consulta. Tente novamente.");
        console.error("Erro na requisição")
    }
})

window.addEventListener("DOMContentLoaded", () => {
    div_resultado.classList.add("disable")
    carregar_historico()
})

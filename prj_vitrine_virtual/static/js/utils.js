// Impede que o clique feche o dropdown
{
    const submit_button = document.getElementById("submit-btn");
    submit_button.addEventListener("click", function(e){
        e.stopPropagation();
    });
}

// Evento para verificar o usuário e senha e realizar o login
{
    // Função que envia os dados do formulário e aguarda a resposta do servidor
    // Caso o usuário tiver digitado corretamente o usuário e senha é feito o login e reencaminhado para a "/"
    // Caso o usuário tiver digitado incorretamente o usuário e senha é apresentado uma mensagem de erro
    // Com essa função não há o carregamento da página inteira, apenas é atualizado o campo "login-message"
    const dropdown_form = document.getElementById("dropdown-login");
    dropdown_form.addEventListener("submit", async function(event){
        event.preventDefault(); // Impede o envio tradicional do formulário
        const formData = new FormData(this); // Formulário
        const response = await fetch('/users/login/', {
            method: 'POST',
            headers: {
                'X-CSRFToken': getCookie('csrftoken') // Inserção do token no cabeçalho
            },
            body: formData
        });
        const data = await response.json();
        const login_message = document.getElementById("login-message")
            if (data.success){
                login_message.textContent = "Login realizado com sucesso!";
                login_message.style.color = "green";
                window.location.href = '/';
            } else {
                login_message.textContent = "Usuário e/ou senha inválidos!";
                login_message.style.color = "red";
            }
    });
}

// Função para confirmação de exclusão de conta
function delete_account(){
    if (window.confirm("Deseja realmente excluir sua conta?") == true) {
        // Chamar a função de exclusão de conta
        window.location.href = '/users/excluir-conta/';
    }
}

// Função que solicita a reserva do item ao servidor
function reserve_item(item_id, total_items){
    const input = document.getElementById("items_quantity");
    const item_qty = Number(input.value);
    let option = false;

    if (item_qty >= 1 && item_qty <= Number(total_items)){
        option = window.confirm(`Você selecionou a quantidade de ${item_qty} itens, deseja reservá-los?`);
    } else if (item_qty > Number(total_items)){
        window.alert(`Você deve selecionar no máximo a quantidade de ${total_items} itens!`);
    } else {
        window.alert("Você deve escolher a quantidade de um item ou mais!");
    };

    if (option){
        const response = fetch("/users/reservar-item/", {
            method: "POST",
            headers: {
                'X-CSRFToken': getCookie('csrftoken'), // Inserção do token no cabeçalho
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                item_id: item_id,
                item_qty: item_qty
            })
        }).then(response => {
            if (!response.ok){
                throw new Error("Erro na resposta do servidor");
            };
            return response.json(); // Converte a resposta pa JS
        }).then(data => {
            console.log("Resposta do Django:", data);
        }).catch(error => {
            console.error("Erro:", error);
        })
    };
}

// Função que mostra um popover informando que é necessário fazer login
function show_popover(){
    console.log("O mouse entrou no botão!");
}

// Função que o token do Django
function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
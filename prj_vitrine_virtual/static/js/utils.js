// Impede que o clique feche o dropdown
{
document.getElementById("submit-btn").addEventListener("click", function(e){
    e.stopPropagation();
});
};

// Função para confirmação de exclusão de conta
function delete_account(){
    if (confirm("Deseja realmente excluir sua conta?") == true) {
        // Chamar a função de exclusão de conta
        window.location.href = '/users/excluir-conta/';
    }
}

// Função para verificar o usuário e senha e realizar o login
function user_login(){
    // Função que envia os dados do formulário e aguarda a resposta do servidor
    // Caso o usuário tiver digitado corretamente o usuário e senha é feito o login e reencaminhado para a "/"
    // Caso o usuário tiver digitado incorretamente o usuário e senha é apresentado uma mensagem de erro
    // Com essa função não há o carregamento da página inteira, apenas é atualizado o campo "login-message"
    const dropdown_form = document.getElementById("dropdown-login");
    dropdown_form.addEventListener("submit", async function(event){
        event.preventDefault(); // Impede o envio tradicional do formulário
        const formData = new FormData(this); // Formulário
        const token = document.getElementsByName("csrfmiddlewaretoken").values(); // Token CSRF exigido pelo Django
        const response = await fetch('/users/login/', {
            method: 'POST',
            headers: {
                'X-CSRFToken': token // Inserção do token no cabeçalho
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
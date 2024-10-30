document.getElementById("buscarCliente").addEventListener("input", function() {
    const query = this.value;

    if (query.length < 1) {
        document.getElementById("resultadoBusca").innerHTML = ""; 
        return;
    }

    fetch(`/buscar-contatos/?q=${query}`)
        .then(response => response.json())
        .then(data => {
            const resultadoBusca = document.getElementById("resultadoBusca");
            resultadoBusca.innerHTML = ""; 

            data.forEach(contato => {
                const item = document.createElement("li");
                item.textContent = contato.nome;
                item.classList.add("list-group-item", "list-group-item-action");
                item.onclick = () => {
                    document.getElementById("buscarCliente").value = contato.nome; 
                    resultadoBusca.innerHTML = "";  
                };
                resultadoBusca.appendChild(item);
            });
        })
        .catch(error => console.error("Erro na busca:", error));
});
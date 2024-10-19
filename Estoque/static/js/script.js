console.log('Arquivo carregado.')
document.querySelectorAll('.btn.btn-sm.btn-info').forEach(item =>{
    item.addEventListener('click', ()=> {
        
        const list = item.parentElement.parentElement

        itemList = list.children

        nameItem = itemList[1]

        fetch('estoque/', {
            method: 'POST',
            headers: {
                'X-CSRFToken': '{{ csrf_token }}',
            },

        })
        nameItem.innerHTML = `<input type='text' value='{{produto.descricao}}'></input>`

        
    })
})
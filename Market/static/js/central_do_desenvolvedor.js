document.querySelectorAll('.status').forEach(app=> {
    app.addEventListener('load', function(){
        if (app.textContent == 'Aprovado'){
            app.setAttribute('class', 'badge bg-success status')
        }
        if (app.textContent == 'Em análise'){
            app.setAttribute('class', 'badge bg-warning status ')
        }
    })
})
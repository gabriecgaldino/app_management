document.addEventListener("DOMContentLoaded", function() {
    const addRowButton = document.getElementById("addRowButton");
    const salesTableBody = document.getElementById("salesTableBody");

    addRowButton.addEventListener("click", function() {
        const newRow = document.createElement("tr");

        newRow.innerHTML = `
            <td><label class="form-control">0</label></td>
            <td><input type="text" class="form-control busca-produto" name="produto[]"></td>
            <td><input type="text" class="form-control" name="valor_total[]"></td>
            <td><input type="number" class="form-control" name="quantidade[]"></td>
            <td><input type="text" class="form-control" name="valor[]"></td>
            <td><button type="button" class="btn btn-danger btn-remove-row">x</button></td>
        `;
        salesTableBody.appendChild(newRow);

        newRow.querySelector(".btn-remove-row").addEventListener("click", function() {
            newRow.remove();
        });
    });

    document.querySelectorAll(".btn-remove-row").forEach(button => {
        button.addEventListener("click", function() {
            this.closest("tr").remove();
        });
    });
});
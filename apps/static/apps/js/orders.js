function updatePrice(select) {
    const price = select.options[select.selectedIndex].dataset.price;
    const row = select.closest('.order-row');
    const selectedOption = select.options[select.selectedIndex];
    const maxQuantity = selectedOption.getAttribute('data-quantity');

    const quantityInput = select.closest('.order-row').querySelector('.order-quantity');
    if (quantityInput) {
        quantityInput.max = maxQuantity;
    }
    row.querySelector('.order-price').value = price;
    calculateTotal();
    disableSelectedOptions();
}

function calculateTotal() {
    let total = 0;
    document.querySelectorAll('.order-row').forEach(row => {
        const qty = parseFloat(row.querySelector('.order-quantity').value) || 0;
        const price = parseFloat(row.querySelector('.order-price').value) || 0;
        total += qty * price;
    });
    document.getElementById('total').value = "Итого: " + total;
}


let productIndex = 1;

function addProduct() {
    const container = document.getElementById('orders-container');
    const firstRow = container.querySelector('.order-row');
    const newRow = firstRow.cloneNode(true);

    productIndex += 1;

    const select = newRow.querySelector('.product-select');
    select.name = 'product_id_' + productIndex;
    select.value = "";

    const quantity = newRow.querySelector('.order-quantity');
    quantity.name = 'quantity_' + productIndex;
    quantity.value = "";

    container.appendChild(newRow);
    disableSelectedOptions();
}

function disableSelectedOptions() {
    const allSelectedValues = Array.from(document.querySelectorAll('.product-select'))
        .map(select => select.value)
        .filter(val => val !== "");

    document.querySelectorAll('.product-select').forEach(select => {
        Array.from(select.options).forEach(option => {
            if (option.value && allSelectedValues.includes(option.value) && option.value !== select.value) {
                option.disabled = true;
            } else {
                option.disabled = false;
            }
        });
    });
}

function removeRow(button) {
    const container = document.getElementById('orders-container');
    if (container.children.length > 1) {
        button.closest('.order-row').remove();
        calculateTotal();
        disableSelectedOptions();
    }
}

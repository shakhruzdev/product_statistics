document.querySelector('.add-btn').addEventListener('click', function () {
    document.getElementById('addProductModal').style.display = 'block';
});

document.querySelector('.close').addEventListener('click', function () {
    document.getElementById('addProductModal').style.display = 'none';
});

window.onclick = function (event) {
    let modal = document.getElementById('addProductModal');
    if (event.target === modal) {
        modal.style.display = 'none';
    }
};

function openDeleteModal(button) {
    const productId = button.getAttribute('data-product-id');
    const productName = button.getAttribute('data-product-name');
    document.getElementById('deleteText').textContent = `Are you sure you want to delete ${productName}?`;
    const form = document.getElementById('deleteForm');
    form.action = `${window.location.origin}/product/delete/${productId}/`;
    document.getElementById('deleteModal').style.display = 'flex';
}

function closeDeleteModal() {
    document.getElementById('deleteModal').style.display = 'none';
}
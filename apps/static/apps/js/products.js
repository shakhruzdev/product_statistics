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
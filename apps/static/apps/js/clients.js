function openModal() {
    document.getElementById("modal").style.display = "block";
}

function closeModal() {
    document.getElementById("modal").style.display = "none";
}

document.getElementById("clientForm").addEventListener("submit", function (e) {
    const name = e.target.name.value;
    const phone = e.target.phone.value;
    console.log("Новый клиент:", name, phone);
    closeModal();
});

const phoneInput = document.getElementById("phone_number");
const errorSpan = document.getElementById("phone-error");

phoneInput.addEventListener("focus", () => {
    if (!phoneInput.value.startsWith("+7")) {
        phoneInput.value = "+7";
    }
});

phoneInput.addEventListener("input", () => {
    if (!phoneInput.value.startsWith("+7")) {
        phoneInput.value = "+7" + phoneInput.value.replace(/[^0-9]/g, "").slice(0, 10);
    } else {
        phoneInput.value = "+7" + phoneInput.value.slice(2).replace(/[^0-9]/g, "").slice(0, 10);
    }

    const prefix = phoneInput.value.slice(2, 5);
    const allowedPrefixes = ["701", "702", "707", "708", "747", "775", "776", "777", "778"];
    if (phoneInput.value.length === 12 && !allowedPrefixes.includes(prefix)) {
        errorSpan.textContent = "Номер должен начинаться с допустимого кода Казахстана (например, 707, 778)";
    } else {
        errorSpan.textContent = "";
    }
});

function openDeleteModal(button) {
    const clientId = button.getAttribute('data-client-id');
    const clientName = button.getAttribute('data-client-name');
    document.getElementById('deleteText').textContent = `Are you sure you want to delete ${clientName}?`;
    const form = document.getElementById('deleteForm');
    form.action = `/clients/delete/${clientId}/`;
    document.getElementById('deleteModal').style.display = 'flex';
}

function closeDeleteModal() {
    document.getElementById('deleteModal').style.display = 'none';
}

function openUpdateModal(button) {
    const modal = document.getElementById("updateModal");
    const name = button.getAttribute("data-client-name");
    const phone = button.getAttribute("data-client-phone");
    const updateUrl = button.getAttribute("data-update-url");

    document.getElementById("full_name").value = name;
    document.getElementById("phone_number").value = phone;

    const form = document.getElementById("updateForm");
    form.action = updateUrl;

    modal.style.display = "block";
}

function closeUpdateModal() {
    document.getElementById("updateModal").style.display = "none";
}

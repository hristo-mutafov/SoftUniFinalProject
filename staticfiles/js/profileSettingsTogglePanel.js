const errorMessages = Array.from(document.querySelectorAll('.error_message'));

const changeNamePanel = document.getElementById("change_name_panel");
const changeEmailPanel = document.getElementById("change_email_panel");
const changePasswordPanel = document.getElementById("change_password_panel");
const deleteProfilePanel = document.getElementById("delete_profile_panel");
const editCityPanel = document.getElementById('edit_city_panel');
const editAddressPanel = document.getElementById('edit_address_panel');
const editPhoneNumberPanel = document.getElementById('edit_phone_number_panel');
const main = document.getElementById("main");

function showDeletePanel() {
    deleteProfilePanel.classList.add("active");
    main.classList.add("active");
}

function showNamePanel() {
    changeNamePanel.classList.add("active");
    main.classList.add("active");
}

function showEmailPanel() {
    changeEmailPanel.classList.add("active");
    main.classList.add("active");
}

function showPasswordPanel() {
    changePasswordPanel.classList.add("active");
    main.classList.add("active");
}

function showCityPanel() {
    editCityPanel.classList.add('active');
    main.classList.add('active');
}

function showAddressPanel() {
    editAddressPanel.classList.add('active');
    main.classList.add('active');
}

function showPhoneNumberPanel() {
    editPhoneNumberPanel.classList.add('active');
    main.classList.add('active');
}

function closePanel(event) {
    event.target.parentNode.classList.remove("active");
    main.classList.remove("active");
    errorMessages.forEach(x => {
        x.style.display = 'none';
    })
}



const mapper = {
    changeName: BASE_URL + 'profile/update_name/',
    changeEmail: BASE_URL + 'profile/update_email/',
    changePassword: BASE_URL + 'profile/change_password/',
    changeCity: BASE_URL + 'profile/update_city/',
    changeAddress: BASE_URL + 'profile/update_address/',
    changePhoneNumber: BASE_URL + 'profile/update_phone_number/',
}


async function changeHandler(event, form) {
    event.preventDefault();

    const errorField = event.target.childNodes[1];

    const rawFormData = new FormData(event.target);
    const formData = Object.fromEntries(rawFormData.entries());

    const fRes = await fetch(mapper[form], {
        method: 'POST',
        headers: {
            'content-type': 'application/json',
            'X-CSRFToken': CSRF_TOKEN
        },
        body: JSON.stringify(formData)

    })

    if (fRes.status === 200) {
        return location.reload();
    }

    const jsonRes = await fRes.json();

    errorField.textContent = jsonRes.message;
    errorField.style.display = "block";
}


const mapper = {
    changeName: 'update_name/',
    changeEmail: 'update_email/',
    changePassword: 'change_password/',

    changeCity: 'update_city/',
    changeAddress: 'update_address/',
    changePhoneNumber: 'update_phone_number/',
}


async function changeHandler(event, form) {
    event.preventDefault();

    const errorField = event.target.childNodes[1];

    const rawFormData = new FormData(event.target);
    const formData = Object.fromEntries(rawFormData.entries());

    const fRes = await fetch(mapper[form], {
        method: 'POST',
        headers: {
            'content-type': 'text/html',
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
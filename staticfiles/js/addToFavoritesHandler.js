async function addToFavorites(e, id) {
    e.stopPropagation();
    const url = `../../favorites/add/${id}/`;

    try {
        const fRes = await fetch(url, {
            method: 'POST',
            headers: {
                'content-type': 'application/json',
                'X-CSRFToken': CSRF_TOKEN
            },
            credentials: 'include'
        })
        if (fRes.status === 403) {
            window.location.href ='/auth/register';
        }

        if (fRes.status === 200) {
            const icon = document.getElementById('icon')

            if (e.target.tagName === 'I') {
                if (e.target.classList.value === 'far fa-heart') {
                    e.target.classList = 'fas fa-heart';
                } else {
                    e.target.classList = 'far fa-heart';
                }
            } else {
                if (icon.classList.value === 'far fa-heart') {
                    icon.classList = 'fas fa-heart';
                } else {
                    icon.classList = 'far fa-heart';
                }
            }



        }
    } catch (err) {
        console.log(`error - ${err}`);
    }
}
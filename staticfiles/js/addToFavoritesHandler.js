async function addToFavorites(e, id) {
    e.stopPropagation();
    const url = BASE_URL + `/favorites/add/${id}/`;

    try {
        const fRes = await fetch(url, {
            method: 'POST',
            headers: {
                'X-Requested-With': 'XMLHttpRequest',
                'X-CSRFToken': CSRF_TOKEN
            }
        })
        if (fRes.status === 403) {
            window.location.href ='/auth/register';
        }

        if (fRes.status === 200) {
            if (e.target.classList.value === 'far fa-heart') {
                e.target.classList = 'fas fa-heart';
            } else {
                e.target.classList = 'far fa-heart';
            }
        }
    } catch (err) {
        console.log(`error - ${err}`);
    }
}
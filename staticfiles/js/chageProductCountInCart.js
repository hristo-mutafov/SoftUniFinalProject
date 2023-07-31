
async function requester(url) {
    const fRes = await fetch(url, {
        method: 'POST',
        headers: {
            'X-CSRFToken': CSRF_TOKEN
        },
    })

    if (fRes.status === 400) {
        throw new Error
    }

    return await fRes.json();
}


function getPricesFields(e) {
    const tdWrapper = e.target.parentNode.parentNode.parentNode.nextElementSibling
    const countWrapper = e.target.parentNode.parentNode

    const count = countWrapper.querySelector('.product_count')
    const currentBigPrice = tdWrapper.querySelector('#bigPrice')
    const currentSmallPrice = tdWrapper.querySelector('#smallPrice')
    const globalPrice = document.querySelector('#headerPrice.list_item')

    return {
        count,

        currentBigPrice,
        currentSmallPrice,
        globalPrice
    }
}

function increaseCount(e, id) {

    const fields = getPricesFields(e);

    fields.count.textContent = Number(fields.count.textContent) + 1;

    requester(`edit_quantity/${id}/?action=increase`)
        .then(res => {
            const price = res.price;

            const bigPriceSum = Number(fields.currentBigPrice.textContent) + Number(price.split('.')[0]);
            const smallPriceSum = Number(fields.currentSmallPrice.textContent) + Number(price.split('.')[1]);

            fields.currentBigPrice.textContent = bigPriceSum;
            fields.currentSmallPrice.textContent = smallPriceSum.toString().padStart(2, '0');
            fields.globalPrice.textContent = (Number(fields.globalPrice.textContent) + Number(price)).toFixed(2)
        })
        .catch((err) => {
            fields.count.textContent = Number(fields.count.textContent) - 1;
        })
}


function decreaseCount(e, id) {
    const fields = getPricesFields(e)

    if (Number(fields.count.textContent) > 1) {
        fields.count.textContent = Number(fields.count.textContent) - 1;

        requester(`edit_quantity/${id}/?action=decrease`)
        .then(res => {
            const price = res.price;

            const bigPriceSum = Number(fields.currentBigPrice.textContent) - Number(price.split('.')[0]);
            const smallPriceSum = Number(fields.currentSmallPrice.textContent) - Number(price.split('.')[1]);

            fields.currentBigPrice.textContent = bigPriceSum;
            fields.currentSmallPrice.textContent = smallPriceSum.toString().padStart(2, '0');
            fields.globalPrice.textContent = (Number(fields.globalPrice.textContent) - Number(price)).toFixed(2)
        })
        .catch((err) => {
            console.log(err)
        })
    }

}
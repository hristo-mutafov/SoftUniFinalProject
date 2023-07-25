const priceWrapper = document.querySelector('#cardInfoWrapper.data')


const withStripeButton = document.querySelector("#id_payment_method_1")
const toAddressButton = document.querySelector("#id_payment_method_0")

withStripeButton.addEventListener('click', (e) => {
    if (e.target.checked) {
        priceWrapper.style.display = 'block'
    }
})

toAddressButton.addEventListener('click', (e) => {
    if (e.target.checked) {
        priceWrapper.style.display = 'none'
    }
})



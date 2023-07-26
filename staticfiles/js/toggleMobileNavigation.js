const mobileButton = document.getElementById('mobile-menu')
const navWrapper = document.querySelector('.header .wrapper.mobile')

mobileButton.addEventListener('click', () => {
    if (!navWrapper.style.display || navWrapper.style.display === 'none') {
        navWrapper.style.display = 'flex'

    } else {
        navWrapper.style.display = 'none'
    }
    mobileButton.classList.toggle('active')
})
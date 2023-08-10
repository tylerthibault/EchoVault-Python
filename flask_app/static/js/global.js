const allCloseBtns = document.querySelectorAll('.close-btn')

allCloseBtns.forEach(btn => {
    btn.addEventListener('click', () => {

        target = btn.getAttribute('target')
        targetEl = document.querySelector(`.${target}`)
        targetEl.remove()
    })
});
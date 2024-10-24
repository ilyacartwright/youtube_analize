import '../scss/styles.scss'

import $ from 'jquery'

$(document).ready(() => {
    $('.burger_menu').on('click', () => {
        $('.burger_menu').toggleClass('active');
        $('.menu-list').toggleClass('active');
    })
})
function showFormSection() {
    var busmiles = document.getElementById('weeklybus').value;
    const busmode = document.getElementById('busmodeform');
    const section_bus = document.getElementById('bus');
    const section_light = document.getElementById('light');
    const section_heavy = document.getElementById('heavy');

    if (busmiles != "" && parseInt(busmiles) != 0) {
        busmode.style.visibility = 'visible';
        busmode.style.fontSize = '16px';

        section_bus.setAttribute('required', "");
        section_light.setAttribute('required', "");
        section_heavy.setAttribute('required', "");
    } else if (busmiles == "") {
        busmode.style.visibility = 'hidden';
        busmode.style.fontSize = '3px';

        section_bus.removeAttribute('required', "");
        section_light.removeAttribute('required', "");
        section_heavy.removeAttribute('required', "");
    }
}

window.addEventListener('input', showFormSection);
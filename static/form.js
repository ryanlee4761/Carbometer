function showFormSection() {
    var busmiles = document.getElementById('weeklybus').value;
    const busmode = document.getElementById('busmodeform');
    if (busmiles != "" && parseInt(busmiles) != 0) {
        busmode.style.visibility = 'visible';
        busmode.style.fontSize = '16px';
    } else if (busmiles == "") {
        busmode.style.visibility = 'hidden';
        busmode.style.fontSize = '3px';
    }
}

window.addEventListener('input', showFormSection);
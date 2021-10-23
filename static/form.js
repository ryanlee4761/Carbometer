function showFormSection() {
    var busmiles = document.getElementById('weeklybus').value;
    const busmode = document.getElementById('busmodeform');
    if (busmiles != "" && busmiles != "0") {
        busmode.style.visibility = 'visible';
    } else if (busmiles == "") {
        busmode.style.visibility = 'hidden';
    }
}

window.addEventListener('input', showFormSection);
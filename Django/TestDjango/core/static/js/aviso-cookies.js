const botonAceptar = document.getElementById('btn-aceptar-cookies');
const avisoCookies = document.getElementById('aviso-cookies');
const fondoCookies = document.getElementById('fondo-aviso-cookies');

// Verifica si el usuario ya aceptó las cookies anteriormente
if (!localStorage.getItem('cookies-aceptadas')) {
    avisoCookies.classList.add('visible');
    fondoCookies.classList.add('visible');
} else {
    // Si las cookies ya fueron aceptadas, puedes incluir aquí código adicional
    // Por ejemplo, inicializar scripts que dependen de la aceptación de cookies.
}

botonAceptar.addEventListener('click', () => {
    // Ocultar el aviso de cookies
    avisoCookies.classList.remove('visible');
    fondoCookies.classList.remove('visible');
    
    // Guardar en localStorage la aceptación de cookies
    localStorage.setItem('cookies-aceptadas', 'true');
    // Recargar la página para reflejar los cambios
    window.location.reload();
    
    // También establecer la cookie en el navegador para indicar que se aceptaron las cookies
    document.cookie = 'cookies-aceptadas=true; expires=Wed, 01 Jan 2030 00:00:00 GMT; path=/';
});
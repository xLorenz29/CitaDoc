window.onload = function() {
    var flashMessage = document.getElementById("flash-message");
    if (flashMessage) {
        setTimeout(function() {
            // Eliminar el mensaje completamente después de 3 segundos
            flashMessage.parentNode.removeChild(flashMessage);
        }, 3000); // 3000ms = 3 segundos
    }
};

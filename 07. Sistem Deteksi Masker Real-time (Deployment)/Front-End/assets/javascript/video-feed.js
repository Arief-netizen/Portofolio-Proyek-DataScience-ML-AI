var videoContainer = document.getElementById("video-container");
var toggleButton = document.getElementById("toggle-button");
var buttonContainer = document.getElementById("button-container");
var isDetecting = false;

    toggleButton.onclick = function() {
        if (isDetecting) {
            videoContainer.style.display = "none";
            toggleButton.innerText = "Mulai Deteksi";
            toggleButton.classList.remove("btn-danger");
            buttonContainer.style.marginTop = "200px";
            buttonContainer.style.marginBottom = "200px";
            toggleButton.style.padding = "30px"
            isDetecting = false;
        } else {
            videoContainer.style.display = "block";
            toggleButton.innerText = "Stop Deteksi";
            toggleButton.classList.add("btn-danger");
            buttonContainer.style.marginTop = "20px";
            buttonContainer.style.marginBottom = "20px";
            toggleButton.style.padding = "10px"
            isDetecting = true;
        }
    };


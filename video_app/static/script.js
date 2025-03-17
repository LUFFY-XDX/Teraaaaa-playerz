document.addEventListener("DOMContentLoaded", function () {
    let savedLink = localStorage.getItem("videoLink");

    if (savedLink) {
        document.getElementById("linkInput").value = savedLink;
        document.getElementById("videoFrame").src = `/generate/?link=${encodeURIComponent(savedLink)}`;
    }
});

function generateLink() {
    let linkInput = document.getElementById("linkInput").value;

    fetch(`/generate/?link=${encodeURIComponent(linkInput)}`)
    .then(response => response.json())
    .then(data => {
        if (data.direct_link) {
            document.getElementById("videoFrame").src = data.direct_link;
            localStorage.setItem("videoLink", linkInput);  
            window.history.pushState({}, "", `/?link=${encodeURIComponent(linkInput)}`);
        } else {
            alert("Invalid link!");
        }
    })
    .catch(error => console.error("Error:", error));
}

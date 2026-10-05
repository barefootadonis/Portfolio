const form = document.getElementById("contact-form");
const successMessage = document.getElementById("success-message");

if (form) {

    form.addEventListener("submit", async function(event) {

        event.preventDefault();

        const response = await fetch(form.action, {
            method: "POST",
            body: new FormData(form),
            headers: {
                "Accept": "application/json"
            }
        });

        if (response.ok) {

            form.style.display = "none";
            successMessage.style.display = "block";

            setTimeout(function() {
                form.reset();
                form.style.display = "flex";
                successMessage.style.display = "none";
            }, 5000);

        } else {

            alert("Something went wrong. Please try again.");

        }

    });

}
document.addEventListener("DOMContentLoaded", () => {
    const form = document.querySelector("form");
    const input = document.querySelector("input");
    const ul = document.querySelector("ul");

    form.addEventListener("submit", async (e) => {
        e.preventDefault();

        const tarea = input.value;

        const res = await fetch("/agregar", {
            method: "POST",
            headers: {
                "Content-Type": "application/x-www-form-urlencoded"
            },
            body: `tarea=${tarea}`
        });

        if (res.ok) {
            const li = document.createElement("li");
            li.textContent = tarea;
            ul.appendChild(li);
            input.value = "";
        }
    });
});

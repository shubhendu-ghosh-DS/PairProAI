function generateSolution() {
    let code = document.getElementById("codeInput").value;
    let option = document.getElementById("optionSelect").value;

    fetch("/generate", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ code: code, option: option })
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById("outputCode").innerText = data.code;
        document.getElementById("outputExplanation").innerText = data.explanation;
    })
    .catch(error => console.error("Error:", error));
}

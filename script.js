async function analyzeNews() {
    let newsText = document.getElementById("newsInput").value;
    let resultDiv = document.getElementById("result");

    if (newsText.trim() === "") {
        alert("Please enter some text!");
        return;
    }

    // Show loading message
    resultDiv.innerText = "🔍 Analyzing...";

    try {
        let response = await fetch("http://127.0.0.1:5000/predict", {  // Local API
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ text: newsText })
        });

        let data = await response.json();
        resultDiv.innerText = data.prediction === "Fake" ? "🚨 Fake News!" : "✅ Real News!";
    } catch (error) {
        resultDiv.innerText = "❌ Error connecting to the server!";
    }
}

function clearText() {
    document.getElementById("newsInput").value = "";
    document.getElementById("result").innerText = "";
}

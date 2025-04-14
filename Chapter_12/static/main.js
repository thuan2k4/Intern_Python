async function predict() {
    const feature = parseFloat(document.getElementById("feature").value);
    const response = await fetch("/predict", {
        headers: {
            "Content-Type": "application/json",
        },
        method: "POST",
        body: JSON.stringify({
            feature: feature,
        }),
    });
    const data = await response.json();
    document.getElementById("result").value = data.prediction;
}

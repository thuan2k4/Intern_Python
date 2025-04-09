async function math(operator) {
    try {
        const num1 = parseFloat(document.getElementById("number1").value);
        const num2 = parseFloat(document.getElementById("number2").value);

        if (isNaN(num1) || isNaN(num2)) {
            alert('Please enter valid numbers');
            return;
        }

        const response = await fetch(`/api/v1/math`, {
            headers: {
                'Content-Type': 'application/json'
            },
            method: "POST",
            body: JSON.stringify({
                number1: num1,
                number2: num2,
                operation: operator
            })
        })
        const data = await response.json();
        console.log(data);
        document.getElementById("result").innerHTML = data;
    }
    catch (error) {
        console.log(`Error: ${error}`);
        alert('An error occurred while calculating');
    }
}
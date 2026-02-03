/**
 * Merge punctuation from input into output.
 * Replaces any control characters in output (\u0001, etc.)
 * with the corresponding punctuation from input.
 *
 * @param {string} input - original text entered by user
 * @param {string} output - diacritized text returned by server
 * @returns {string} - output with punctuation restored
 */
function mergeInputPunctuation(input, output) {
    const controlCharRegex = /[\u0000-\u001F]/g; // matches SOH, STX, etc.

    let result = '';
    let inputIndex = 0;

    for (let i = 0; i < output.length; i++) {
        const char = output[i];

        if (controlCharRegex.test(char)) {
            // Find next punctuation in input
            while (inputIndex < input.length && !/[^\w\s\u0621-\u064A]/.test(input[inputIndex])) {
                inputIndex++;
            }

            // Use punctuation from input if exists, else fallback to '!'
            if (inputIndex < input.length) {
                result += input[inputIndex];
                inputIndex++;
            } else {
                result += '!'; // fallback
            }
        } else {
            result += char;

            // Skip non-punctuation in input
            if (inputIndex < input.length && input[inputIndex] === char) {
                inputIndex++;
            }
        }
    }

    return result;
}


document.getElementById("diacritizeBtn").addEventListener("click", async () => {
    const inputText = document.getElementById("inputText").value;

    if (!inputText.trim()) {
        alert("يرجى إدخال نص!");
        return;
    }

    const formData = new FormData();
    formData.append("text", inputText);

    try {
        const response = await fetch("/diacritize", {
            method: "POST",
            body: formData
        });

        if (!response.ok) throw new Error("Network response was not OK");

        const data = await response.json();

        // Merge input punctuation into the output
        const fixedText = mergeInputPunctuation(inputText, data.result);

        document.getElementById("resultText").textContent = fixedText;

    } catch (err) {
        console.error(err);
        alert("حدث خطأ أثناء المعالجة!");
    }
});


// Copy button functionality
const copyBtn = document.getElementById('copyBtn');
const resultText = document.getElementById('resultText');

copyBtn.addEventListener('click', () => {
    const text = resultText.innerText;
    if (text.trim() !== "") {
        navigator.clipboard.writeText(text).then(() => {
            copyBtn.innerText = "تم النسخ!";
            setTimeout(() => copyBtn.innerText = "نسخ", 1500);
        });
    }
});

async function sendMessage() {
    const input = document.getElementById("userInput").value;
    if (!input) return;

    const chat = document.getElementById("chat");
    chat.innerHTML += `<p><b>Du:</b> ${input}</p>`;

    const response = await fetch("/ask", {   // Pfad für Vercel Serverless
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify({ question: input })
    });

    const data = await response.json();
    chat.innerHTML += `<p><b>KI:</b> ${data.answer}</p>`;
    document.getElementById("userInput").value = "";
}
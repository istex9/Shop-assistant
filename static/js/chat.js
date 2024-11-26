// static/js/chat.js

document.addEventListener('DOMContentLoaded', () => {
    const chatForm = document.getElementById('chat-form');
    const userInput = document.getElementById('user-input');
    const chatBox = document.getElementById('chat-box');

    chatForm.addEventListener('submit', async (e) => {
        e.preventDefault();
        const message = userInput.value.trim();
        if (message === '') return;

        appendMessage('user', message);
        userInput.value = '';
        chatBox.scrollTop = chatBox.scrollHeight;

        try {
            const response = await fetch('/chat', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ message: message })
            });

            if (!response.ok) {
                throw new Error(`Hiba történt: ${response.statusText}`);
            }

            const data = await response.json();
            if (data.error) {
                appendMessage('bot', `Hiba: ${data.error}`);
            } else {
                const formattedResponse = formatResponse(data.response);
                appendMessage('bot', formattedResponse);
            }
        } catch (error) {
            appendMessage('bot', `Hiba: ${error.message}`);
        }

        chatBox.scrollTop = chatBox.scrollHeight;
    });

    function appendMessage(sender, message) {
        const messageDiv = document.createElement('div');
        messageDiv.classList.add('chat-message', sender);

        const messageContent = document.createElement('div');
        messageContent.classList.add('message-content');

        if (sender === 'bot') {
            messageContent.innerHTML = formatResponse(message);
        } else {
            messageContent.textContent = message;
        }

        messageDiv.appendChild(messageContent);
        chatBox.appendChild(messageDiv);
    }

    function formatResponse(message) {
        let formatted = message;

        // Kötőjel alapú listák új sorokkal
        formatted = formatted.replace(/-\s+/g, '<br>- ');

        // Számozott listák új sorokkal
        formatted = formatted.replace(/(\d+)\.\s+/g, '<br>$1. ');

        // Egyéb formázások (pl. e-mail címek linkként)
        formatted = formatted.replace(/\[([^\]]+)\]\(([^)]+)\)/g, '<a href="$2">$1</a>');

        return formatted;
    }
});

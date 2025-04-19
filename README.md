# LiveHealthy Customer Support Assistant

Welcome to the **LiveHealthy Customer Support Assistant**, a simple yet effective command-line chatbot built with Python and the Groq API. This assistant helps simulate a customer service interaction for a fictional health-focused company called **LiveHealthy**.

## 🏢 About LiveHealthy
LiveHealthy is a company that sells **healthy, nutritious, and affordable** food items. Its target audience is **health-conscious individuals** who want reliable, polite, and professional support when they need help.

## 💬 What This Project Does

This assistant:
- Presents users with a menu of support topics: **Complaints**, **Inquiries**, or **Feedback**
- Uses the **Groq API (LLaMA-3.3-70B)** to generate dynamic, natural-sounding responses
- Maintains conversation flow for multi-turn dialogue
- Allows switching between menu items or exiting gracefully
- Logs all interactions in a `.txt` file for audit or training purposes

## 🚀 Getting Started

### Prerequisites
Make sure you have the following:
- Python 3.8+
- A Groq API key
- A `.env` file with your `GROQ_API_KEY` set

### Install dependencies
```bash
pip install groq python-dotenv
```

### Set up your .env file
```
GROQ_API_KEY=your_groq_api_key_here
```

### Run the assistant
```bash
python try.py
```

## 🧠 Features

- **Multi-turn conversation**: The assistant keeps the conversation going until the user wants to switch topics or exit.
- **Context-aware responses**: Responses are tailored based on the selected topic (Complaints, Inquiries, or Feedback).
- **Error handling**: Invalid input is handled gracefully.
- **Logging**: All conversations are logged in `livehealthy_support_log.txt`.

## 📁 File Structure

```
.
├── try.py                   # Main chatbot logic
├── .env                    # Environment variables (not committed)
├── livehealthy_support_log.txt  # Log of all conversations
├── README_LiveHealthy_Assistant.md # This README file
```

## 💡 Possible Improvements
- Add a GUI for more visual interaction
- Integrate with a database to track orders or user details
- Add context memory for more intelligent conversations
- Include sentiment analysis to prioritize angry customers

## 🤝 Contributing
Feel free to fork the repo and suggest improvements! Whether it's UI, logging, smarter prompts, or general cleanup — contributions are welcome.

## 📜 License
MIT License

---

Built with ❤️ by Khadijah Agboola

# Healthcare_Assistant_Chatbot

# 🩺 Health Care Assistant Chatbot

A conversational AI-powered assistant designed to provide **accurate, user-friendly, and medically relevant answers**. This project combines a **domain-specific fine-tuned model** (using TinyLlama + LoRA) with a **general-purpose LLM**, and blends their responses via a third LLM to provide a final enhanced answer.

---

## 📸 Demo Output

![Healthcare Assistant Chatbot UI](./9bf8d8d1-780b-4df3-a848-b591b65a18e8.jpg)

---

## 💡 Key Features

- 🧠 **Dual Model Inference**:
  - A fine-tuned medical model (`TinyLlama-1.1B-Chat` with LoRA)
  - A general-purpose LLM (via LangChain agents or Gemini/Groq)

- 🔗 **Response Fusion**:
  - Uses a third LLM to combine outputs from both models.
  - Prioritizes medical accuracy and human-readable responses.

- 🖥️ **Streamlit Frontend**:
  - Chat-style UI for interacting with the assistant.
  - Session memory support via `st.session_state`.

- ⚙️ **LangChain Agent Integration**:
  - Uses tools like `Wikipedia` and `Arxiv` via LangChain for general lookup (via `agent_making.py`).

---

## 🏗️ Project Structure


# LangGraph AI Chatbot

A **FastAPI-based AI chatbot** powered by **LangGraph**, **Groq models**, and **Tavily Search**, with a **Streamlit frontend** for user interaction. The application is **Dockerized** and deployed on **AWS ECS** for scalability.

## 🚀 Features

- **Multi-Agent AI Chatbot**: Uses LangGraph for ReAct-style agent interactions.
- **Supports Groq Models**: Choose between `Deepseek-r1-distill-llama-70b` and `Llama3-70b-8192`.
- **Integrated Web Search**: Uses Tavily Search API for fetching real-time information.
- **FastAPI Backend**: Provides a robust and scalable REST API.
- **Streamlit Frontend**: User-friendly UI for chatbot interaction.
- **Dockerized Deployment**: Runs in a containerized environment for easy deployment.
- **AWS ECS Hosting**: Scalable cloud deployment with potential for load balancing.

---

## 🛠️ Installation & Setup

### **1️⃣ Clone the Repository**
```bash
git clone https://github.com/yourusername/langgraph-ai-chatbot.git
cd langgraph-ai-chatbot
```

2️⃣ **Create a Virtual Environment (Optional but Recommended)**
```bash
python -m venv venv
venv\Scripts\activate
```

3️⃣ **Install Dependencies**
```bash
pip install -r requirements.txt
```

4️⃣ **Set Up API Keys**

Create a .env file in the root directory and add the following environment variables:

```bash
GROQ_API_KEY="Your Groq API Key"
TAVILY_API_KEY="Your Tavily API Key"
```

5️⃣ **Run the Application Locally**

**(You can adjust the ports accordingly, here the port for FastAPI Backend is:8000 and port for Streamlit frontend is:8501)**

Start FastAPI Backend 
```bash
uvicorn app:app --host 127.0.0.1 --port 8000 --reload
```

Start Streamlit Frontend
```bash
streamlit run ui.py --server.port 8501
```

Once running:
- Backend API: http://127.0.0.1:8000/docs
- Frontend UI: http://127.0.0.1:8501

---

## 🐳 Docker Setup

1️⃣ **Build Docker Image**
```bash
docker build -t langgraph-ai-chatbot .
```

2️⃣ **Run Docker Container**
```bash
docker run -d -p 8000:8000 -p 8501:8501 --name langgraph-ai-chatbot-container langgraph-ai-chatbot
```

3️⃣ **Push to DockerHub**
```bash
docker tag langgraph-agent-app your_dockerhub_username/langgraph-ai-chatbot:latest
docker push your_dockerhub_username/langgraph-agent-app:latest
```

---

## 🌐 Deployment on AWS

- Create an ECS Cluster.
- Define a Task Definition using the Docker image.
- Configure a Service with an Application Load Balancer (for scalability).
- Deploy and access via the assigned public URL.

---

## 📌 API Endpoints

**Chat with the AI Agent**

POST /chat

**Request Body**
```bash
{
  "model_name": "Llama3-70b-8192",
  "system_prompt": "You are a helpful AI assistant.",
  "messages": ["What is the capital of France?"]
}
```

**Response**
```bash
{
  "status": "success",
  "response": [
    {"type": "ai", "content": "The capital of France is Paris."}
  ],
  "metadata": {"model": "Llama3-70b-8192"}
}
```

---

## 🏗️ Tech Stack

- **Python**
- **FastAPI**
- **Streamlit**
- **LangGraph**
- **Groq API**
- **Tavily Search Tool**
- **Docker**
- **AWS**

## 🤝 Contributing
**Contributions are welcome! Feel free to open an issue or submit a pull request.**

---

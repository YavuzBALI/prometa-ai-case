# CHAT INTENT ANALYZE PROJECT

## 📌 Project Information

This project analyzes dialogues between a customer and a sales representative. The system processes each sentence in the conversation to determine:

- **User intent** (e.g., inquiry, purchase intention, complaint, greeting, package change, renewal, etc.)
- **Sentiment** (positive, neutral, or negative)

All analysis results are **asynchronously logged** and streamed to the **user interface in real time**, providing a smooth and interactive experience. The system is designed to handle live conversational data and deliver immediate feedback with high responsiveness.

## 📁 Project Structure
```
project-root/
├── docker-compose        # Service docker up direction                            
├── intent_service        # intent service root direction                                              
├── ui-service            # ui service root direction
├── log-service           # log service root direction
├── .gitignore                
└── README.md                             
```

## 💻 Usage

To run the project:
1. First you need to clone the project from the repo.
```bash
   git clone [HTTPS URL]
   cd prometa_ai_case
   ```
2. In the configurations in `intent_service`, you need to enter the API Key to benefit from the LLM API.
```
project-root/                          
└──  intent_service        # intent service root direction
│   └── config             # configuration direction
│   │   └── config.yaml    # configuration file
```

3. Finally, you can remove the services with Docker Compose in the project file.
```bash
   docker-compose up --build
   ```
4. For the interface, simply enter the URL into your browser: [Open Streamlit Interface](http://localhost:8502/)


## ⚙️ Requirements

- Python 3.9

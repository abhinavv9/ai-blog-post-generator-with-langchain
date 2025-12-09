# AI Blog Post Generator with LangChain

This project demonstrates how to build an AI-powered blog post generator using LangChain and OpenAI.

## Features

- Generates blog post titles and content based on user-provided topics.
- Leverages LangChain for orchestrating AI workflows.
- Integrates with OpenAI's language models.
- Securely manages API keys using environment variables.

## Prerequisites

- Python 3.7+
- An OpenAI API key
- Familiarity with virtual environments

## Setup

1. **Clone the repository:**
   ```bash
   git clone <repository-url>
   cd ai-blog-post-generator-with-langchain
   ```

2. **Create and activate a virtual environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure environment variables:**
   Create a `.env` file in the root directory and add your OpenAI API key:
   ```
   OPENAI_API_KEY=your_openai_api_key_here
   ```

## Running the Application

Execute the `main.py` script:

```bash
python src/main.py
```

The application will generate a blog post about "The Future of Artificial Intelligence" and print it to the console.

## Project Structure

```
.env
requirements.txt
src/
  main.py
```

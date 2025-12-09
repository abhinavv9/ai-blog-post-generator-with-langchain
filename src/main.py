import os
from dotenv import load_dotenv
from langchain.chat_models import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from langchain.schema import SystemMessage, HumanMessage

# Load environment variables from .env file
load_dotenv()

# Initialize the OpenAI chat model
# temperature: Controls randomness. Lower values make output more focused and deterministic.
# max_tokens: The maximum number of tokens to generate in the completion.
llm = ChatOpenAI(temperature=0.7, max_tokens=1000)

# Define the prompt template for generating blog post titles
# This template uses placeholders for the user's topic and keywords.
title_template = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant that generates creative and engaging blog post titles."),
    ("human", "Generate a blog post title about: {topic}. Include keywords like: {keywords}.")
])

# Define the prompt template for generating blog post content
# This template guides the AI to create a blog post with a specific structure.
content_template = ChatPromptTemplate.from_messages([
    ("system", "You are a skilled content writer that produces informative and engaging blog posts."),
    ("human", "Write a blog post about: {topic}. The title is: {title}. Ensure the content is well-structured and covers the following aspects: {sections}.")
])

def generate_blog_post(topic: str, keywords: str, sections: str) -> dict:
    """
    Generates a blog post based on the provided topic, keywords, and sections.

    Args:
        topic: The main subject of the blog post.
        keywords: Keywords to include in the blog post.
        sections: Specific sections or points to cover in the blog post.

    Returns:
        A dictionary containing the generated title and content of the blog post.
    """
    # Format the title prompt
    formatted_title_prompt = title_template.format_messages(topic=topic, keywords=keywords)
    # Invoke the LLM to generate the title
    generated_title_response = llm.invoke(formatted_title_prompt)
    generated_title = generated_title_response.content

    # Format the content prompt
    formatted_content_prompt = content_template.format_messages(topic=topic, title=generated_title, sections=sections)
    # Invoke the LLM to generate the content
    generated_content_response = llm.invoke(formatted_content_prompt)
    generated_content = generated_content_response.content

    return {
        "title": generated_title,
        "content": generated_content
    }

if __name__ == "__main__":
    blog_topic = "The Future of Artificial Intelligence"
    blog_keywords = "AI, machine learning, deep learning, future trends"
    blog_sections = "Introduction to AI, current applications, future predictions, ethical considerations, conclusion"

    print(f"Generating blog post for topic: '{blog_topic}'...")
    blog_post = generate_blog_post(blog_topic, blog_keywords, blog_sections)

    print("\n--- Generated Blog Post ---")
    print(f"Title: {blog_post['title']}")
    print("\nContent:")
    print(blog_post['content'])
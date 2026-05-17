import os
from playwright.sync_api import sync_playwright
from anthropic import Anthropic
from dotenv import load_dotenv

load_dotenv()

client = Anthropic()

def analyze_page(url: str) -> str:
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto(url)
        
        title = page.title()
        content = page.inner_text("body")[:3000]
        
        browser.close()
        
    return f"Page title: {title}\n\nPage content:\n{content}"

def generate_test_cases(page_info: str) -> str:
    message = client.messages.create(
        model="claude-haiku-4-5",
        max_tokens=1024,
        messages=[
            {
                "role": "user",
                "content": f"""You are a QA automation expert. 
                Based on the following web page information, generate 5 detailed test cases.
                For each test case include:
                - Test case name
                - Description
                - Steps to reproduce
                - Expected result
                
                Page information:
                {page_info}"""
            }
        ]
    )
    return message.content[0].text

def run_agent(url: str):
    print(f"\nAnalyzing: {url}")
    print("-" * 50)
    
    print("Extracting page information...")
    page_info = analyze_page(url)
    
    print("Generating test cases with Claude AI...")
    test_cases = generate_test_cases(page_info)
    
    print("\nGenerated Test Cases:")
    print("=" * 50)
    print(test_cases)
    
    with open("reports/test_cases.md", "w") as f:
        f.write(f"# Test Cases for {url}\n\n")
        f.write(test_cases)
    
    print("\nReport saved to reports/test_cases.md")

if __name__ == "__main__":
    run_agent("https://www.saucedemo.com")
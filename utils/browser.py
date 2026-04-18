from playwright.sync_api import sync_playwright

def run_task(task):
    results = []

    # Simple demo: always search for a keyword extracted from task
    keyword = "iphone"
    if "laptop" in task.lower():
        keyword = "laptop"

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        # Open Amazon
        page.goto("https://www.amazon.in")

        # Search
        page.fill("input[name='field-keywords']", keyword)
        page.press("input[name='field-keywords']", "Enter")

        page.wait_for_timeout(3000)

        # Extract product titles
        items = page.query_selector_all("h2 span")

        for item in items[:5]:
            results.append(item.inner_text())

        browser.close()

    return results

import webbrowser
from output_module import output


def webbrowser_search(query):
    sites = [["youtube", "https://www.youtube.com"], ["wikipedia", "https://www.wikipedia.org/"], ["google", "https://www.google.com"]]
    for site in sites:
        if f"open {site[0]}".lower() in query.lower():
            output(f"Opening {site[0]} sir...")
            webbrowser.open(site[1])


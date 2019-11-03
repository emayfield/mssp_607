from wiki_api import page_text
import re

if __name__ == "__main__":
    penn_html = page_text("University of Pennsylvania", "html")

    penn_text = page_text("University of Pennsylvania", "text")

    penn_list = page_text("University of Pennsylvania", "list")
    
from langchain_community.tools.tavily_search import TavilySearchResults


# Tavily is used to connect LLM to Web
def get_profile_url_tavily(name: str):
    """Searches for LinkedIn Profile Page of a person"""
    search = TavilySearchResults()
    res = search.run(f"{name}")
    print(res)
    return res[0]["url"]

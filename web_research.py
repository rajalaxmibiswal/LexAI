from duckduckgo_search import DDGS


def search_legal_updates(query):

    context = []

    with DDGS() as ddgs:

        results = ddgs.text(
            query,
            max_results=5
        )

        for r in results:
            context.append(r["body"])

    return "\n".join(context)
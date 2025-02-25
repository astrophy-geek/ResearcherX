import streamlit as st
import arxiv 


client = arxiv.Client()

def search_arxiv(query, limit):
    search = arxiv.Search(
    query = query,
    max_results = limit,
    sort_by = arxiv.SortCriterion.SubmittedDate
    )
    results = []
    for result in search.results():
        results.append({"title": result.title, "abstract": result.summary, "authors": " ".join(str(author) for author in result.authors)})
    return results


st.set_page_config(page_title="ResearchDigest", layout="centered")

st.title("ResearchDigest")
st.write("Search for papers!")

user_input = st.text_input("Search")

st.radio("Service:", ["arXiv", "bioRxiv", "medRxiv"])

limit = st.slider("Limit results to:", 1, 100)

if st.button("Search"):
    if user_input:
        with st.spinner("Searching..."):
            papers = search_arxiv(user_input, limit)
            if papers:
                st.success(f"Found {len(papers)} papers!")
                for i, paper in enumerate(papers):
                    st.subheader(f"{i+1}. {paper['title']}")
                    st.markdown(f"**Authors:** {paper['authors']}")
                    st.markdown(f"**Abstract:** {paper['abstract']}")
            else:
                st.warning("No results.")
    else:
        st.warning("Enter a query!")


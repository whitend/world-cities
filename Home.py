import streamlit as st

st.set_page_config(page_title="Home", page_icon="🏙️")

st.title("World Cities Explorer")

st.write(
    """
    Welcome! 👋

    This multi-page app lets you explore **world cities with a population over one million**
    from a single, interactive dashboard.

    On the next page you can:

    - Filter cities by **minimum population** (in millions) with a slider
    - Filter by **capital type** (primary / admin / minor)
    - Search for a specific **country** (enter `ALL` to reset)
    - See the matching cities on a **map**, in a **table**, and as a
      **total population by country** bar chart

    Click the button below to get started.
    """
)

if st.button("Go to the World Cities app ➡️"):
    st.switch_page("pages/app.py")

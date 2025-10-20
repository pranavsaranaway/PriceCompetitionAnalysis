import streamlit as st

def render_header():
    st.title("Amazon Compeittive Analysis Tool")
    st.caption("Enter your ASIN to get product insights")

def render_inputs():
    asin = st.text_input("Enter ASIN:", placeholder="e.g., B08N5WRWNW")
    geo = st.text_input("Zip/Postal Code:", placeholder="e.g., 10001")
    domain = st.selectbox("Domain:", options=["com", "ca", "co.uk", "de", "fr", "it", "es", "in", "jp", "mx", "au"])
    return asin.strip(), geo.strip(), domain
   
def main():
    st.set_page_config(page_title="Amazon Competitive Analysis Tool", page_icon=":bar_chart:", layout="centered")
    render_header()
    asin,geo,domain = render_inputs()

    if st.button("Scrape Product") and asin:
        with st.spinner("Scraping product..."):
            st.write("Scrape")
            # TODO: scrape product
        st.success("Product scraped successfully!")

if __name__ == "__main__":
    main()
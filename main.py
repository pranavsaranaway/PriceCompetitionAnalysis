import streamlit as st
from src.oxylabs_client import scrape_procut_details

def render_header():
    st.title("Amazon Compeittive Analysis Tool")
    st.caption("Enter your ASIN to get product insights")

def render_inputs():
    asin = st.text_input("Enter ASIN:", placeholder="e.g., B08N5WRWNW")
    geo = st.text_input("Zip/Postal Code:", placeholder="e.g., 10001")
    domain = st.selectbox("Domain:", options=["com", "ca", "co.uk", "de", "fr", "it", "es", "in", "jp", "mx", "au"])
    return asin.strip(), geo.strip(), domain

def render_product_card(product):
    with st.container(border = True):
        cols = st.columns([1, 2])

        try:
            images = product.get("images", [])
            if images and len(images) > 0:
                cols[0].image(images[0], width=200)
            else:
                cols[0].write("No Image Available")
        except:
            cols[0].write("Error Loading Image")

        with cols[1]:
            st.subheader(product.get("title") or product["asin"])
            info_cols = st.columns(3)
            currency = product.get("currency", "")
            price = product.get("price", "N/A")
            info_cols[0].metric("Price", f"{currency} {price}" if currency else price)
            info_cols[1].write(f"Brand: {product.get('brand', 'N/A')}")
            info_cols[2].write(f"Product: {product.get('product', 'N/A')}")

            domain_info = f"amazon.{product.get('amazon_domain', 'com')}"
            geo_info = product.get("geo_location", "N/A")
            st.caption(f"Domain: {domain_info} | Geo: {geo_info}")

            st.write(product.get("url", ""))
            if st.button("Start analyzing competitors", key = f"analyze_{product['asin']}"):
                st.session_state['analyzing_asin'] = product['asin']
   
def main():
    st.set_page_config(page_title="Amazon Competitive Analysis Tool", page_icon=":bar_chart:", layout="centered")
    render_header()
    asin,geo,domain = render_inputs()

    if st.button("Scrape Product") and asin:
        with st.spinner("Scraping product..."):
            product = scrape_procut_details(asin, geo, domain)
        st.success("Product scraped successfully!")
        render_product_card(product)

if __name__ == "__main__":
    main()
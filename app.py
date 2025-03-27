import streamlit as st 
from visuals.emissions_and_le import co2_vs_le, hdi_vs_co2, co2_vs_hdi_percent_change

st.header("Human Development Index Analysis")
st.divider()

st.subheader("CO2 vs. Quality of Life Analysis")
c1,c2 = st.columns(2)
with c1:
    st.pyplot(co2_vs_le())
with c2:
    st.pyplot(hdi_vs_co2())

st.pyplot(co2_vs_hdi_percent_change())
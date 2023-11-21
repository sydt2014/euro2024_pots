import streamlit as st
import pandas as pd

st.set_page_config(layout="wide")

st.title("Euro 2024 Torba Simülasyonu")

col1, col2, col3 = st.columns([0.3, 0.4, 0.3])

custom_css = """
<style>
div[data-baseweb="input"] input[type="number"] {
    width: 70px;  /* İstediğiniz genişliği burada belirleyin */
}
</style>
"""

# CSS stilini uygula
st.markdown(custom_css, unsafe_allow_html=True)

with col1:
    gal, tr = st.columns([0.5, 0.5])
    gal_value = gal.number_input("🏴󠁧󠁢󠁷󠁬󠁳󠁿 Galler", min_value=0, max_value=10, step=1)
    tr_value = tr.number_input("🇹🇷 Türkiye", min_value=0, max_value=10, step=1)
    text = ''' --- '''
    st.markdown(text)
    hs5, as5 = st.columns([0.5, 0.5])
    hir_value = hs5.number_input("🇭🇷 Hırvatistan", min_value=0, max_value=10, step=1)
    erm_value = as5.number_input("🇦🇲 Ermenistan", min_value=0, max_value=10, step=1)
    st.markdown(text)
    hs8, as8 = st.columns([0.5, 0.5])
    rom_value = hs8.number_input("🇷🇴 Romanya", min_value=0, max_value=10, step=1)
    swi_value = as8.number_input("🇨🇭 İsviçre", min_value=0, max_value=10, step=1)
    st.markdown(text)
    hs9, as9 = st.columns([0.5, 0.5])
    ceb_value = hs9.number_input("🇬🇮 Cebelitarık", min_value=0, max_value=10, step=1)
    hol_value = as9.number_input("🇳🇱 Hollanda", min_value=0, max_value=10, step=1)

with col2:
    data = {
        'Rnk': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
                11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21],
        'Grp': ['J', 'B', 'A', 'F', 'C', 'G', 'D', 'H', 'E', 'I',
                'F', 'A', 'J', 'B', 'G', 'D', 'C', 'H', 'E', 'I', 'D'],
        'Team': ['Portekiz', 'Fransa', 'İspanya', 'Belçika', 'İngiltere',
                 'Macaristan', 'Türkiye', 'Danimarka', 'Arnavutluk', 'Romanya',
                 'Avusturya', 'İskoçya', 'Slovenya', 'Slovakya', 'Çekya',
                 'Hollanda', 'İtalya', 'Sırbistan', 'Hırvatistan', 'İsviçre',
                 'Galler', ],
        'P': [24, 21, 21, 20, 20, 18, 16, 16, 15, 13,
              19, 17, 16, 16, 15, 15, 14, 14, 13, 11, 11],
        'Av.': [28, 26, 20, 18, 18, 9, 7, 4, 8, 4,
                10, 9, 5, 5, 6, 4, 7, 6, 8, 8, 0],
        'Siralama': [1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
                     2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3],
    }

    ct = pd.DataFrame(data)

    # Yeni "Grp_Rnk" sütunu ekleyerek istenilen değerleri atayalım
    # ct['Siralama'] = pd.cut(ct['Rnk'], bins=[0, 10, 20, float('inf')], labels=[1, 2, 3], right=False).astype(int)

    # Türkiye
    if tr_value > gal_value:
        ct.loc[ct['Team'] == 'Türkiye', 'P'] += 3
    elif tr_value == gal_value:
        ct.loc[ct['Team'] == 'Türkiye', 'P'] += 1
    elif (tr_value < gal_value) & (erm_value < hir_value):
        ct.loc[ct['Team'] == 'Türkiye', 'Siralama'] = 2
        ct.loc[ct['Team'] == 'Hırvatistan', 'Siralama'] = 1
    else:
        ct.loc[ct['Team'] == 'Türkiye', 'P'] += 0

    # Romanya
    if rom_value > swi_value:
        ct.loc[ct['Team'] == 'Romanya', 'P'] += 3
    elif rom_value == swi_value:
        ct.loc[ct['Team'] == 'Romanya', 'P'] += 1
    elif rom_value < swi_value:
        ct.loc[ct['Team'] == 'Romanya', 'Siralama'] = 2
        ct.loc[ct['Team'] == 'İsviçre', 'Siralama'] = 1
    else:
        ct.loc[ct['Team'] == 'Romanya', 'P'] += 0

    # Hollanda
    if ceb_value < hol_value:
        ct.loc[ct['Team'] == 'Hollanda', 'P'] += 3
    elif ceb_value == hol_value:
        ct.loc[ct['Team'] == 'Hollanda', 'P'] += 1
    else:
        ct.loc[ct['Team'] == 'Hollanda', 'P'] += 0

    # Hırvatistan
    if (gal_value > tr_value) & (erm_value < hir_value):
        ct.loc[ct['Team'] == 'Türkiye', 'Siralama'] = 2
        ct.loc[ct['Team'] == 'Hırvatistan', 'Siralama'] = 1
        ct.loc[ct['Team'] == 'Hırvatistan', 'P'] += 3
    elif (hir_value > erm_value) & (gal_value <= tr_value):
        ct.loc[ct['Team'] == 'Hırvatistan', 'P'] += 3
    elif (hir_value == erm_value) & (gal_value > tr_value):
        ct.loc[ct['Team'] == 'Hırvatistan', 'P'] += 1
        ct.loc[ct['Team'] == 'Hırvatistan', 'Siralama'] = 3
        ct.loc[ct['Team'] == 'Galler', 'Siralama'] = 2
    elif (hir_value == erm_value) & (gal_value <= tr_value):
        ct.loc[ct['Team'] == 'Hırvatistan', 'P'] += 1
    else:
        ct.loc[ct['Team'] == 'Hırvatistan', 'P'] += 0

    # İsviçre
    if swi_value > rom_value:
        ct.loc[ct['Team'] == 'İsviçre', 'P'] += 3
        ct.loc[ct['Team'] == 'Romanya', 'Siralama'] = 2
        ct.loc[ct['Team'] == 'İsviçre', 'Siralama'] = 1
    elif rom_value == swi_value:
        ct.loc[ct['Team'] == 'İsviçre', 'P'] += 1
    else:
        ct.loc[ct['Team'] == 'İsviçre', 'P'] += 0

    # Galler
    if (gal_value > tr_value) & (erm_value >= hir_value):
        ct.loc[ct['Team'] == 'Galler', 'Siralama'] = 2
        ct.loc[ct['Team'] == 'Hırvatistan', 'Siralama'] = 3
        ct.loc[ct['Team'] == 'Galler', 'P'] += 3
    elif (hir_value > erm_value) & (gal_value > tr_value):
        ct.loc[ct['Team'] == 'Galler', 'P'] += 3
    elif gal_value == tr_value:
        ct.loc[ct['Team'] == 'Galler', 'P'] += 1
    else:
        ct.loc[ct['Team'] == 'Galler', 'P'] += 0

    ct.loc[ct['Team'] == 'Türkiye', 'Av.'] += tr_value - gal_value
    ct.loc[ct['Team'] == 'Galler', 'Av.'] += gal_value - tr_value
    ct.loc[ct['Team'] == 'Hırvatistan', 'Av.'] += hir_value - erm_value
    ct.loc[ct['Team'] == 'Romanya', 'Av.'] += rom_value - swi_value
    ct.loc[ct['Team'] == 'İsviçre', 'Av.'] += swi_value - rom_value
    ct.loc[ct['Team'] == 'Hollanda', 'Av.'] += hol_value - ceb_value

    ct_sorted = ct.sort_values(["Siralama", "P", "Av."], ascending=[True, False, False])
    ct_sorted.drop(['Rnk'], axis=1, inplace=True)

    table = ct_sorted.style.apply(lambda x: ['background: lightblue' if i < 5 else '' for i, val in enumerate(x.index)],
                                  axis=0)\
        .apply(lambda x: ['background: lightgreen' if 5 <= i < 11 else '' for i, val in enumerate(x.index)], axis=0) \
        .apply(lambda x: ['background: wheat' if 11 <= i < 17 else '' for i, val in enumerate(x.index)], axis=0) \
        .apply(lambda x: ['background: lightcoral' if 17 <= i <= 19 else '' for i, val in enumerate(x.index)], axis=0) \
        .apply(lambda x: ['background: lightgray' if 19 < i else '' for i, val in enumerate(x.index)], axis=0)

# CSS to inject contained in a string
    hide_table_row_index = """
                <style>
                thead tr th:first-child {display:none}
                tbody th {display:none}
                </style>
                """
    st.markdown(hide_table_row_index, unsafe_allow_html=True)

    st.table(table)

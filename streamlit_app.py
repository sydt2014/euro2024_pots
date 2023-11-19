import streamlit as st
import pandas as pd

st.set_page_config(layout="wide")

st.title("Euro 2024 Torba Simülasyonu")

col1, col2 = st.columns([0.3, 0.7])

with st.sidebar:
    gal, tr = st.columns([0.5, 0.5])
    gal_value = gal.number_input("🏴󠁧󠁢󠁷󠁬󠁳󠁿 Galler", min_value=0, max_value=10, step=1)
    tr_value = tr.number_input("🇹🇷 Türkiye", min_value=0, max_value=10, step=1)

    hs4, as4 = st.columns([0.5, 0.5])
    dan_value = as4.number_input("🇩🇰 Danimarka", min_value=0, max_value=10, step=1)
    nir_value = hs4.number_input("🇬🇧 K. İrlanda", min_value=0, max_value=10, step=1)

    hs5, as5 = st.columns([0.5, 0.5])
    hir_value = hs5.number_input("🇭🇷 Hırvatistan", min_value=0, max_value=10, step=1)
    erm_value = as5.number_input("🇦🇲 Ermenistan", min_value=0, max_value=10, step=1)

    hs6, as6 = st.columns([0.5, 0.5])
    arn_value = hs6.number_input("🇦🇱 Arvanutluk", min_value=0, max_value=10, step=1)
    far_value = as6.number_input("🇫🇴 Faroe Adaları", min_value=0, max_value=10, step=1)

    hs7, as7 = st.columns([0.5, 0.5])
    cek_value = hs7.number_input("🇨🇿 Çekya", min_value=0, max_value=10, step=1)
    mol_value = as7.number_input("🇲🇩 Moldova", min_value=0, max_value=10, step=1)

    hs8, as8 = st.columns([0.5, 0.5])
    rom_value = hs8.number_input("🇷🇴 Romanya", min_value=0, max_value=10, step=1)
    swi_value = as8.number_input("🇨🇭 İsviçre", min_value=0, max_value=10, step=1)

    hs9, as9 = st.columns([0.5, 0.5])
    ceb_value = hs9.number_input("🇬🇮 Cebelitarık", min_value=0, max_value=10, step=1)
    hol_value = as9.number_input("🇳🇱 Hollanda", min_value=0, max_value=10, step=1)

    hs10, as10 = st.columns([0.5, 0.5])
    ukr_value = hs10.number_input("🇺🇦 Ukrayna", min_value=0, max_value=10, step=1)
    ita_value = as10.number_input("🇮🇹 İtalya", min_value=0, max_value=10, step=1)

    hs11, as11 = st.columns([0.5, 0.5])
    slo_value = hs11.number_input("🇸🇮 Slovenya", min_value=0, max_value=10, step=1)
    kaz_value = as11.number_input("🇰🇿 Kazakistan", min_value=0, max_value=10, step=1)

    hs12, as12 = st.columns([0.5, 0.5])
    svk_value = hs12.number_input("🇸🇰 Slovakya", min_value=0, max_value=10, step=1)
    bos_value = as12.number_input("🇧🇦 Bosna-Hersek", min_value=0, max_value=10, step=1)


with col1:
    data = {
        'Rnk': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28,
                 29, 30],
        'Grp': ['J', 'B', 'C', 'F', 'A', 'D', 'H', 'G', 'E', 'I',
                'F', 'A', 'B', 'D', 'C', 'G', 'H', 'J', 'E', 'I',
                'C', 'B', 'H', 'E', 'D', 'G', 'J', 'A', 'I', 'F'],
        'Team': ['Portekiz', 'Fransa', 'İngiltere', 'Avusturya', 'İspanya',
                     'Türkiye', 'Danimarka', 'Macaristan', 'Arnavutluk', 'Romanya',
                     'Belçika', 'İskoçya', 'Hollanda', 'Hırvatistan', 'İtalya',
                     'Sırbistan', 'Slovenya', 'Slovakya', 'Çekya', 'İsviçre',
                     'Ukrayna', 'Yunanistan', 'Kazakistan', 'Polonya', 'Galler',
                     'Karadağ', 'Lüksemburg', 'Norveç', 'İsrail', 'İsveç'],
        'P': [24, 21, 19, 19, 21, 16, 16, 18, 14, 13,
              20, 17, 15, 13, 13, 14, 13, 16, 12, 11,
              13, 12, 12, 11, 11, 11, 11, 10, 9, 7],
        'Av.': [28, 26, 18, 10, 20, 7, 6, 9, 8, 4,
               18, 9, 4, 8, 7, 6, 4, 5, 3, 8,
               3, 6, 0, 0, 0, 0, -9, 2, -3, 0]
    }
    data = {
    'Rnk': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30],
    'Grp': ['J', 'B', 'A', 'F', 'C', 'G', 'D', 'H', 'E', 'I', 'F', 'A', 'J', 'B', 'G', 'D', 'C', 'H', 'E', 'I', 'C', 'B', 'H', 'A', 'E', 'D', 'G', 'J', 'F', 'I'],
    'Team': ['Portugal', 'France', 'Spain', 'Belgium', 'England', 'Hungary', 'Turkey', 'Denmark', 'Albania', 'Romania', 'Austria', 'Scotland', 'Slovakia', 'Netherlands', 'Serbia', 'Croatia', 'Italy', 'Slovenia', 'Czech Republic', 'Switzerland', 'Ukraine', 'Greece', 'Kazakhstan', 'Norway', 'Poland', 'Wales', 'Montenegro', 'Luxembourg', 'Sweden', 'Israel'],
    'P': [24, 21, 21, 20, 19, 18, 16, 16, 14, 13, 19, 17, 16, 15, 14, 13, 13, 13, 13, 11, 13, 12, 11, 11, 11, 11, 11, 11, 10, 9],
    'Av.': [28, 26, 20, 18, 18, 9, 7, 6, 8, 4, 10, 9, 5, 4, 6, 8, 7, 4, 3, 8, 3, 4, 0, 2, 0, 0, -2, -9, 2, -3],
    'Siralama': [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3],
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

    # Denmark
    if nir_value < dan_value:
        ct.loc[ct['Team'] == 'Danimarka', 'P'] += 3
    elif nir_value == dan_value:
        ct.loc[ct['Team'] == 'Danimarka', 'P'] += 1
    else:
        ct.loc[ct['Team'] == 'Danimarka', 'P'] += 0

    # Arnavutluk
    if arn_value > far_value:
        ct.loc[ct['Team'] == 'Arnavutluk', 'P'] += 3
    elif arn_value == far_value:
        ct.loc[ct['Team'] == 'Arnavutluk', 'P'] += 1
    elif (arn_value < far_value) & (cek_value > mol_value):
        ct.loc[ct['Team'] == 'Arnavutluk', 'Siralama'] = 2
        ct.loc[ct['Team'] == 'Çekya', 'Siralama'] = 1
    else:
        ct.loc[ct['Team'] == 'Arnavutluk', 'P'] += 0

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

    # İtalya
    if ukr_value < ita_value:
        ct.loc[ct['Team'] == 'İtalya', 'P'] += 3
    elif ukr_value == ita_value:
        ct.loc[ct['Team'] == 'İtalya', 'P'] += 1
    elif ukr_value > ita_value:
        ct.loc[ct['Team'] == 'İtalya', 'Siralama'] = 3
        ct.loc[ct['Team'] == 'Ukrayna', 'Siralama'] = 2
    else:
        ct.loc[ct['Team'] == 'İtalya', 'P'] += 0

    # Slovenya
    if slo_value > kaz_value:
        ct.loc[ct['Team'] == 'Slovenya', 'P'] += 3
    elif slo_value == kaz_value:
        ct.loc[ct['Team'] == 'Slovenya', 'P'] += 1
    elif slo_value < kaz_value:
        ct.loc[ct['Team'] == 'Slovenya', 'Siralama'] = 3
        ct.loc[ct['Team'] == 'Kazankistan', 'Siralama'] = 2
    else:
        ct.loc[ct['Team'] == 'Slovenya', 'P'] += 0

    # Çekya
    if (arn_value < far_value) & (cek_value > mol_value):
        ct.loc[ct['Team'] == 'Arnavutluk', 'Siralama'] = 2
        ct.loc[ct['Team'] == 'Çekya', 'Siralama'] = 1
        ct.loc[ct['Team'] == 'Çekya', 'P'] += 3
    elif cek_value == mol_value:
        ct.loc[ct['Team'] == 'Çekya', 'P'] += 1
    else:
        ct.loc[ct['Team'] == 'Çekya', 'P'] += 0

    # İsviçre
    if swi_value > rom_value:
        ct.loc[ct['Team'] == 'İsviçre', 'P'] += 3
        ct.loc[ct['Team'] == 'Romanya', 'Siralama'] = 2
        ct.loc[ct['Team'] == 'İsviçre', 'Siralama'] = 1
    elif rom_value == swi_value:
        ct.loc[ct['Team'] == 'İsviçre', 'P'] += 1
    else:
        ct.loc[ct['Team'] == 'İsviçre', 'P'] += 0

    # Ukrayna
    if ukr_value > ita_value:
        ct.loc[ct['Team'] == 'Ukrayna', 'P'] += 3
        ct.loc[ct['Team'] == 'İtalya', 'Siralama'] = 3
        ct.loc[ct['Team'] == 'Ukrayna', 'Siralama'] = 2
    elif ukr_value == ita_value:
        ct.loc[ct['Team'] == 'Ukrayna', 'P'] += 1
    else:
        ct.loc[ct['Team'] == 'Ukrayna', 'P'] += 0

    # Kazakistan
    if slo_value < kaz_value:
        ct.loc[ct['Team'] == 'Kazankistan', 'P'] += 3
        ct.loc[ct['Team'] == 'Slovenya', 'Siralama'] = 3
        ct.loc[ct['Team'] == 'Kazankistan', 'Siralama'] = 2
    elif slo_value == kaz_value:
        ct.loc[ct['Team'] == 'Kazankistan', 'P'] += 1
    else:
        ct.loc[ct['Team'] == 'Kazankistan', 'P'] += 0

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

    ct.loc[ct['Team'] == 'Türkiye', 'Av.'] += tr_value-gal_value
    ct.loc[ct['Team'] == 'Galler', 'Av.'] += gal_value-tr_value
    ct.loc[ct['Team'] == 'Danimarka', 'Av.'] += dan_value - nir_value
    ct.loc[ct['Team'] == 'Hırvatistan', 'Av.'] += hir_value - erm_value
    ct.loc[ct['Team'] == 'Arnavutluk', 'Av.'] += arn_value-far_value
    ct.loc[ct['Team'] == 'Çekya', 'Av.'] += cek_value - mol_value
    ct.loc[ct['Team'] == 'Romanya', 'Av.'] += rom_value - swi_value
    ct.loc[ct['Team'] == 'İsviçre', 'Av.'] += swi_value - rom_value
    ct.loc[ct['Team'] == 'Hollanda', 'Av.'] += hol_value - ceb_value
    ct.loc[ct['Team'] == 'Ukrayna', 'Av.'] += ukr_value - ita_value
    ct.loc[ct['Team'] == 'İtalya', 'Av.'] += ita_value-ukr_value
    ct.loc[ct['Team'] == 'Slovenya', 'Av.'] += slo_value - kaz_value
    ct.loc[ct['Team'] == 'Kazakistan', 'Av.'] += kaz_value-slo_value
    ct.loc[ct['Team'] == 'Slovakya', 'Av.'] += svk_value-bos_value

    ct_sorted = ct.sort_values(["Siralama", "P", "Av."], ascending=[True, False, False])
    #ct_sorted.drop("Rnk", inplace=True)
    ct_sorted.drop(['Rnk'], axis=1, inplace=True)

    table = ct_sorted.style.apply(lambda x: ['background: lightblue' if i < 5 else '' for i, val in enumerate(x.index)],
                                  axis=0) \
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

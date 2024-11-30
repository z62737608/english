import streamlit as st

st.markdown(f"""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Nanum+Gothic:wght@400;700&display=swap');
        
        body {{
            background-color: #f8f9fa;
            font-family: 'Nanum Gothic', sans-serif;
            color: #2c3e50;
        }}
        .container {{
            display: flex;
            flex-direction: column;
            padding: 2em;
            margin: 0 auto;
            width: 90%;
            max-width: 1200px;
            background-color: #ffffff;
            border-radius: 12px;
            box-shadow: 0 2px 8px rgba(0, 0, 0, 0.05);
        }}
        .section {{
            background-color: #fff9c4;
            padding: 20px;
            border-radius: 8px;
            margin: 15px 0;
            font-size: 1.1em;
            color: #2c3e50;
            box-shadow: 0 2px 4px rgba(0, 0, 0, 0.05);
            line-height: 1.6;
        }}
        .info-header {{
            background: #e3f2fd;
            color: #1565c0;
            padding: 15px 20px;
            border-radius: 8px;
            margin: 10px 0;
            font-weight: 600;
            box-shadow: 0 2px 4px rgba(0, 0, 0, 0.05);
        }}
        .category-title {{
            color: #1565c0;
            padding: 15px;
            margin: 15px 0;
            border-bottom: 2px solid #90caf9;
            font-weight: 600;
        }}
        .stButton button {{
            background: #ffffff;
            color: #1565c0;
            padding: 12px 20px;
            border-radius: 8px;
            border: 1px solid #90caf9;
            margin: 8px 0;
            width: 100%;
            transition: all 0.2s ease;
            font-size: 1em;
        }}
        .stButton button:hover {{
            background: #e3f2fd;
            border-color: #1565c0;
        }}
        .stTabs [data-baseweb="tab-list"] {{
            gap: 8px;
            background-color: #ffffff;
            border-radius: 8px;
            padding: 10px;
            box-shadow: 0 2px 4px rgba(0, 0, 0, 0.05);
        }}
        .stTabs [data-baseweb="tab"] {{
            background-color: transparent;
            color: #1565c0;
            border-radius: 6px;
            padding: 10px 20px;
            font-weight: 600;
        }}
        .stTabs [aria-selected="true"] {{
            background: #e3f2fd;
            color: #1565c0;
        }}
    </style>
""", unsafe_allow_html=True)

st.title("Introduce of Jeju food!")

if 'active_specialty' not in st.session_state:
    st.session_state.active_specialty = None
if 'active_local' not in st.session_state:
    st.session_state.active_local = None

specialties = {
    "Tangerine": {
        "desc": "It is an alkaline food that is good for dieting and helps absorb calcium. It facilitates metabolism and is rich in vitamin C, so it is good for skin beauty and fatigue recovery.",
        "image": "images/a.jpg"
    },
    "Bracken": {
        "desc": "It is rich in various minerals such as protein, fiber, calcium, and potassium. It is a food that goes well with chuja dried corvina and Jeju pork, and is cooked with stew, seasoned vegetables, and yukgaejang.",
        "image": "images/b.jpg"
    },
    "Damselfish": {
        "desc": "May-August is the season and is cooked by cold raw fish, river sashimi, roasting, salted fish, and braised fish. It is suitable for obese people due to its low calorie content, and is good for patients in the recovery phase after the disease because it has a light taste and is easy to digest due to its low oiliness.",
        "image": "images/c.jpg"
    },
    "Tilefish": {
        "desc": "It has been raised as a royal tribute since the Joseon Dynasty. The flesh is hard, low in fat, and rich in protein. It is rich in minerals such as calcium, phosphorus, and iron, and vitamins A, B1, and B2.",
        "image": "images/d.jpg"
    },
    "Cutlassfish": {
        "desc": "It is in season from September to October, and the skin is white and soft, used in diet meals, and good for promoting children's growth and development. Cook with boiled pumpkin soup, grilled meat, and fried food.",
        "image": "images/e.jpg"
    },
    "Horse Meat": {
        "desc": "It was used for medicinal purposes because it was good for wind disease and itching, and leg bones are special medicines for arthritis and neuralgia. It is excellent for preventing colds in children.",
        "image": "images/f.jpg"
    },
    "Black Pig Meat": {
        "desc": "Jeju pigs are used almost all parts to cook. The meat quality is excellent and the amount of fat is small, so the taste is much better.",
        "image": "images/g.jpg"
    }
}

local_foods = {
    "Cold Raw Damselfish Soup": {
        "desc": "Cold raw damselfish soup is a substitute for cold soup enjoyed in summer on Jeju Island, and it was named cold raw fish soup because it is eaten by mixing raw fish and then pouring water.",
        "image": "images/h.jpg"
    },
    "Cutlassfish Soup": {
        "desc": "Cutlassfish soup is a soup made by seasoning fresh cutlassfish with pumpkin, ground cabbage, and green pepper.",
        "image": "images/i.jpg"
    },
    "Sea Urchin Soup": {
        "desc": "It is common for sea urchin soup boiled with fresh seaweed to be served to guests by boiling it at a feast or a funeral.",
        "image": "images/j.jpg"
    },
    "Cold Raw Squid Soup": {
        "desc": "It is the most popular in any restaurant in summer and forms two major mountain ranges along with Cold raw damselfish soup.",
        "image": "images/k.jpg"
    },
    "Grilled Tilefish": {
        "desc": "Tilefish, called the queen of snapper, is baked after splitting the belly, sprinkling salt, and drying it thickly, and the taste is excellent.",
        "image": "images/l.jpg"
    },
    "Bingtteok": {
        "desc": "Bingtteok is a rice cake made by rolling a cow made of boiled radish into buckwheat pancakes. The light taste of buckwheat pancakes and the cool taste of radish vegetables are combined to create a unique taste.",
        "image": "images/m.jpg"
    },
    "Meat Noodle": {
        "desc": "Meat noodle is a favorite food to eat on the village's feast day or on the day of a big event.",
        "image": "images/n.jpg"
    }
}

tab1, tab2 = st.tabs(["Jeju's 7 Specialties", "Jeju's 7 Local Food"])

with tab1:
    col1, col2 = st.columns([1, 2])
    with col1:
        st.markdown("<div class='category-title'>Select Specialties</div>", unsafe_allow_html=True)
        for item in specialties.keys():
            if st.button(item, key=f"specialty_{item}", use_container_width=True):
                st.session_state.active_specialty = item if st.session_state.active_specialty != item else None
    
    with col2:
        st.markdown("<div class='info-header'>Information (Press the food button again to hide the information.)</div>", unsafe_allow_html=True)
        if st.session_state.active_specialty:
            st.markdown(f"<div class='section'>{specialties[st.session_state.active_specialty]['desc']}</div>", unsafe_allow_html=True)
            try:
                st.image(specialties[st.session_state.active_specialty]['image'], 
                        caption=f"Jeju {st.session_state.active_specialty}", 
                        use_column_width=True)
            except:
                st.info("Preparing Images..")

with tab2:
    col3, col4 = st.columns([1, 2])
    with col3:
        st.markdown("<div class='category-title'>Select Local Food</div>", unsafe_allow_html=True)
        for item in local_foods.keys():
            if st.button(item, key=f"local_{item}", use_container_width=True):
                st.session_state.active_local = item if st.session_state.active_local != item else None
    
    with col4:
        st.markdown("<div class='info-header'>Information (Press the food button again to hide the information.)</div>", unsafe_allow_html=True)
        if st.session_state.active_local:
            st.markdown(f"<div class='section'>{local_foods[st.session_state.active_local]['desc']}</div>", unsafe_allow_html=True)
            try:
                st.image(local_foods[st.session_state.active_local]['image'], 
                        caption=f"Jeju {st.session_state.active_local}", 
                        use_column_width=True)
            except:
                st.info("Preparing Images..")
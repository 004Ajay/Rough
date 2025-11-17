import streamlit as st

PRINTER_MODEL_PATTERNS = {
    "ZD421": ["zd421", "zdesigner zd421", "zebra zd421"],
    "GT800": ["gt800", "zebra gt800"],
    "ZD230": ["zd230", "zdesigner zd230", "zebra zd230"],
}

@st.cache_resource
def build_printer_lookup():
    lookup = {}
    for model, patterns in PRINTER_MODEL_PATTERNS.items():
        for p in patterns:
            lookup[p.lower()] = model
    return lookup

PRINTER_LOOKUP = build_printer_lookup()

# {'zd421': 'ZD421',
#  'zdesigner zd421': 'ZD421',
#  'zebra zd421': 'ZD421',
#  'gt800': 'GT800',
#  'zebra gt800': 'GT800',
#  'zd230': 'ZD230',
#  'zdesigner zd230': 'ZD230',
#  'zebra zd230': 'ZD230'}

@st.cache_data
def detect_printer_model(queue_name: str):
    q = queue_name.lower()
    for pattern, model in PRINTER_LOOKUP.items():
        if pattern in q:
            return model
    return None

detect_printer_model("zd421")

# 'ZD421'

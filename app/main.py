import streamlit as st
import pandas as pd
from pathlib import Path
import os
from rag_system import RAGSystem
from data_generator import DataGenerator

class StreamlitApp:
    def __init__(self):
        """Initialize Streamlit application"""
        st.set_page_config(
            page_title="ExcelMind",
            page_icon="📊",
            layout="wide"
        )
        
        # Initialize session state
        if 'rag_system' not in st.session_state:
            st.session_state.rag_system = RAGSystem()
        if 'chat_history' not in st.session_state:
            st.session_state.chat_history = []

    def render_sidebar(self):
        """Render sidebar with data loading options"""
        st.sidebar.title("📊 ExcelMind")
        st.sidebar.write("Excel Analysis with Natural Language")
        
        # Data loading options
        st.sidebar.header("Data Loading")
        
        # Option to generate sample data
        if st.sidebar.button("Generate Sample Data"):
            with st.sidebar.spinner("Generating sample data..."):
                generator = DataGenerator()
                df = generator.save_to_excel()
                st.sidebar.success("Sample data generated!")
                self.load_data("data/sample/employee_data.xlsx")
        
        # File upload
import pandas as pd
import google.generativeai as genai
from typing import Dict, Any, Optional
import os
from dotenv import load_dotenv
from .utils.database import DatabaseManager
from .utils.visualization import Visualizer

class RAGSystem:
    def __init__(self):
        """Initialize RAG system"""
        # Load environment variables
        load_dotenv()
        
        # Initialize components
        self._setup_llm()
        self.db = DatabaseManager()
        self.visualizer = Visualizer()
        self.current_context = {}

    def _setup_llm(self):
        """Setup Gemini LLM"""
        api_key = os.getenv('GEMINI_API_KEY')
        if not api_key:
            raise ValueError("GEMINI_API_KEY not found in environment variables")
        
        genai.configure(api_key=api_key)
        self.model = genai.GenerativeModel("gemini-1.5-pro")
        self.chat = self.model.start_chat(history=[])

    def load_data(self, excel_file: str, table_name: str = 'main_table') -> bool:
        """Load Excel file into database"""
        try:
            df = pd.read_excel(excel_file)
            success = self.db.create_table_from_dataframe(df, table_name)
            if success:
                self._update_context(table_name)
            return success
        except Exception as e:
            print(f"Error loading data: {str(e)}")
            return False

    def _update_context(self, table_name: str):
        """Update context with table schema"""
        schema = self.db.get_table_schema(table_name)
        self.current_context = {
            'table_name': table_name,
            'schema': schema
        }

    def _generate_sql_query(self, question: str) -> str:
        """Generate SQL query from natural language question"""
        system_prompt = f"""You are an expert SQL analyst. Generate a SQL query for the following question.
        Table name: {self.current_context['table_name']}
        Schema: {self.current_context['schema']}
        
        Rules:
        1. Only use SELECT statements
        2. Use proper SQL syntax
        3. Only use columns that exist in the schema
        4. Return only the SQL query, no explanations
        
        Question: {question}
        """
        
        response = self.model.generate_content(system_prompt)
        return response.text.strip()

    def _determine_visualization(self, query: str, data: pd.DataFrame) -> Optional[Dict[str, Any]]:
        """Determine appropriate visualization for the data"""
        viz_params = None
        
        # Check query type and data shape for visualization
        if any(word in query.lower() for word in ['average', 'count', 'sum']):
            if len(data.columns) == 2:
                viz_params = {
                    'type': 'bar',
                    'params': {
                        'x': data.columns[0],
                        'y': data.columns[1],
                        'title': 'Query Results'
                    }
                }
        elif 'trend' in query.lower() or 'over time' in query.lower():
            viz_params = {
                'type': 'line',
                'params': {
                    'x': data.columns[0],
                    'y': data.columns[1],
                    'title': 'Trend Analysis'
                }
            }
        elif 'distribution' in query.lower():
            viz_params = {
                'type': 'pie',
                'params': {
                    'values': data.columns[1],
                    'names': data.columns[0],
                    'title': 'Distribution Analysis'
                }
            }
        
        return viz_params

    def query(self, question: str) -> Dict[str, Any]:
        """Process natural language query and return results"""
        try:
            # Generate SQL query
            sql_query = self._generate_sql_query(question)
            
            # Execute query
            results = self.db.execute_query(sql_query)
            
            # Create DataFrame from results
            df_results = pd.DataFrame(results)
            
            # Determine visualization
            viz_params = self._determine_visualization(question, df_results)
            
            # Create visualization if applicable
            visualization = None
            if viz_params:
                visualization = self.visualizer.create_visualization(
                    df_results,
                    viz_params['type'],
                    viz_params['params']
                )
            
            # Generate natural language response
            response_prompt = f"""Given the following query results, provide a natural language summary:
            Query: {question}
            Results: {results}
            
            Keep the response concise and highlight key insights."""
            
            response = self.model.generate_content(response_prompt)
            
            return {
                'query': sql_query,
                'results': results,
                'visualization': visualization,
                'summary': response.text
            }
            
        except Exception as e:
            return {
                'error': str(e)
            }

    def close(self):
        """Clean up resources"""
        self.db.disconnect()
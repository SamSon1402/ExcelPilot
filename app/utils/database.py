import sqlite3
import pandas as pd
from typing import List, Dict, Any

class DatabaseManager:
    def __init__(self, database_name: str = 'excelmind.db'):
        """Initialize database connection"""
        self.database_name = database_name
        self.connection = None
        self.connect()

    def connect(self):
        """Create database connection"""
        self.connection = sqlite3.connect(self.database_name)

    def disconnect(self):
        """Close database connection"""
        if self.connection:
            self.connection.close()

    def create_table_from_dataframe(self, df: pd.DataFrame, table_name: str):
        """Create a table from pandas DataFrame"""
        try:
            df.to_sql(table_name, self.connection, if_exists='replace', index=False)
            return True
        except Exception as e:
            print(f"Error creating table: {str(e)}")
            return False

    def execute_query(self, query: str) -> List[Dict[str, Any]]:
        """Execute SQL query and return results as list of dictionaries"""
        try:
            result = pd.read_sql_query(query, self.connection)
            return result.to_dict(orient='records')
        except Exception as e:
            print(f"Error executing query: {str(e)}")
            return []

    def get_table_schema(self, table_name: str) -> List[Dict[str, str]]:
        """Get schema information for a table"""
        cursor = self.connection.cursor()
        cursor.execute(f"PRAGMA table_info({table_name})")
        columns = cursor.fetchall()
        
        schema = []
        for col in columns:
            schema.append({
                'name': col[1],
                'type': col[2]
            })
        return schema

    def __del__(self):
        """Destructor to ensure connection is closed"""
        self.disconnect()
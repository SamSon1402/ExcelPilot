import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import os

class DataGenerator:
    def __init__(self, num_rows: int = 1000):
        self.num_rows = num_rows
        self.departments = ['Engineering', 'Sales', 'Marketing', 'HR', 'Finance']
        self.locations = ['New York', 'London', 'Tokyo', 'Singapore', 'Berlin']
        self.positions = ['Junior', 'Senior', 'Lead', 'Manager', 'Director']

    def generate_employee_data(self) -> pd.DataFrame:
        """Generate sample employee data"""
        np.random.seed(42)  # For reproducibility

        data = {
            'employee_id': range(1, self.num_rows + 1),
            'first_name': np.random.choice(self._get_first_names(), self.num_rows),
            'last_name': np.random.choice(self._get_last_names(), self.num_rows),
            'department': np.random.choice(self.departments, self.num_rows),
            'position': np.random.choice(self.positions, self.num_rows),
            'location': np.random.choice(self.locations, self.num_rows),
            'salary': self._generate_salaries(),
            'joining_date': self._generate_dates(),
            'performance_rating': np.random.normal(3.5, 0.5, self.num_rows).clip(1, 5),
            'projects_completed': np.random.randint(0, 30, self.num_rows)
        }

        df = pd.DataFrame(data)
        
        # Add some realistic correlations
        df.loc[df['position'] == 'Director', 'salary'] *= 1.5
        df.loc[df['performance_rating'] >= 4.0, 'projects_completed'] += 5
        
        return df

    def _generate_salaries(self) -> np.ndarray:
        """Generate realistic salary distribution"""
        base_salaries = np.random.normal(70000, 15000, self.num_rows)
        return base_salaries.clip(40000, 150000).astype(int)

    def _generate_dates(self) -> pd.Series:
        """Generate joining dates within last 5 years"""
        end_date = datetime.now()
        start_date = end_date - timedelta(days=5*365)
        
        dates = [start_date + timedelta(days=x) for x in 
                np.random.randint(0, (end_date - start_date).days, self.num_rows)]
        return pd.Series(dates)

    def _get_first_names(self) -> list:
        """Get list of sample first names"""
        return ['John', 'Jane', 'Michael', 'Emily', 'David', 'Sarah', 'Robert', 
                'Emma', 'William', 'Olivia', 'James', 'Sophia', 'Joseph', 'Isabella']

    def _get_last_names(self) -> list:
        """Get list of sample last names"""
        return ['Smith', 'Johnson', 'Williams', 'Brown', 'Jones', 'Garcia', 'Miller',
                'Davis', 'Rodriguez', 'Martinez', 'Hernandez', 'Lopez', 'Gonzalez']

    def save_to_excel(self, filename: str = 'employee_data.xlsx'):
        """Generate and save data to Excel file"""
        df = self.generate_employee_data()
        
        # Create directory if it doesn't exist
        os.makedirs('data/sample', exist_ok=True)
        file_path = os.path.join('data/sample', filename)
        
        df.to_excel(file_path, index=False)
        print(f"Sample data saved to {file_path}")
        return df

if __name__ == "__main__":
    generator = DataGenerator()
    generator.save_to_excel()
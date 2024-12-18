import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
from typing import Dict, Any

class Visualizer:
    @staticmethod
    def create_visualization(data: pd.DataFrame, viz_type: str, params: Dict[str, Any] = None):
        """Create visualization based on type and parameters"""
        if params is None:
            params = {}

        try:
            if viz_type == 'bar':
                return Visualizer._create_bar_chart(data, params)
            elif viz_type == 'line':
                return Visualizer._create_line_chart(data, params)
            elif viz_type == 'pie':
                return Visualizer._create_pie_chart(data, params)
            elif viz_type == 'scatter':
                return Visualizer._create_scatter_plot(data, params)
            else:
                raise ValueError(f"Unsupported visualization type: {viz_type}")
        except Exception as e:
            print(f"Error creating visualization: {str(e)}")
            return None

    @staticmethod
    def _create_bar_chart(data: pd.DataFrame, params: Dict[str, Any]):
        """Create a bar chart"""
        return px.bar(
            data,
            x=params.get('x'),
            y=params.get('y'),
            title=params.get('title', ''),
            labels=params.get('labels', {}),
            color=params.get('color')
        )

    @staticmethod
    def _create_line_chart(data: pd.DataFrame, params: Dict[str, Any]):
        """Create a line chart"""
        return px.line(
            data,
            x=params.get('x'),
            y=params.get('y'),
            title=params.get('title', ''),
            labels=params.get('labels', {})
        )

    @staticmethod
    def _create_pie_chart(data: pd.DataFrame, params: Dict[str, Any]):
        """Create a pie chart"""
        return px.pie(
            data,
            values=params.get('values'),
            names=params.get('names'),
            title=params.get('title', '')
        )

    @staticmethod
    def _create_scatter_plot(data: pd.DataFrame, params: Dict[str, Any]):
        """Create a scatter plot"""
        return px.scatter(
            data,
            x=params.get('x'),
            y=params.get('y'),
            title=params.get('title', ''),
            labels=params.get('labels', {}),
            color=params.get('color')
        )
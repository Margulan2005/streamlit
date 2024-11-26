import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


class StreamlitApp:
    def __init__(self):
        pass

    @staticmethod
    def load_data(file):
        try:
            data = pd.read_csv(file)
            return data
        except Exception as e:
            st.error(f"Error loading file: {e}")
            return None

    @staticmethod
    def clean_and_convert_values(df, column):
        """
        Clean and convert a column to numeric type, replacing commas with dots and removing whitespace.
        """
        try:
            df[column] = df[column].astype(str).str.replace(",", ".", regex=False).str.replace(r"\s+", "", regex=True)
            df[column] = pd.to_numeric(df[column], errors="coerce")
        except Exception as e:
            st.error(f"Error processing column '{column}': {e}")
        return df

    @staticmethod
    def plot_bar_chart(df, category_column, value_column):
        """
        Plot a bar chart showing the mean of a numeric column grouped by a categorical column.
        """
        # Clean and convert the numeric column
        df = StreamlitApp.clean_and_convert_values(df, value_column)

        # Check column types
        if not pd.api.types.is_object_dtype(df[category_column]) and not pd.api.types.is_categorical_dtype(df[category_column]):
            st.warning(f"The column '{category_column}' must be categorical.")
            return

        if not pd.api.types.is_numeric_dtype(df[value_column]):
            st.warning(f"The column '{value_column}' must be numeric.")
            return

        # Group by category and calculate the mean
        category_mean = df.groupby(category_column)[value_column].mean()

        # Plot the bar chart
        fig, ax = plt.subplots(figsize=(10, 6))
        colors = plt.cm.tab20(np.linspace(0, 1, len(category_mean)))

        ax.bar(category_mean.index, category_mean.values, color=colors)
        ax.set_title(f"Mean {value_column} by {category_column}", fontsize=16)
        ax.set_xlabel(category_column, fontsize=14)
        ax.set_ylabel(f"Mean {value_column}", fontsize=14)
        ax.tick_params(axis="x", rotation=45)

        st.pyplot(fig)
        st.write(f"Mean {value_column} by {category_column}:")
        st.dataframe(category_mean.reset_index())

    def run(self):
        st.title("Data Analysis Tool")
        st.markdown(
            """
            This app allows you to upload a CSV file, select a categorical and numeric column, 
            and visualize the mean of the numeric column grouped by the categories.
            """
        )

        # File uploader
        uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"])
        if uploaded_file is not None:
            df = self.load_data(uploaded_file)

            if df is not None and not df.empty:
                st.write("### Uploaded Data")
                st.dataframe(df, height=400)

                # Column selection
                category_column = st.selectbox("Select a categorical column", df.columns)
                value_column = st.selectbox("Select a numeric column", df.columns)

                if category_column and value_column:
                    st.write(f"### Bar Chart: Mean of {value_column} by {category_column}")
                    self.plot_bar_chart(df, category_column, value_column)
            else:
                st.warning("The uploaded file is empty or invalid.")
        else:
            st.info("Please upload a CSV file to begin.")

        # Custom CSS styling for header
        st.markdown(
            """
            <style>
            h1 {
                color: green;
                text-align: center;
                font-size: 24px;
            }
            </style>
            """,
            unsafe_allow_html=True,
        )


# Main entry point
if __name__ == "__main__":
    app = StreamlitApp()
    app.run()

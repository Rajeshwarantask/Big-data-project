import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Load your sales data
sales_data = pd.read_csv('data/retail_data.csv')  # Adjust the path if needed
customer_df = pd.read_csv('data/retail_data.csv')  # Load your customer data if necessary

# Ensure date column is in datetime format
sales_data['transaction_date'] = pd.to_datetime(sales_data['transaction_date'])

# 1. Sales Trend Visualization
def plot_sales_trend():
    sales_trend = sales_data.resample('ME', on='transaction_date').sum()  # Monthly sales
    plt.figure(figsize=(12, 6))
    plt.plot(sales_trend.index, sales_trend['total_sales'], marker='o')
    plt.title('Sales Trend Over Time')
    plt.xlabel('Date')
    plt.ylabel('Total Sales')
    plt.xticks(rotation=45)
    plt.grid()
    plt.tight_layout()
    plt.savefig('visualizations/sales_trend.png')
    plt.show()

# 2. Spending vs Transactions
def plot_spending_vs_transactions():
    plt.figure(figsize=(10, 6))
    plt.scatter(customer_df['transactions_count'], customer_df['average_spent'], alpha=0.5)
    plt.title('Customer Spending vs. Transactions Count')
    plt.xlabel('Transactions Count')
    plt.ylabel('Average Spending')
    plt.grid()
    plt.savefig('results/spending_vs_transactions.png')
    plt.close()

# 3. Churn Rate by Age
def plot_churn_rate_by_age():
    plt.figure(figsize=(12, 6))
    sns.countplot(data=customer_df, x='age', hue='churn')
    plt.title('Churn Rate by Age')
    plt.xlabel('Age')
    plt.ylabel('Count')
    plt.legend(title='Churn', loc='upper right', labels=['Not Churned', 'Churned'])
    plt.grid()
    plt.savefig('results/churn_rate_by_age.png')
    plt.close()

# 4. Sales Distribution
def plot_sales_distribution():
    plt.figure(figsize=(10, 6))
    plt.hist(sales_data['total_sales'], bins=30, edgecolor='k', alpha=0.7)
    plt.title('Sales Amount Distribution')
    plt.xlabel('Sales Amount')
    plt.ylabel('Frequency')
    plt.grid()
    plt.savefig('results/sales_distribution.png')
    plt.close()

# 5. Radar Chart for Sales by Product Category
def plot_radar_chart():
    categories = list(customer_df['product_category'].unique())
    values = [customer_df[customer_df['product_category'] == category]['total_sales'].sum() for category in categories]
    
    # Number of variables
    num_vars = len(categories)

    # Compute angle for each axis
    angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()

    # The plot is a circle, so we need to "complete the loop" and append the start value to the end.
    values += values[:1]
    angles += angles[:1]

    # Draw the radar chart
    fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(polar=True))
    ax.fill(angles, values, color='red', alpha=0.25)
    ax.plot(angles, values, color='red', linewidth=2)

    # Labels for each axis
    ax.set_yticklabels([])
    ax.set_xticks(angles[:-1])
    ax.set_xticklabels(categories)

    plt.title('Sales by Product Category')
    plt.savefig('results/sales_by_product_category.png')
    plt.close()

# Run all visualizations
if __name__ == "__main__":
    plot_sales_trend()
    plot_spending_vs_transactions()
    plot_churn_rate_by_age()
    plot_sales_distribution()
    plot_radar_chart()  # Add this line to run the radar chart

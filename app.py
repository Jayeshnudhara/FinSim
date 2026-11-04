
import streamlit as st
import pandas as pd
import plotly.express as px

from sample_data import get_sample_data
from modules.anomaly_detector import detect_anomalies
from modules.anomaly_detector import explain_anomalies

# --------------------------------------------------
# PAGE CONFIGURATION
# --------------------------------------------------

st.set_page_config(
    page_title="FinSight | Financial Intelligence",
    page_icon="💹",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --------------------------------------------------
# CUSTOM STYLING
# --------------------------------------------------

st.markdown("""

<style>
/* =========================================
   FINSIGHT — DESIGN SYSTEM
========================================= */

:root {
    --navy: #17243A;
    --navy-light: #263B58;
    --ivory: #F6F5F0;
    --white: #FFFFFF;
    --gold: #B99A60;
    --gold-light: #E9DFC9;
    --text: #253247;
    --muted: #788397;
    --border: #E5E3DC;
}

/* MAIN APPLICATION */

.stApp {
    background-color: var(--ivory);
    color: var(--text);
}

[data-testid="stAppViewContainer"] {
    background-color: var(--ivory);
}

[data-testid="stHeader"] {
    background-color: transparent;
}

/* MAIN CONTENT */

[data-testid="stMain"] {
    background-color: var(--ivory);
}

.block-container {
    padding-top: 2.2rem;
    padding-bottom: 3rem;
    max-width: 1450px;
}

/* TYPOGRAPHY */

.stApp h1,
.stApp h2,
.stApp h3,
.stApp p,
.stApp label,
.stApp li {
    color: var(--text);
}

.stApp h1 {
    font-weight: 750;
    letter-spacing: -1px;
}

.stApp h2,
.stApp h3 {
    font-weight: 650;
}

/* SIDEBAR */

[data-testid="stSidebar"] {
    background-color: var(--white);
    border-right: 1px solid #34435A;
}

[data-testid="stSidebar"] * {
    color: #F6F5F0;
}

[data-testid="stSidebar"] [data-testid="stRadio"] label {
    color: #E5E9EF;
}

[data-testid="stSidebar"] [data-testid="stRadio"] label:hover {
    color: var(--gold);
}

/* BRAND */

.brand {
    font-size: 32px;
    font-weight: 800;
    letter-spacing: 1px;
    color: var(--gold);
}

.subtitle {
    color: #AAB5C5;
    font-size: 11px;
    letter-spacing: 2px;
}

/* HERO SECTION */

.hero {
    background: linear-gradient(
        120deg,
        var(--navy),
        var(--navy-light)
    );
    padding: 38px;
    border-radius: 18px;
    color: white;
    margin-bottom: 30px;
    box-shadow: 0 8px 25px rgba(23, 36, 58, 0.12);
}

.hero h1 {
    color: white !important;
    font-size: 34px;
    line-height: 1.3;
}

.hero p {
    color: #D8DFE8 !important;
    font-size: 16px;
    line-height: 1.7;
}

/* SECTION HEADINGS */

.section-title {
    color: var(--navy);
    font-size: 23px;
    font-weight: 750;
    margin-top: 28px;
    margin-bottom: 16px;
}

/* METRIC CARDS */

div[data-testid="stMetric"] {
    background-color: var(--white);
    padding: 20px;
    border: 1px solid var(--border);
    border-radius: 14px;
    box-shadow: 0 3px 12px rgba(23, 36, 58, 0.04);
}

div[data-testid="stMetricLabel"] {
    color: var(--muted) !important;
}

div[data-testid="stMetricValue"] {
    color: var(--navy) !important;
    font-weight: 750;
}

div[data-testid="stMetricDelta"] {
    color: #477B61 !important;
}

/* BUTTONS */

.stButton button {
    background-color: var(--navy);
    color: white !important;
    border: 1px solid var(--navy);
    border-radius: 9px;
    padding: 8px 18px;
}

.stButton button:hover {
    background-color: var(--navy-light);
    border-color: var(--gold);
}

/* INPUTS */

.stTextInput input,
.stNumberInput input,
.stSelectbox div[data-baseweb="select"],
.stDateInput input {
    background-color: white;
    color: var(--text);
    border-radius: 8px;
}

/* DATA TABLES */

[data-testid="stDataFrame"] {
    border: 1px solid var(--border);
    border-radius: 12px;
    overflow: hidden;
}

/* ALERTS */

[data-testid="stAlert"] {
    border-radius: 10px;
}

/* DIVIDERS */

hr {
    border-color: var(--border);
}
</style>

""", unsafe_allow_html=True)

# --------------------------------------------------
# SIDEBAR
# --------------------------------------------------

with st.sidebar:

    st.markdown(
        '<div class="brand">FinSim.</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="subtitle">FINANCIAL INTELLIGENCE</div>',
        unsafe_allow_html=True
    )

    st.divider()

    page = st.radio(
        "NAVIGATION",
        [
            "Overview",
            "Spend Intelligence",
            "Anomaly Detection",
            "Financial Forecast",
            "What-If Simulator"
        ]
    )

    st.divider()

    st.caption("FinSim | National Project Expo 2026")

# --------------------------------------------------
# MAIN PAGE
# --------------------------------------------------

if page == "Overview":

    st.markdown("""
    <div class="hero">
        <h1>Understand your money.<br>Make smarter decisions.</h1>
        <p>
            Your personal financial intelligence centre.
            Explore spending patterns, detect unusual
            transactions and simulate financial decisions.
        </p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown(
        '<div class="section-title">Your Financial Overview</div>',
        unsafe_allow_html=True
    )

    # Load transaction data
    df = get_sample_data()

    # Calculate financial metrics
    total_income = df[df["type"] == "Income"]["amount"].sum()

    total_expenses = df[df["type"] == "Expense"]["amount"].sum()

    balance = total_income - total_expenses

    savings_rate = (
    (balance / total_income) * 100
    if total_income > 0 else 0
    )

    # Display financial metrics
    col1, col2, col3, col4 = st.columns(4)

    col1.metric(
    "Total Income",
    f"₹{total_income:,.0f}"
    )

    col2.metric(
    "Total Expenses",
    f"₹{total_expenses:,.0f}"
    )

    col3.metric(
    "Current Balance",
    f"₹{balance:,.0f}"
    )

    col4.metric(
    "Savings Rate",
    f"{savings_rate:.1f}%"
    )

    
    # ------------------------------------------
    # FINANCIAL CHARTS
    # ------------------------------------------

    st.markdown(
        '<div class="section-title">Financial Analytics</div>',
        unsafe_allow_html=True
    )

    # Monthly income and expenses
    monthly_data = (
        df.assign(month=df["date"].dt.strftime("%b"))
        .groupby(["month", "type"])["amount"]
        .sum()
        .reset_index()
    )

    monthly_chart = px.bar(
        monthly_data,
        x="month",
        y="amount",
        color="type",
        barmode="group",
        title="Income vs Expenses",
        color_discrete_map={
            "Income": "#B99A60",
            "Expense": "#263B58"
        }
    )

    monthly_chart.update_layout(
        plot_bgcolor="white",
        paper_bgcolor="white",
        font_color="#17243A",
        legend_title_text="Transaction Type",
        margin=dict(l=20, r=20, t=60, b=20)
    )

    # Spending by category
    expense_data = df[df["type"] == "Expense"]

    category_data = (
        expense_data.groupby("category")["amount"]
        .sum()
        .reset_index()
        .sort_values("amount", ascending=False)
    )

    category_chart = px.pie(
        category_data,
        names="category",
        values="amount",
        hole=0.55,
        title="Expense Distribution"
    )

    category_chart.update_layout(
        paper_bgcolor="white",
        font_color="#17243A",
        margin=dict(l=20, r=20, t=60, b=20)
    )

    col1, col2 = st.columns(2)

    with col1:
        st.plotly_chart(
            monthly_chart,
            use_container_width=True
            )

    with col2:
        st.plotly_chart(
            category_chart,
            use_container_width=True
        )


    
# ------------------------------------------
# RECENT TRANSACTIONS
# ------------------------------------------

    st.markdown(
        '<div class="section-title">Recent Transactions</div>',
        unsafe_allow_html=True
    )

    recent_transactions = df.sort_values(
        "date", ascending=False
    ).head(8)

    st.dataframe(
        recent_transactions[
            ["date", "description", "category", "type", "amount"]
        ],
        use_container_width=True,
        hide_index=True,
        column_config={
            "date": st.column_config.DateColumn("Date"),
            "amount": st.column_config.NumberColumn(
                "Amount",
                format="₹%.2f"
            )
        }
    )

    st.markdown(
        '<div class="section-title">Explore FinSight</div>',
        unsafe_allow_html=True
    )

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("### Spend Intelligence")
        st.write(
            "Understand where your money goes "
            "and discover spending patterns."
        )

        st.markdown("### Anomaly Detection")
        st.write(
            "Identify unusual transactions "
            "using machine learning."
        )

    with col2:
        st.markdown("### Financial Forecast")
        st.write(
            "Explore possible future financial "
            "outcomes."
        )

        st.markdown("### What-If Simulator")
        st.write(
            "Experiment with financial decisions "
            "before making them."
        )

elif page == "Spend Intelligence":

    st.title("Spend Intelligence")
    st.write("Understand your spending patterns and discover where your money goes.")

    df = get_sample_data()

    expenses = df[df["type"] == "Expense"].copy()

    # Spending summary
    total_spending = expenses["amount"].sum()
    transaction_count = len(expenses)
    average_spending = expenses["amount"].mean()

    col1, col2, col3 = st.columns(3)

    col1.metric("Total Spending", f"₹{total_spending:,.0f}")
    col2.metric("Number of Transactions", transaction_count)
    col3.metric("Average Transaction", f"₹{average_spending:,.0f}")

    # Category-wise spending
    st.subheader("Spending by Category")

    category_spending = (
        expenses.groupby("category")["amount"]
        .sum()
        .reset_index()
        .sort_values("amount", ascending=False)
    )

    category_chart = px.bar(
        category_spending,
        x="category",
        y="amount",
        color="amount",
        title="Which categories cost you the most?",
        color_continuous_scale=["#E9DFC9", "#B99A60", "#17243A"]
    )

    category_chart.update_layout(
        plot_bgcolor="white",
        paper_bgcolor="white",
        font_color="#17243A"
    )

    st.plotly_chart(category_chart, use_container_width=True)

    # Spending transactions
    st.subheader("Expense Details")

    st.dataframe(
        expenses[["date", "description", "category", "merchant", "amount"]],
        use_container_width=True,
        hide_index=True
    )

elif page == "Anomaly Detection":

    st.title("Anomaly Detection")
    st.write("Identify unusual transactions using machine learning.")

    df = get_sample_data()

    # Run the anomaly detection model
    with st.spinner("Analysing transactions..."):
        anomaly_results = detect_anomalies(df)
        anomaly_results = explain_anomalies(anomaly_results)

    # Summary metrics
    flagged = anomaly_results[anomaly_results["anomaly"] == True]
    high_alerts = anomaly_results[
        anomaly_results["alert_level"] == "High"
    ]

    col1, col2, col3 = st.columns(3)

    col1.metric("Transactions Analysed", len(anomaly_results))
    col2.metric("Unusual Transactions", len(flagged))
    col3.metric("High Alerts", len(high_alerts))

    st.subheader("Detected Anomalies")

    if len(flagged) > 0:
        st.dataframe(
            flagged[
                ["date", "description", "category", "amount",
                 "alert_level", "explanation"]
            ],
            use_container_width=True,
            hide_index=True
        )
    else:
        st.success("No unusual transactions detected.")

    st.subheader("All Analysed Expenses")

    st.dataframe(
        anomaly_results[
            ["date", "description", "category", "amount",
             "anomaly", "alert_level"]
        ],
        use_container_width=True,
        hide_index=True
    )
elif page == "Financial Forecast":

    st.title("Financial Forecast")
    st.write("Explore your spending trends and estimate your future financial position.")

    df = get_sample_data()

    # Prepare monthly financial data
    monthly_data = (
        df.assign(month=df["date"].dt.to_period("M").astype(str))
        .groupby(["month", "type"])["amount"]
        .sum()
        .unstack(fill_value=0)
        .reset_index()
    )

    # Make sure both columns exist
    if "Income" not in monthly_data.columns:
        monthly_data["Income"] = 0

    if "Expense" not in monthly_data.columns:
        monthly_data["Expense"] = 0

    monthly_data["Net Savings"] = (
        monthly_data["Income"] - monthly_data["Expense"]
    )

    st.subheader("Historical Financial Performance")

    st.dataframe(
        monthly_data,
        use_container_width=True,
        hide_index=True
    )

    # Calculate average daily spending
    expenses = df[df["type"] == "Expense"]

    daily_spending = (
        expenses.groupby(expenses["date"].dt.date)["amount"]
        .sum()
    )

    average_daily_spending = daily_spending.mean()

    # Simple 30-day spending estimate
    estimated_monthly_spending = average_daily_spending * 30

    st.subheader("30-Day Spending Estimate")

    col1, col2 = st.columns(2)

    col1.metric(
        "Average Daily Spending",
        f"₹{average_daily_spending:,.0f}"
    )

    col2.metric(
        "Estimated 30-Day Spending",
        f"₹{estimated_monthly_spending:,.0f}"
    )

    # Daily spending chart
    st.subheader("Daily Spending Trend")

    daily_data = (
        expenses.groupby(expenses["date"].dt.date)["amount"]
        .sum()
        .reset_index()
    )

    daily_data.columns = ["Date", "Spending"]

    forecast_chart = px.line(
        daily_data,
        x="Date",
        y="Spending",
        markers=True,
        title="Daily Expense Trend"
    )

    forecast_chart.update_layout(
        plot_bgcolor="white",
        paper_bgcolor="white",
        font_color="#17243A"
    )

    st.plotly_chart(
        forecast_chart,
        use_container_width=True
    )

    st.caption(
        "Note: This is a basic estimate using historical daily averages, "
        "not the final machine-learning forecast."
    )

elif page == "What-If Simulator":

    st.title("What-If Financial Simulator")
    st.write(
        "Experiment with financial decisions and see how they affect your savings."
    )

    df = get_sample_data()

    # Calculate current monthly baseline
    monthly_income = (
        df[df["type"] == "Income"]["amount"].sum()
    )

    monthly_expenses = (
        df[df["type"] == "Expense"]["amount"].sum()
    )

    current_savings = monthly_income - monthly_expenses

    st.subheader("Your Current Financial Position")

    col1, col2, col3 = st.columns(3)

    col1.metric("Income", f"₹{monthly_income:,.0f}")
    col2.metric("Expenses", f"₹{monthly_expenses:,.0f}")
    col3.metric("Net Balance", f"₹{current_savings:,.0f}")

    st.divider()

    st.subheader("Adjust Your Financial Decisions")

    # User-controlled simulation inputs
    income_change = st.slider(
        "Change in monthly income (%)",
        min_value=-50,
        max_value=100,
        value=0,
        step=5
    )

    expense_change = st.slider(
        "Change in monthly expenses (%)",
        min_value=-50,
        max_value=100,
        value=0,
        step=5
    )

    additional_expense = st.number_input(
        "Additional monthly expense (₹)",
        min_value=0,
        max_value=100000,
        value=0,
        step=500
    )

    # Calculate simulated financial position
    simulated_income = monthly_income * (1 + income_change / 100)

    simulated_expenses = (
        monthly_expenses * (1 + expense_change / 100)
        + additional_expense
    )

    simulated_savings = simulated_income - simulated_expenses

    savings_rate = (
        simulated_savings / simulated_income * 100
        if simulated_income > 0 else 0
    )

    st.divider()

    st.subheader("Simulation Results")

    col1, col2, col3 = st.columns(3)

    col1.metric(
        "Projected Income",
        f"₹{simulated_income:,.0f}",
        f"{income_change:+}%"
    )

    col2.metric(
        "Projected Expenses",
        f"₹{simulated_expenses:,.0f}",
        f"{expense_change:+}%"
    )

    col3.metric(
        "Projected Savings",
        f"₹{simulated_savings:,.0f}",
        f"₹{simulated_savings - current_savings:,.0f}"
    )

    st.metric(
        "Projected Savings Rate",
        f"{savings_rate:.1f}%"
    )

    # Compare current and simulated position
    comparison = pd.DataFrame({
        "Scenario": ["Current", "Simulated"],
        "Income": [monthly_income, simulated_income],
        "Expenses": [monthly_expenses, simulated_expenses],
        "Savings": [current_savings, simulated_savings]
    })

    comparison_chart = px.bar(
        comparison,
        x="Scenario",
        y=["Income", "Expenses", "Savings"],
        barmode="group",
        title="Current vs Simulated Financial Position",
        color_discrete_map={
            "Income": "#B99A60",
            "Expenses": "#263B58",
            "Savings": "#788397"
        }
    )

    comparison_chart.update_layout(
        plot_bgcolor="white",
        paper_bgcolor="white",
        font_color="#17243A"
    )

    st.plotly_chart(
        comparison_chart,
        use_container_width=True
    )

    if simulated_savings > current_savings:
        st.success(
            "This scenario improves your financial position!"
        )
    elif simulated_savings < current_savings:
        st.warning(
            "This scenario reduces your available savings."
        )
    else:
        st.info(
            "Your financial position remains unchanged."
        )

    st.caption(
        "This is a scenario-based financial estimate using sample data, "
        "not a prediction or financial recommendation."
    )

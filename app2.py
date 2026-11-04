import streamlit as st
import pandas as pd
import plotly.express as px

from sample_data import get_sample_data
from modules.anomaly_detector import detect_anomalies
from modules.anomaly_detector import explain_anomalies
from modules.forecasting import forecast_finances
from modules.financial_simulator import simulate_scenario

# ==========================================
# PAGE CONFIGURATION
# ==========================================

st.set_page_config(
    page_title="FinSim | Smart Finance",
    page_icon="💎",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ==========================================
# CUSTOM CSS
# ==========================================

st.markdown("""
<style>

@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');

.stApp {
    background: linear-gradient(135deg, #070B18, #0C1630, #101E3D);
    color: #FFFFFF;
    font-family: 'Inter', sans-serif;
}

header[data-testid="stHeader"] {
    background: transparent;
}

.block-container {
    padding-top: 2rem;
    max-width: 1250px;
}

h1, h2, h3, p, label {
    color: white;
}

.hero {
    text-align: center;
    padding: 90px 20px 35px 20px;
}

.hero h1 {
    font-size: 58px;
    font-weight: 800;
    line-height: 1.2;
}

.gradient-text {
    background: linear-gradient(90deg, #00D4FF, #4776FF);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}

.hero p {
    color: #AAB8D0;
    font-size: 17px;
    line-height: 1.8;
}

.badge {
    display: inline-block;
    background: rgba(0, 180, 255, 0.10);
    border: 1px solid rgba(0, 180, 255, 0.35);
    color: #45D5FF;
    padding: 10px 20px;
    border-radius: 30px;
    font-size: 12px;
    letter-spacing: 2px;
    margin-bottom: 25px;
}

.feature-card {
    background: linear-gradient(
        145deg,
        rgba(255,255,255,0.08),
        rgba(255,255,255,0.02)
    );
    border: 1px solid rgba(100,160,255,0.18);
    border-radius: 18px;
    padding: 25px;
    min-height: 195px;
    margin-bottom: 18px;
}

.feature-card:hover {
    border-color: #00BFFF;
}

.feature-icon {
    font-size: 32px;
}

.feature-card h3 {
    font-size: 19px;
    margin-top: 15px;
}

.feature-card p {
    color: #AAB8D0;
    font-size: 13px;
    line-height: 1.7;
}

.section-title {
    text-align: center;
    font-size: 32px;
    font-weight: 800;
    margin-bottom: 35px;
}

div.stButton > button {
    background: linear-gradient(90deg, #126BFF, #00C6FF);
    color: white;
    border: 0;
    border-radius: 10px;
    font-weight: 700;
    padding: 12px;
    transition: 0.3s;
}

div.stButton > button:hover {
    box-shadow: 0 0 22px rgba(0,180,255,0.45);
    border: 1px solid #75E4FF;
    color: white;
}

div[data-testid="stMetric"] {
    background: rgba(255,255,255,0.05);
    padding: 20px;
    border: 1px solid rgba(100,160,255,0.2);
    border-radius: 15px;
}

div[data-testid="stMetricValue"] {
    color: #40D5FF;
}

.footer {
    text-align: center;
    color: #71819D;
    padding: 50px 0 20px 0;
    font-size: 13px;
}

[data-testid="stSidebar"] {
    background: #0A1227;
}

</style>
""", unsafe_allow_html=True)


# ==========================================
# SESSION STATE
# ==========================================

if "page" not in st.session_state:
    st.session_state.page = "home"

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False


# ==========================================
# HOME PAGE
# ==========================================

def home_page():

    col1, col2, col3 = st.columns([5, 1, 1])

    with col1:
        st.markdown("## 💎 FinSim")

    with col2:
        if st.button("Home"):
            st.session_state.page = "home"
            st.rerun()

    with col3:
        if st.button("Login"):
            st.session_state.page = "login"
            st.rerun()
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


    a, b, c = st.columns([2, 1, 2])

    with b:
        if st.button("GET STARTED  →", use_container_width=True):
            st.session_state.page = "login"
            st.rerun()

    st.markdown("<br><br>", unsafe_allow_html=True)

    st.markdown(
        '<div class="section-title">Everything You Need. One Platform.</div>',
        unsafe_allow_html=True
    )

    features = [
        ("📊", "Overview", "Your complete financial picture in one interactive dashboard."),
        ("💳", "Transactions", "Track and organise your income and expenses."),
        ("🧠", "Spend Intelligence", "Understand your spending habits and patterns."),
        ("🔮", "Forecast", "Explore future financial trends and possibilities."),
        ("🧪", "What-If Lab", "Simulate decisions and compare financial scenarios."),
        ("✨", "Insights", "Discover meaningful insights for smarter decisions.")
    ]

    for row in range(2):
        cols = st.columns(3)

        for index, col in enumerate(cols):
            icon, title, description = features[row * 3 + index]

            with col:
                st.markdown(f"""
                <div class="feature-card">
                    <div class="feature-icon">{icon}</div>
                    <h3>{title}</h3>
                    <p>{description}</p>
                </div>
                """, unsafe_allow_html=True)

    st.markdown("""
    <div class="footer">
        💎 FINSIM | FINANCIAL SIMULATOR<br><br>
        Smarter Decisions. Better Financial Futures.
        <br><br>
        © 2026 FinSim Project
    </div>
    """, unsafe_allow_html=True)


# ==========================================
# LOGIN PAGE
# ==========================================

def login_page():

    st.markdown("<br><br>", unsafe_allow_html=True)

    left, center, right = st.columns([1, 1.4, 1])

    with center:

        st.markdown("""
        <div style="text-align:center;">
            <div style="font-size:55px;">💎</div>
            <h1>Welcome Back</h1>
            <p style="color:#AAB8D0;">
                Sign in to access your financial dashboard.
            </p>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("<br>", unsafe_allow_html=True)

        email = st.text_input(
            "Email Address",
            placeholder="Enter your email"
        )

        password = st.text_input(
            "Password",
            type="password",
            placeholder="Enter your password"
        )

        if st.button("SIGN IN  →", use_container_width=True):

            if email.strip() and password.strip():

                st.session_state.logged_in = True
                st.session_state.user_email = email
                st.session_state.page = "dashboard"
                st.rerun()

            else:
                st.error("Please enter your email and password.")

        st.markdown("<br>", unsafe_allow_html=True)

        if st.button("← Back to Home", use_container_width=True):
            st.session_state.page = "home"
            st.rerun()

        st.caption("Demo login: Enter any email and password.")


# ==========================================
# DASHBOARD
# ==========================================

def dashboard_page():

    st.sidebar.markdown("# 💎 FinSim")
    st.sidebar.caption("FINANCIAL SIMULATOR")

    st.sidebar.markdown("---")

    st.sidebar.write("NAVIGATION")

    menu = [
        "Overview",
        "Spend Intelligence",
        "Anomaly Detection",
        "Financial Forecast",
        "What-If Simulator"
    ]

    selected = st.sidebar.radio(
        "Go to",
        menu,
        label_visibility="collapsed"
    )

    st.sidebar.markdown("---")

    st.sidebar.write("👤 " + st.session_state.user_email)

    if st.sidebar.button("Logout", use_container_width=True):
        st.session_state.logged_in = False
        st.session_state.page = "home"
        st.rerun()

    st.markdown("## 💎 FinSim Dashboard")

    st.markdown(
        f"Welcome back, **{st.session_state.user_email}** 👋"
    )

    st.markdown("---")

    # OVERVIEW

    if selected == "Overview":

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


    # OTHER SECTIONS

    elif selected == "Spend Intelligence":

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

    elif selected == "Anomaly Detection":

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
    
    elif selected == "Financial Forecast":

        st.title("Financial Forecast")
        st.write(
            "Explore historical financial performance and "
            "predict your income, expenses and savings for "
            "the next 30 days."
        )

        df = get_sample_data()

        # --------------------------------
        # 1. Historical Financial Performance
        # --------------------------------

        monthly_data = (
            df.assign(month=df["date"].dt.to_period("M").astype(str))
            .groupby(["month", "type"])["amount"]
            .sum()
            .unstack(fill_value=0)
            .reset_index()
        )

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

        # --------------------------------
        # 2. Generate 30-Day Forecast
        # --------------------------------

        forecast_df = forecast_finances(
            df,
            forecast_days=30
        )

        st.subheader("30-Day Financial Forecast")

        total_income = forecast_df["predicted_income"].sum()
        total_expenses = forecast_df["predicted_expenses"].sum()
        total_savings = forecast_df["predicted_savings"].sum()

        col1, col2, col3 = st.columns(3)

        col1.metric(
            "Predicted Income",
            f"₹{total_income:,.0f}"
        )

        col2.metric(
            "Predicted Expenses",
            f"₹{total_expenses:,.0f}"
        )

        col3.metric(
            "Predicted Savings",
            f"₹{total_savings:,.0f}"
        )

        # --------------------------------
        # 3. Forecast Chart
        # --------------------------------

        st.subheader("Predicted Financial Trends")

        forecast_chart = px.line(
            forecast_df,
            x="date",
            y=[
                "predicted_income",
                "predicted_expenses",
                "predicted_savings"
            ],
            markers=True,
            title="30-Day Income, Expense and Savings Forecast",
            labels={
                "date": "Date",
                "value": "Amount (₹)",
                "variable": "Financial Metric"
            }
        )

        forecast_chart.update_layout(
            plot_bgcolor="white",
            paper_bgcolor="white",
            font_color="#17243A",
            legend_title_text="Financial Metric"
        )

        st.plotly_chart(
            forecast_chart,
            use_container_width=True
        )

        # --------------------------------
        # 4. Forecast Table
        # --------------------------------

        st.subheader("Daily Forecast Details")

        st.dataframe(
            forecast_df.round(2),
            use_container_width=True,
            hide_index=True
        )

        st.caption(
            "Forecasts are generated using Linear Regression "
            "on historical daily transaction totals. They are "
            "estimates, not guaranteed financial outcomes."
        )

        st.info(
            "The forecast is based on the historical data "
            "available in the uploaded dataset."
        )


    elif selected == "What-If Simulator":

        st.title("What-If Financial Simulator")

        st.write(
            "Explore how changes in your income and expenses "
            "could affect your monthly savings."
        )

        df = get_sample_data()

        st.subheader("Adjust Your Financial Scenario")

        col1, col2 = st.columns(2)

        with col1:
            income_change = st.slider(
                "Change in Income (%)",
                min_value=-50,
                max_value=100,
                value=0,
                step=5
            )

        with col2:
            expense_change = st.slider(
                "Change in Expenses (%)",
                min_value=-50,
                max_value=100,
                value=0,
                step=5
            )

        additional_expense = st.slider(
            "Additional Monthly Expense (₹)",
            min_value=0,
            max_value=50000,
            value=0,
            step=500
        )

        results = simulate_scenario(
            df,
            income_change_pct=income_change,
            expense_change_pct=expense_change,
            additional_expense=additional_expense
        )

        st.subheader("Your Financial Comparison")

        col1, col2, col3 = st.columns(3)

        col1.metric(
            "Monthly Income",
            f"₹{results['simulated_income']:,.0f}",
            f"{income_change:+}%"
        )

        col2.metric(
            "Monthly Expenses",
            f"₹{results['simulated_expenses']:,.0f}"
        )

        col3.metric(
            "Monthly Savings",
            f"₹{results['simulated_savings']:,.0f}"
        )

        comparison_data = pd.DataFrame({
            "Scenario": ["Current", "Simulated"],
            "Income": [
                results["current_income"],
                results["simulated_income"]
            ],
            "Expenses": [
                results["current_expenses"],
                results["simulated_expenses"]
            ],
            "Savings": [
                results["current_savings"],
                results["simulated_savings"]
            ]
        })

        comparison_chart = px.bar(
            comparison_data,
            x="Scenario",
            y=["Income", "Expenses", "Savings"],
            barmode="group",
            title="Current vs Simulated Financial Position",
            labels={
                "value": "Amount (₹)",
                "variable": "Financial Metric"
            }
        )

        st.plotly_chart(
            comparison_chart,
            use_container_width=True
        )

        st.subheader("Savings Rate")

        st.metric(
            "Simulated Savings Rate",
            f"{results['savings_rate']:.2f}%"
        )

        if results["simulated_savings"] >= 0:
            st.success(
                "Your simulated income covers your expenses. "
                "You have a positive savings balance."
            )
        else:
            st.warning(
                "Your simulated expenses are higher than your income. "
                "Consider adjusting your financial scenario."
            )

        st.caption(
            "Simulation results are estimates based on average monthly "
            "historical transactions. They are not guaranteed outcomes."
        )

# ==========================================
# PAGE ROUTING
# ==========================================

if st.session_state.page == "home":

    home_page()

elif st.session_state.page == "login":

    login_page()

elif st.session_state.page == "dashboard":

    if st.session_state.logged_in:
        dashboard_page()
    else:
        st.session_state.page = "login"
        st.rerun()
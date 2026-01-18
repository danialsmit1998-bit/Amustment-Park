import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
from plotly.subplots import make_subplots
import numpy as np
from datetime import datetime

# Page Configuration
st.set_page_config(
    page_title="Amusement Park Analytics Pro",
    page_icon="🎢",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Professional Theme CSS
st.markdown("""
    <style>
    * {
        margin: 0;
        padding: 0;
        box-sizing: border-box;
    }
    
    body {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    }
    
    .main {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding-top: 2rem;
    }
    
    /* Header Styling */
    .header-title {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        padding: 3rem 2rem;
        border-radius: 0;
        text-align: center;
        margin: -2rem -2rem 2rem -2rem;
        box-shadow: 0 12px 40px rgba(0, 0, 0, 0.15);
    }
    
    .header-title h1 {
        font-size: 3.5rem;
        font-weight: 900;
        margin-bottom: 0.5rem;
        text-shadow: 3px 3px 6px rgba(0, 0, 0, 0.3);
        letter-spacing: 1px;
    }
    
    .header-title p {
        font-size: 1.3rem;
        color: rgba(255, 255, 255, 0.95);
        font-weight: 300;
        letter-spacing: 0.5px;
    }
    
    /* Sidebar Styling */
    [data-testid="stSidebar"] {
        background: linear-gradient(180deg, #1a1a2e 0%, #16213e 100%);
    }
    
    [data-testid="stSidebar"] [data-testid="stMarkdownContainer"] {
        color: white;
    }
    
    .sidebar-header {
        color: white;
        font-size: 1.8rem;
        font-weight: 700;
        margin-bottom: 1rem;
        text-transform: uppercase;
        letter-spacing: 2px;
    }
    
    /* Country Selector Card */
    .country-selector-card {
        background: linear-gradient(135deg, rgba(255,255,255,0.98) 0%, rgba(248,249,250,0.98) 100%);
        padding: 1.5rem;
        border-radius: 15px;
        box-shadow: 0 10px 30px rgba(0, 0, 0, 0.2);
        margin-bottom: 1.5rem;
        border: 3px solid #667eea;
    }
    
    /* Metric Cards */
    .metric-card {
        background: linear-gradient(135deg, rgba(255,255,255,0.98) 0%, rgba(248,249,250,0.98) 100%);
        padding: 1.8rem;
        border-radius: 15px;
        border-left: 6px solid;
        box-shadow: 0 10px 25px rgba(0, 0, 0, 0.12);
        transition: all 0.4s ease;
        margin-bottom: 1.2rem;
    }
    
    .metric-card:hover {
        transform: translateY(-8px);
        box-shadow: 0 15px 35px rgba(0, 0, 0, 0.2);
    }
    
    .metric-value {
        font-size: 2.2rem;
        font-weight: 800;
        color: #667eea;
        margin: 0.7rem 0;
        letter-spacing: -1px;
    }
    
    .metric-label {
        font-size: 0.95rem;
        color: #555;
        font-weight: 700;
        text-transform: uppercase;
        letter-spacing: 0.7px;
    }
    
    /* Section Headers */
    .section-header {
        color: white;
        font-size: 2rem;
        font-weight: 800;
        margin: 2.5rem 0 1.5rem 0;
        padding: 1.2rem;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        border-radius: 12px;
        box-shadow: 0 6px 20px rgba(0, 0, 0, 0.15);
        border-left: 6px solid rgba(255, 255, 255, 0.3);
        letter-spacing: 0.5px;
    }
    
    /* Data Table */
    .dataframe {
        border-radius: 15px;
        overflow: hidden;
        box-shadow: 0 10px 30px rgba(0, 0, 0, 0.15);
    }
    
    /* Buttons */
    .stButton > button {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        border: none;
        border-radius: 10px;
        padding: 0.85rem 2.2rem;
        font-weight: 700;
        font-size: 1rem;
        transition: all 0.4s ease;
        box-shadow: 0 6px 20px rgba(102, 126, 234, 0.4);
        letter-spacing: 0.5px;
    }
    
    .stButton > button:hover {
        transform: translateY(-3px);
        box-shadow: 0 8px 25px rgba(102, 126, 234, 0.6);
    }
    
    /* Text Styling */
    .subtitle {
        color: #666;
        font-size: 1.15rem;
        margin-bottom: 1.5rem;
        font-weight: 500;
        letter-spacing: 0.3px;
    }
    
    .stat-box {
        background: white;
        padding: 2.2rem;
        border-radius: 15px;
        box-shadow: 0 10px 30px rgba(0, 0, 0, 0.12);
        margin: 1.5rem 0;
        border-top: 5px solid #667eea;
    }
    
    .stat-box h2 {
        letter-spacing: 0.5px;
    }
    
    /* Top Performers Card */
    .top-performer-card {
        background: linear-gradient(135deg, rgba(255,255,255,0.97) 0%, rgba(248,249,250,0.97) 100%);
        padding: 1.2rem;
        border-radius: 12px;
        margin-bottom: 1rem;
        border-left: 5px solid;
        box-shadow: 0 8px 20px rgba(0, 0, 0, 0.1);
        transition: all 0.3s ease;
    }
    
    .top-performer-card:hover {
        transform: translateX(5px);
        box-shadow: 0 10px 28px rgba(0, 0, 0, 0.15);
    }
    
    .top-performer-rank {
        font-weight: 800;
        font-size: 1.3rem;
        margin-bottom: 0.5rem;
    }
    
    .top-performer-name {
        font-weight: 700;
        color: #333;
        margin-bottom: 0.5rem;
        font-size: 1rem;
    }
    
    .top-performer-stats {
        color: #666;
        font-size: 0.85rem;
        line-height: 1.6;
    }
    
    /* Divider */
    .divider {
        height: 2px;
        background: linear-gradient(90deg, transparent, #667eea, transparent);
        margin: 2rem 0;
    }
    
    </style>
""", unsafe_allow_html=True)

# Load Data
try:
    df = pd.read_csv('Book1.csv', encoding='latin-1')
    # Remove any rows with NaN values in key columns
    df = df.dropna(subset=['country', 'category', 'park_name', 'price', 'per_year_visitors'])
    if df.empty:
        st.error("❌ Data file is empty after cleaning")
        st.stop()
except FileNotFoundError:
    st.error("❌ Data file 'Book1.csv' not found")
    st.stop()
except Exception as e:
    st.error(f"❌ Error loading data: {str(e)}")
    st.stop()

# Get Countries and Categories
countries = sorted([str(c).strip() for c in df['country'].unique() if pd.notna(c)])
categories = sorted([str(c).strip() for c in df['category'].unique() if pd.notna(c)])

# ==================== HEADER ====================
st.markdown("""
    <div class="header-title">
        <h1>🎢 AMUSEMENT PARK ANALYTICS PRO</h1>
        <p>Comprehensive Global Theme Park Performance & Market Intelligence Dashboard</p>
    </div>
""", unsafe_allow_html=True)

# ==================== SIDEBAR ====================
with st.sidebar:
    st.markdown('<div class="sidebar-header">🎯 DASHBOARD CONTROLS</div>', unsafe_allow_html=True)
    
    # Country Selector with enhanced UI
    st.markdown("---")
    st.markdown("### 🌍 Select Country")
    
    # Create a nice country selector
    selected_country = st.selectbox(
        "Choose a country to analyze",
        countries,
        index=0,
        key="country_select",
        help="Select a country to view detailed amusement park analytics"
    )
    
    # Display country info
    country_parks_count = len(df[df['country'] == selected_country])
    country_revenue = df[df['country'] == selected_country]['total_revenue_per_year(millions)'].sum()
    
    st.markdown(f"""
        <div class="country-selector-card">
            <div style="text-align: center;">
                <div style="font-size: 2.5rem; margin-bottom: 0.5rem;">🌐</div>
                <div style="font-size: 1.3rem; font-weight: 700; color: #667eea; margin-bottom: 0.5rem;">{selected_country.upper()}</div>
                <div style="color: #666; font-size: 0.9rem;">
                    <div>🏢 {country_parks_count} Parks</div>
                    <div>💰 ${country_revenue:.1f}M Revenue</div>
                </div>
            </div>
        </div>
    """, unsafe_allow_html=True)
    
    # Get categories for selected country
    country_categories = sorted(df[df['country'] == selected_country]['category'].unique())
    
    # Category Selector (Optional)
    st.markdown("---")
    st.markdown("### 🎪 Category Filter")
    show_all_categories = st.checkbox("Show All Categories", value=True, help="Toggle to filter by specific category")
    
    if show_all_categories:
        country_data = df[df['country'] == selected_country]
        selected_categories = country_categories
    else:
        selected_category = st.selectbox(
            "Select Specific Category",
            country_categories,
            index=0,
            help="Filter parks by category type"
        )
        country_data = df[(df['country'] == selected_country) & (df['category'] == selected_category)]
        selected_categories = [selected_category]
    
    if country_data.empty:
        st.error("❌ No data for this selection")
        st.stop()
    
    # Summary Section
    st.markdown("---")
    st.markdown('<div class="sidebar-header" style="font-size: 1.3rem; margin: 1rem 0;">📊 QUICK STATS</div>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    with col1:
        st.metric(
            "🏢 Parks",
            len(country_data),
            help="Total parks in selection"
        )
        st.metric(
            "💰 Avg Revenue",
            f"${country_data['total_revenue_per_year(millions)'].mean():.1f}M",
            help="Average annual revenue"
        )
    
    with col2:
        st.metric(
            "👥 Avg Visitors",
            f"{country_data['per_year_visitors'].mean():,.0f}",
            help="Average annual visitors"
        )
        st.metric(
            "⭐ Avg Rating",
            f"{country_data['revisit_rate_per_year'].mean():.1f}%",
            help="Average revisit rate"
        )
    
    # Additional insights
    st.markdown("---")
    st.markdown("### 📈 Market Insights")
    
    highest_revenue = country_data.loc[country_data['total_revenue_per_year(millions)'].idxmax()]
    most_visited = country_data.loc[country_data['per_year_visitors'].idxmax()]
    
    st.markdown(f"""
    **💎 Top Revenue Park:**
    {highest_revenue['park_name']} - ${highest_revenue['total_revenue_per_year(millions)']:.1f}M
    
    **👥 Most Visited Park:**
    {most_visited['park_name']} - {most_visited['per_year_visitors']:,} visitors/year
    """)


# ==================== MAIN CONTENT ====================

# Country Overview Card
st.markdown(f"""
    <div class="stat-box">
        <h2 style="color: #667eea; margin-bottom: 0.5rem;">🌍 {selected_country.upper()} - COMPREHENSIVE MARKET ANALYSIS</h2>
        <p class="subtitle">Real-time Performance Metrics & Strategic Insights for {len(country_data)} Leading Entertainment Venues</p>
        <div style="font-size: 0.9rem; color: #999;">Last Updated: {datetime.now().strftime('%B %d, %Y')}</div>
    </div>
""", unsafe_allow_html=True)

# ==================== KPI METRICS ====================
st.markdown('<div class="section-header">📊 KEY PERFORMANCE INDICATORS</div>', unsafe_allow_html=True)

kpi_col1, kpi_col2, kpi_col3, kpi_col4, kpi_col5 = st.columns(5)

with kpi_col1:
    total_parks = len(country_data)
    st.markdown(f"""
        <div class="metric-card" style="border-left-color: #667eea;">
            <div class="metric-label">🏢 Total Parks</div>
            <div class="metric-value">{total_parks}</div>
            <div style="font-size: 0.85rem; color: #999;">Active venues</div>
        </div>
    """, unsafe_allow_html=True)

with kpi_col2:
    avg_price = country_data['price'].mean()
    st.markdown(f"""
        <div class="metric-card" style="border-left-color: #764ba2;">
            <div class="metric-label">🎟️ Avg Entry Price</div>
            <div class="metric-value">${avg_price:,.0f}</div>
            <div style="font-size: 0.85rem; color: #999;">Per ticket</div>
        </div>
    """, unsafe_allow_html=True)

with kpi_col3:
    total_revenue = country_data['total_revenue_per_year(millions)'].sum()
    st.markdown(f"""
        <div class="metric-card" style="border-left-color: #f093fb;">
            <div class="metric-label">💵 Total Revenue</div>
            <div class="metric-value">${total_revenue:,.1f}M</div>
            <div style="font-size: 0.85rem; color: #999;">Annual combined</div>
        </div>
    """, unsafe_allow_html=True)

with kpi_col4:
    avg_visitors = country_data['per_year_visitors'].mean()
    st.markdown(f"""
        <div class="metric-card" style="border-left-color: #4facfe;">
            <div class="metric-label">👥 Avg Annual Visitors</div>
            <div class="metric-value">{avg_visitors:,.0f}</div>
            <div style="font-size: 0.85rem; color: #999;">Per park</div>
        </div>
    """, unsafe_allow_html=True)

with kpi_col5:
    avg_revisit = country_data['revisit_rate_per_year'].mean()
    st.markdown(f"""
        <div class="metric-card" style="border-left-color: #43e97b;">
            <div class="metric-label">🔄 Revisit Rate</div>
            <div class="metric-value">{avg_revisit:.1f}%</div>
            <div style="font-size: 0.85rem; color: #999;">Customer loyalty</div>
        </div>
    """, unsafe_allow_html=True)

st.markdown('<div class="divider"></div>', unsafe_allow_html=True)

# ==================== VISUAL ANALYTICS ====================
st.markdown('<div class="section-header">📈 ADVANCED ANALYTICS & MARKET INSIGHTS</div>', unsafe_allow_html=True)

# Row 1: Revenue Leaders & Category Mix
col1, col2 = st.columns(2)

with col1:
    # Top Parks by Revenue
    top_parks = country_data.nlargest(12, 'total_revenue_per_year(millions)')[['park_name', 'total_revenue_per_year(millions)']].sort_values('total_revenue_per_year(millions)')
    
    fig_revenue = go.Figure(data=[
        go.Bar(
            y=top_parks['park_name'],
            x=top_parks['total_revenue_per_year(millions)'],
            orientation='h',
            marker=dict(
                color=top_parks['total_revenue_per_year(millions)'],
                colorscale='Viridis',
                showscale=False
            ),
            text=top_parks['total_revenue_per_year(millions)'].apply(lambda x: f'${x:.1f}M'),
            textposition='outside'
        )
    ])
    fig_revenue.update_layout(
        title="💰 Top Parks by Annual Revenue",
        xaxis_title="Revenue (Millions $)",
        yaxis_title="Park Name",
        height=500,
        template="plotly_white",
        margin=dict(l=200, r=50, t=50, b=20),
        font=dict(size=11, color="#333", family="Arial"),
        plot_bgcolor="rgba(240,240,240,0.3)",
        xaxis_showgrid=True,
        xaxis_gridwidth=1,
        xaxis_gridcolor="rgba(0,0,0,0.05)"
    )
    st.plotly_chart(fig_revenue, use_container_width=True)

with col2:
    # Category Distribution
    category_dist = country_data['category'].value_counts()
    colors_pie = px.colors.qualitative.Set2
    
    fig_category = px.pie(
        values=category_dist.values,
        names=category_dist.index,
        title="🎪 Park Distribution by Category",
        color_discrete_sequence=colors_pie,
        hole=0.4
    )
    fig_category.update_traces(textposition='inside', textinfo='percent+label')
    fig_category.update_layout(
        height=500,
        template="plotly_white",
        font=dict(size=11, color="#333", family="Arial")
    )
    st.plotly_chart(fig_category, use_container_width=True)

st.markdown('<div class="divider"></div>', unsafe_allow_html=True)

# Row 2: Price vs Visitors & Revenue Analysis
col1, col2 = st.columns(2)

with col1:
    # Price vs Visitors Analysis
    fig_scatter = px.scatter(
        country_data,
        x='price',
        y='per_year_visitors',
        size='total_revenue_per_year(millions)',
        color='category',
        hover_name='park_name',
        hover_data={'price': ':.0f', 'per_year_visitors': ':,', 'category': True},
        title="💵 Entry Price vs Annual Visitors (Bubble Size = Revenue)",
        labels={"price": "Entry Price ($)", "per_year_visitors": "Annual Visitors"},
        size_max=80
    )
    fig_scatter.update_layout(
        height=500,
        template="plotly_white",
        font=dict(size=10, color="#333"),
        plot_bgcolor="rgba(240,240,240,0.3)",
        hovermode='closest'
    )
    st.plotly_chart(fig_scatter, use_container_width=True)

with col2:
    # Revenue Distribution by Category
    revenue_by_cat = country_data.groupby('category')['total_revenue_per_year(millions)'].agg(['sum', 'count']).sort_values('sum', ascending=False)
    
    fig_revenue_cat = px.bar(
        x=revenue_by_cat.index,
        y=revenue_by_cat['sum'],
        title="💰 Total Revenue by Category",
        labels={"x": "Category", "y": "Revenue (Millions $)", "sum": "Revenue"},
        color=revenue_by_cat['sum'],
        color_continuous_scale="RdYlGn",
        text_auto='.1f'
    )
    fig_revenue_cat.update_traces(textposition='outside')
    fig_revenue_cat.update_layout(
        height=500,
        template="plotly_white",
        showlegend=False,
        xaxis_tickangle=-45,
        font=dict(size=10, color="#333"),
        plot_bgcolor="rgba(240,240,240,0.3)",
        margin=dict(b=100)
    )
    st.plotly_chart(fig_revenue_cat, use_container_width=True)

st.markdown('<div class="divider"></div>', unsafe_allow_html=True)

# Row 3: Visitor Reviews & Revisit Rate Analysis
col1, col2 = st.columns(2)

with col1:
    # Visitor Reviews Distribution
    review_counts = country_data['visitor_reviews'].value_counts()
    review_order = ['excellent', 'very good', 'good', 'average', 'poor']
    review_counts = review_counts.reindex(review_order, fill_value=0)
    color_map = {'excellent': '#43e97b', 'very good': '#4facfe', 'good': '#f093fb', 'average': '#ffa502', 'poor': '#ff6b6b'}
    colors = [color_map.get(r, '#999') for r in review_counts.index]
    
    fig_reviews = px.bar(
        x=review_counts.index,
        y=review_counts.values,
        title="⭐ Visitor Review Ratings Distribution",
        labels={"x": "Rating", "y": "Number of Parks"},
        text_auto=True,
        color=review_counts.index,
        color_discrete_map=color_map
    )
    fig_reviews.update_traces(textposition='outside')
    fig_reviews.update_layout(
        height=450,
        template="plotly_white",
        showlegend=False,
        font=dict(size=11, color="#333"),
        plot_bgcolor="rgba(240,240,240,0.3)",
        xaxis_tickangle=-45
    )
    st.plotly_chart(fig_reviews, use_container_width=True)

with col2:
    # Revisit Rate Analysis
    fig_revisit = px.box(
        country_data,
        y='revisit_rate_per_year',
        x='category',
        title="📊 Revisit Rate Distribution by Category",
        labels={"revisit_rate_per_year": "Revisit Rate (%)", "category": "Category"},
        color='category',
        points="all"
    )
    fig_revisit.update_layout(
        height=450,
        template="plotly_white",
        showlegend=False,
        xaxis_tickangle=-45,
        font=dict(size=10, color="#333"),
        plot_bgcolor="rgba(240,240,240,0.3)"
    )
    st.plotly_chart(fig_revisit, use_container_width=True)

st.markdown('<div class="divider"></div>', unsafe_allow_html=True)

# ==================== TOP PERFORMERS ====================
st.markdown('<div class="section-header">🏆 TOP PERFORMERS & MARKET LEADERS</div>', unsafe_allow_html=True)

top_col1, top_col2, top_col3 = st.columns(3)

# Top Revenue Parks
with top_col1:
    st.markdown("### 💵 Revenue Champions")
    top_revenue_parks = country_data.nlargest(5, 'total_revenue_per_year(millions)')[['park_name', 'total_revenue_per_year(millions)', 'price']]
    
    for idx, (_, row) in enumerate(top_revenue_parks.iterrows(), 1):
        medal = "🥇" if idx == 1 else "🥈" if idx == 2 else "🥉" if idx == 3 else f"#{idx}"
        st.markdown(f"""
        <div class="top-performer-card" style="border-left-color: #667eea;">
            <div class="top-performer-rank">{medal}</div>
            <div class="top-performer-name">{row['park_name']}</div>
            <div class="top-performer-stats">
                💰 ${row['total_revenue_per_year(millions)']:.2f}M revenue<br>
                🎟️ ${row['price']:,.0f} entry price
            </div>
        </div>
        """, unsafe_allow_html=True)

# Most Visited Parks
with top_col2:
    st.markdown("### 👥 Visitor Favorites")
    top_visited_parks = country_data.nlargest(5, 'per_year_visitors')[['park_name', 'per_year_visitors', 'price']]
    
    for idx, (_, row) in enumerate(top_visited_parks.iterrows(), 1):
        medal = "🥇" if idx == 1 else "🥈" if idx == 2 else "🥉" if idx == 3 else f"#{idx}"
        st.markdown(f"""
        <div class="top-performer-card" style="border-left-color: #4facfe;">
            <div class="top-performer-rank">{medal}</div>
            <div class="top-performer-name">{row['park_name']}</div>
            <div class="top-performer-stats">
                👥 {row['per_year_visitors']:,} annual visitors<br>
                🎟️ ${row['price']:,.0f} entry price
            </div>
        </div>
        """, unsafe_allow_html=True)

# Best Rated Parks
with top_col3:
    st.markdown("### ⭐ Guest Satisfaction Leaders")
    rating_map = {'excellent': 5, 'very good': 4, 'good': 3, 'average': 2, 'poor': 1}
    country_data_copy = country_data.copy()
    country_data_copy['rating_score'] = country_data_copy['visitor_reviews'].map(rating_map)
    top_rated_parks = country_data_copy.nlargest(5, 'rating_score')[['park_name', 'visitor_reviews', 'revisit_rate_per_year']]
    
    for idx, (_, row) in enumerate(top_rated_parks.iterrows(), 1):
        medal = "🥇" if idx == 1 else "🥈" if idx == 2 else "🥉" if idx == 3 else f"#{idx}"
        st.markdown(f"""
        <div class="top-performer-card" style="border-left-color: #43e97b;">
            <div class="top-performer-rank">{medal}</div>
            <div class="top-performer-name">{row['park_name']}</div>
            <div class="top-performer-stats">
                ⭐ {row['visitor_reviews'].upper()} rating<br>
                🔄 {row['revisit_rate_per_year']:.1f}% revisit rate
            </div>
        </div>
        """, unsafe_allow_html=True)

st.markdown('<div class="divider"></div>', unsafe_allow_html=True)

# ==================== DETAILED DATA TABLE ====================
st.markdown('<div class="section-header">📋 COMPREHENSIVE PARK INFORMATION & DETAILED METRICS</div>', unsafe_allow_html=True)

# Prepare display data
display_data = country_data[['park_name', 'category', 'price', 'per_week_visitors2', 'per_year_visitors', 'total_revenue_per_year(millions)', 'visitor_reviews', 'revisit_rate_per_year']].copy()
display_data.columns = ['Park Name', 'Category', 'Entry Price ($)', 'Weekly Visitors', 'Annual Visitors', 'Revenue ($M)', 'Rating', 'Revisit Rate (%)']

# Sort by revenue
display_data = display_data.sort_values('Revenue ($M)', ascending=False).reset_index(drop=True)
display_data.index = display_data.index + 1

# Format columns
display_data['Entry Price ($)'] = display_data['Entry Price ($)'].apply(lambda x: f"${x:,.0f}")
display_data['Weekly Visitors'] = display_data['Weekly Visitors'].apply(lambda x: f"{x:,}")
display_data['Annual Visitors'] = display_data['Annual Visitors'].apply(lambda x: f"{x:,}")
display_data['Revenue ($M)'] = display_data['Revenue ($M)'].apply(lambda x: f"${x:.2f}M")
display_data['Revisit Rate (%)'] = display_data['Revisit Rate (%)'].apply(lambda x: f"{x:.1f}%")

# Display table
st.dataframe(
    display_data,
    use_container_width=True,
    height=min(400, len(display_data) * 30 + 50)
)

# Download button
csv_data = country_data.to_csv(index=False)
download_col1, download_col2, download_col3 = st.columns([1, 1, 2])

with download_col1:
    st.download_button(
        label="📥 Download CSV",
        data=csv_data,
        file_name=f"parks_{selected_country.lower().replace(' ', '_')}_{datetime.now().strftime('%Y%m%d')}.csv",
        mime="text/csv"
    )

st.markdown('<div class="divider"></div>', unsafe_allow_html=True)

# ==================== STATISTICAL SUMMARY ====================
st.markdown('<div class="section-header">📊 STATISTICAL ANALYSIS & CORRELATIONS</div>', unsafe_allow_html=True)

stats_col1, stats_col2, stats_col3 = st.columns(3)

with stats_col1:
    st.markdown("""
    ### Price Statistics
    """)
    st.markdown(f"""
    - **Min Entry Price:** ${country_data['price'].min():,.0f}
    - **Max Entry Price:** ${country_data['price'].max():,.0f}
    - **Avg Entry Price:** ${country_data['price'].mean():,.0f}
    - **Median Entry Price:** ${country_data['price'].median():,.0f}
    - **Price Range:** ${country_data['price'].max() - country_data['price'].min():,.0f}
    """)

with stats_col2:
    st.markdown("""
    ### Visitor Statistics
    """)
    st.markdown(f"""
    - **Min Annual Visitors:** {country_data['per_year_visitors'].min():,}
    - **Max Annual Visitors:** {country_data['per_year_visitors'].max():,}
    - **Avg Annual Visitors:** {country_data['per_year_visitors'].mean():,.0f}
    - **Median Annual Visitors:** {country_data['per_year_visitors'].median():,.0f}
    - **Total Visitors:** {country_data['per_year_visitors'].sum():,}
    """)

with stats_col3:
    st.markdown("""
    ### Revenue Statistics
    """)
    st.markdown(f"""
    - **Min Annual Revenue:** ${country_data['total_revenue_per_year(millions)'].min():.2f}M
    - **Max Annual Revenue:** ${country_data['total_revenue_per_year(millions)'].max():.2f}M
    - **Avg Annual Revenue:** ${country_data['total_revenue_per_year(millions)'].mean():.2f}M
    - **Median Annual Revenue:** ${country_data['total_revenue_per_year(millions)'].median():.2f}M
    - **Total Market Revenue:** ${country_data['total_revenue_per_year(millions)'].sum():.2f}M
    """)

st.markdown("---")

# ==================== FOOTER ====================
st.markdown("""
    <div style="text-align: center; color: white; padding: 2.5rem; margin-top: 3rem; background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); border-radius: 12px;">
        <p style="font-size: 1rem; font-weight: 700; letter-spacing: 1px;">
            🎢 AMUSEMENT PARK ANALYTICS PRO DASHBOARD
        </p>
        <p style="font-size: 0.9rem; opacity: 0.9; margin-top: 0.7rem;">
            Advanced Market Intelligence & Performance Analytics Platform
        </p>
        <p style="font-size: 0.8rem; opacity: 0.7; margin-top: 1rem;">
            📊 Real-time Global Entertainment Industry Analysis | 🌍 Multi-Country Coverage | 💼 Strategic Business Intelligence
        </p>
        <p style="font-size: 0.75rem; opacity: 0.6; margin-top: 1.2rem;">
            © 2026 | Last Updated: {datetime.now().strftime('%B %d, %Y at %H:%M')} | Data-Driven Decision Support System
        </p>
    </div>
""", unsafe_allow_html=True)

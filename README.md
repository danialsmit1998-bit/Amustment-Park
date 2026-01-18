# 🎢 Amusement Park Analytics Pro Dashboard

## Overview
A stunning, professional, interactive dashboard for comprehensive analysis of global amusement parks and theme park performance metrics. Built with Streamlit and Plotly for real-time data visualization and strategic business intelligence.

## Features

### 🌍 **Country-Based Analysis**
- **Dynamic Country Selector**: Choose from multiple countries with instant data filtering
- **Real-time Country Insights**: Quick statistics showing total parks, revenue, and visitor metrics for selected country
- **Category Filtering**: Toggle between viewing all categories or filtering by specific park type (theme park, water park, amusement park, etc.)

### 📊 **Key Performance Indicators (KPIs)**
Five main metrics displayed prominently:
- 🏢 **Total Parks**: Active entertainment venues in the region
- 🎟️ **Average Entry Price**: Mean ticket pricing across parks
- 💵 **Total Revenue**: Combined annual revenue in millions
- 👥 **Average Annual Visitors**: Mean visitor count per park
- 🔄 **Revisit Rate**: Average customer loyalty percentage

### 📈 **Advanced Analytics & Visualizations**

#### Revenue & Category Analysis
- **Top Parks by Revenue**: Horizontal bar chart showing top 12 parks sorted by annual revenue
- **Category Distribution**: Donut chart showing the breakdown of park types in the market

#### Market Performance
- **Price vs Visitors Correlation**: Interactive bubble chart showing relationship between entry price and visitor count (bubble size represents revenue)
- **Revenue by Category**: Bar chart showing total revenue contribution by park category

#### Customer Satisfaction
- **Review Ratings Distribution**: Bar chart showing visitor rating distribution (Excellent, Very Good, Good, Average, Poor)
- **Revisit Rate Analysis**: Box plot showing revisit rate trends across different park categories

### 🏆 **Top Performers**
Three ranking sections showing market leaders:
- **💵 Revenue Champions**: Top 5 parks by annual revenue with medal rankings
- **👥 Visitor Favorites**: Most visited parks with annual visitor counts
- **⭐ Guest Satisfaction Leaders**: Highest-rated parks with revisit rates

### 📋 **Comprehensive Data Table**
- Complete park listing with all metrics
- Sortable and searchable data
- Formatted numerical values for easy reading
- CSV download capability for further analysis

### 📊 **Statistical Summary**
Three-column statistical overview:
- **Price Statistics**: Min, max, average, median, and range
- **Visitor Statistics**: Min, max, average, median, and total
- **Revenue Statistics**: Min, max, average, median, and total market revenue

### 🎨 **Stunning UI/UX Design**
- **Professional Color Scheme**: Purple to blue gradient theme
- **Smooth Animations**: Hover effects on cards and charts
- **Responsive Layout**: Adapts to different screen sizes
- **High-Quality Typography**: Clean, modern font styling
- **Interactive Charts**: Hover tooltips, zoom, and pan capabilities
- **Dark Sidebar**: Professional dark navigation panel

## Dashboard Sections

### Sidebar (Left Panel)
- **Dashboard Controls**: Country and category selection
- **Country Info Card**: Visual representation of selected country metrics
- **Quick Stats**: At-a-glance KPIs in sidebar format
- **Market Insights**: Top revenue and most visited parks highlights

### Main Dashboard
1. **Header Section**: Eye-catching title and subtitle
2. **KPI Metrics**: Five key indicators in card format
3. **Advanced Analytics**: Six interactive Plotly visualizations
4. **Top Performers**: Three columns of ranked parks
5. **Data Table**: Comprehensive park information
6. **Statistical Analysis**: Detailed market statistics
7. **Professional Footer**: Updated timestamp and dashboard branding

## Data Metrics Included

### Per Park:
- Park name and category
- Entry price
- Weekly visitors
- Annual visitors
- Annual revenue (in millions)
- Visitor reviews (rating)
- Revisit rate (percentage)

### Countries Covered:
- India
- United States
- China
- Japan
- Australia
- South Korea
- Germany
- Thailand
- Malaysia
- Singapore
- And many more global markets!

## Technologies Used

- **Streamlit**: Interactive web app framework
- **Pandas**: Data processing and analysis
- **Plotly**: Interactive visualizations
- **NumPy**: Numerical computing
- **Python**: Core programming language

## How to Use

### Running the Dashboard
```bash
cd "d:\Dashboard\Amustment Park"
streamlit run app.py
```

### Accessing the Dashboard
- **Local**: http://localhost:8501
- **Network**: http://192.168.20.50:8501

### Interactive Features
1. **Select Country**: Use the dropdown in the sidebar to choose a country
2. **Filter by Category**: Toggle "Show All Categories" or select specific types
3. **Hover on Charts**: Get detailed information by hovering over visualizations
4. **Download Data**: Click "Download CSV" button to export filtered data
5. **Interact with Charts**: Zoom, pan, and toggle data series in Plotly charts

## Color Scheme
- **Primary**: #667eea (Purple)
- **Secondary**: #764ba2 (Dark Purple)
- **Accent**: #4facfe (Blue), #43e97b (Green), #f093fb (Pink)
- **Background**: White with gradient overlays
- **Text**: Dark gray (#333) on light backgrounds

## Key Insights Provided
- Market leaders by revenue and visitor count
- Price elasticity and visitor attraction relationships
- Customer satisfaction trends by park category
- Market segmentation and category performance
- Revenue concentration across park types
- Revisit rate trends as loyalty indicators

## Features Highlights

✨ **Professional Design**: Investment-grade dashboard aesthetics
📱 **Responsive**: Works seamlessly on desktop, tablet, and mobile
🔄 **Real-time**: Updates instantly when filters change
📊 **Data-Rich**: Comprehensive metrics and analytics
🎯 **Intuitive**: Easy navigation and clear labeling
💾 **Exportable**: Download data in CSV format
🌐 **Multi-Country**: Global entertainment industry analysis

## Future Enhancement Ideas
- Time-series trend analysis
- Market forecasting models
- Competitor benchmarking
- Seasonal visitor patterns
- Price optimization recommendations
- ROI analysis and profitability metrics

## Data Source
- **Dataset**: Book1.csv
- **Records**: 460+ amusement parks worldwide
- **Coverage**: Multiple countries and regions

## Support
For issues or feature requests, ensure:
1. Book1.csv is in the same directory as app.py
2. Python 3.7+ is installed
3. All required packages are installed (streamlit, pandas, plotly, numpy)

---

**Dashboard Version**: 2.0 Pro
**Last Updated**: January 2026
**Status**: Production Ready

🎢 Experience the Future of Theme Park Analytics! 🎢

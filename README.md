# End-to-End Azure Sales Pipeline Analytics Project  
### Azure Data Factory • Azure Databricks • Delta Lake • Azure SQL • Logic Apps • Azure Synapse • Power BI

This project showcases a **full-scale, production-ready Azure Data Engineering solution** built to transform raw CRM sales pipeline data into actionable business insights.  
It covers the **entire data lifecycle** — ingestion, orchestration, transformation, monitoring, storage, and analytics — using modern Azure services.

---

## 📘 **Project Architecture**

![Architecture](./img/architecture.png)

The solution integrates:

**Azure Data Factory (ADF)** – Orchestration, ingestion, Git integration
**Azure Data Lake Storage Gen2 (ADLS)** – Central data storage (crm-data folder)
**Azure Databricks** – Cleaning, transformation, schema standardization
**Delta Lake** – Optimized storage for curated datasets
**Azure Synapse Analytics** – SQL pools & serverless queries for advanced analytics, modeling, and downstream consumption
**Azure SQL Database** – Final analytic storage layer
**Logic Apps + Azure Monitor** – Alerts, operational monitoring
**Power BI** – Executive dashboards & insights

---

## **Source Data — CRM Sales Pipeline Dataset**

Raw CRM files stored in:

```

/raw-data

````

These include pipeline activities, company info, deals, products, sectors, and sales agent records.

Example raw data validation:

![Sales Pipeline Nulls](./img/salepipeline_nuls.png)

![Accounts Null](./img/accounts_null.png)

---

## 🏗️ **Azure Data Factory Pipelines**

ADF orchestrates ingestion & movement of all CRM files into Data Lake.

### **ADF Pipeline Overview**
![Pipeline Activity](./img/pipelineactivity.png)

### **Logic Apps Email Alerts**
Automated notifications for failures, SLA breaches, or missing files.

![Logic App](./img/logicapp.png)

### **Azure Monitor Integration**
Centralized pipeline monitoring & health tracking.

![Azure Monitor](./img/azuremonitor.png)

---

## 🔧 **Data Transformation with Azure Databricks & Delta Lake**

Transformation steps included:

- Handling nulls & missing values  
- Standardizing column names  
- Fixing date/time formats  
- Removing duplicates  
- Enforcing schema consistency  
- Joining/splitting complex fields  
- Mapping product → sector → revenue relationships  

Example:

![Data Mount](./img/data_mount.png)  
![Transformed Data](./img/transformed_data_azure.png)

Additionally, tables such as accounts, deals, and activities were cleaned and renamed:

![Renamed Accounts](./img/rename_accounts.png)  
![Data Dictionary](./img/rename_data_dictionary.png)

---

## 🗄️ **Azure SQL Database — Curated Analytical Layer**

Final curated tables loaded into Azure SQL for downstream BI consumption.

![View Tables](./img/view_tables.png)

---

# 📊 **Power BI Report — Sales Pipeline Insights Dashboard**

This dashboard tells the full story of sales performance, revenue, deal outcome trends, product strength, and sales agent effectiveness.

![Power BI Report](./img/PowerBI_report.png)
---

## 🟦 **1. Sales Agent Performance by Close Value**  
### *Clustered Bar Chart*

Shows which agents drive the most revenue and how they rank across deal closure values.  
This visual helps management:

- Identify top performers  
- Allocate leads based on strengths  
- Evaluate consistency across quarters  

---

## 🟦 **2. Total Sales by Month**
### *Line Chart*

Tracks month-by-month revenue trends using `close date` vs `close value`.  

This reveals:

- Peak sales periods  
- Slumps requiring intervention  
- Seasonal cycles  
- Pipeline forecasting opportunities  

---

## 🟦 **3. Revenue by Office Location**
### *Azure Maps Visual*

Displays geographical revenue distribution.

Helps answer:

- Which branches outperform others  
- Regional business strength  
- Areas requiring marketing spend or team reinforcement  

---

## 🟦 **4. Highest Revenue Companies**
### *Funnel Chart — Account by Revenue*

Highlights the top revenue-generating accounts across the pipeline.  
Useful for:

- Identifying strategic clients  
- Focusing on high-value relationships  
- Prioritizing account-based marketing (ABM) strategies  

---

## 🟦 **5. Product Wins Across Deal Stages**
### *Column Chart — Product vs Deal Stage*

Shows which products:

- Win the most deals  
- Lose the most deals  
- Maintain consistent performance across stages  

This helps leadership understand product-market fit.

---

## 🟦 **6. Revenue by Sector**
### *Donut Chart*

Provides a breakdown of revenue contribution across sectors.  
Useful for:

- Diversification analysis  
- Identifying strong/weak industries  
- Strategic repositioning  

---

# 🧮 **Power BI KPIs**

| KPI | Value | Definition |
|------|--------|------------|
| **Total Deals Closed** | **6,711** | Total close value across all deals |
| **Deals Won** | **4,238** | Close value where `deal_stage = "won"` |
| **Deals Lost** | **2,473** | Close value where `deal_stage = "lost"` |
| **Win Rate %** | **63%** | % of won deals out of total outcomes |

### **Win Rate DAX Measure**

```DAX
WinRate% =
DIVIDE(
    CALCULATE(
        COUNTROWS('Sales Pipeline'),
        'Sales Pipeline'[deal_stage] = "won"
    ),
    CALCULATE(
        COUNTROWS('Sales Pipeline'),
        'Sales Pipeline'[deal_stage] = "won"
            || 'Sales Pipeline'[deal_stage] = "lost"
    ),
    0
)
````

---

# 💡 **Why This Project Matters**

This project demonstrates end-to-end data engineering capability:

* Cloud ingestion strategy
* Pipeline orchestration
* Distributed data transformation
* Production data modeling
* Operational monitoring
* KPI-driven executive reporting

The final solution enables businesses to answer:

* *Which agents perform best?*
* *Which products win the most deals?*
* *Which regions generate the highest revenue?*
* *Are we improving win rates over time?*
* *How healthy is our sales pipeline?*

The project is production-grade and scalable — perfect for enterprise CRM analytics.

---

# 🧾 **Technologies Used**

* Azure Data Factory
* Azure Storage (ADLS Gen2)
* Azure Databricks
* PySpark / Delta Lake
* Azure SQL Database
* Azure Monitor
* Logic Apps
* Azure Synapse
* Power BI

---

# 🎯 **Conclusion**

This project takes a **raw CRM dataset** and transforms it into a **sales intelligence engine** powered by Azure.
It demonstrates cloud engineering excellence, real-world data pipelines, and actionable business insights — making it ideal for portfolios, interviews, and enterprise implementation.

---

# 🌐 **Contact / Portfolio**

For collaborations or technical inquiries, feel free to reach out or explore additional projects.

```

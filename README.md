#  End-to-End CRM Sales Pipeline Azure Data Engineering Project

### **Real-World Sales Pipeline Analytics | Azure Data Factory • Databricks • Synapse • Power BI**

This project demonstrates a **full-scale, production-focused Azure Data Engineering pipeline**, built to solve real business challenges in managing, transforming, securing, and analyzing sales pipeline data.

Whether you're preparing for **Azure Data Engineering interviews**, **Microsoft certifications**, or building a **strong portfolio**, this project delivers hands-on experience across the entire modern data lifecycle.

---

## 📌 **Why This Project Matters**

In fast-growing businesses, **sales pipeline data** is the heartbeat of revenue forecasting. Yet many organizations struggle with:

* Scattered or on-premises data silos
* Dirty, inconsistent datasets
* Poor visibility into sales performance
* Lack of automated alerts for failures
* Limited analytics capabilities

This project solves all of these pain points using a **cloud-native, scalable, secure Azure architecture**.

By the end, we transform raw CSV files into **cleaned, structured, query-ready tables** powering an **interactive Power BI dashboard** that drives real business decisions such as:

* Win rate trends
* Deal stage analysis
* Customer acquisition insights
* Sales team performance
* Revenue forecasting

---

# 🏗️ **Architecture Overview**

Below is the end-to-end architecture implemented in this project:

![Architecture](img/architecture.png)

### **Architecture Components**

* **On-Premises CSV Data**
* **Azure Data Factory**

  * Git-enabled development
  * Self-Hosted Integration Runtime
* **Azure Data Lake Storage Gen2** (Bronze → Silver → Gold layers)
* **Logic Apps** for pipeline failure notifications
* **Azure Monitor** for operational observability
* **Azure Databricks** for transformations
* **Azure Key Vault + Secret Scopes** for secure credentials
* **Azure Synapse Analytics** for analysis
* **Power BI** for reporting

---

# 🎯 **What You’ll Learn**

This project covers **eight major Azure skills** every Data Engineer must master:

### **1️⃣ Move On-Prem Data to Cloud using Azure Data Factory**

* Built a Self-Hosted Integration Runtime
* Configured pipelines for ingestion
* Automated folder-based CSV ingestion

![Pipeline Activity](img/pipelineactivity.png)

---

### **2️⃣ Enable Git Integration for Version Control**

Git integration ensures:

* CI/CD readiness
* Change tracking
* Collaboration across teams

---

### **3️⃣ Manage Data with Azure Data Lake Gen2**

Data is organized using a medallion architecture:

* **Bronze** — Raw landing zone
* **Silver** — Cleaned and standardized
* **Gold** — Analytics-ready tables

![Renamed Data Dictionary](img/rename_data_dictionary.png)
![Renamed Accounts](img/rename_accounts.png)

---

### **4️⃣ Implement Automated Alerts with Logic Apps + Azure Monitor**

Failures trigger:

* Email Notifications
* Monitoring logs

This increases **reliability** and reduces downtime.

**Logic App:**

![Logic App](img/logicapp.png)

**Azure Monitor:**

![Azure Monitor](img/azuremonitir.png)

---

### **5️⃣ Clean & Transform Data in Azure Databricks**

Databricks performs:

* Null handling
* Schema standardization
* Data type corrections
* Deduplication
* Business logic transformations

**Handling Nulls Example:**

![Accounts Nulls](img/accounts_null.png)
![Sales Pipeline Nulls](img/salepipeline_nuls.png)

**Mounted Storage:**

![Data Mount](img/data_mount.png)

**Transformed Data in Azure:**

![Transformed Data Azure](img/transformed_data_azure.png)

---

### **6️⃣ Secure Credentials with Azure Key Vault + Secret Scopes**

No hardcoded secrets.
Databricks uses a **secure secret scope** to access:

* Storage Keys
* Database Credentials
* SAS Tokens

This follows cloud security best practices.

---

### **7️⃣ Load Clean Data into Azure Synapse Analytics**

Synapse provides:

* Serverless SQL queries
* Scalable analytics
* Ability to connect downstream to Power BI

![View Tables](img/view_tables.png)

---

### **8️⃣ Build Interactive Dashboards with Power BI**

Final visualizations include:

* Win Rate%
* Sales Funnel Performance
* Deals Won vs Lost
* Customer Segmentation
* Revenue by Region / Account Manager

These insights help organizations:

* Improve sales strategy
* Identify bottlenecks
* Predict revenue
* Strengthen decision-making

---

# 🔥 **Business Impact of This Project**

This solution directly supports business growth by:

### ✔️ Ensuring accurate sales forecasting

### ✔️ Reducing manual data preparation

### ✔️ Improving visibility across the sales lifecycle

### ✔️ Providing automated monitoring & alerts

### ✔️ Enabling real-time analytics for decision-makers

### ✔️ Bringing enterprise-grade security and scalability

For any organization, especially those with growing sales teams, this solution becomes a **strategic asset**.

---

# 🧠 **Who This Project Is For**

* Aspiring & Professional **Data Engineers**
* Azure Certification Candidates
* Cloud Engineers
* Anyone building a **high-value portfolio**
* Organizations needing scalable data pipelines

---

# 🧪 **Technologies Used**

| Category        | Tools                                    |
| --------------- | ---------------------------------------- |
| Cloud Storage   | Azure Data Lake Gen2                     |
| Ingestion       | Azure Data Factory                       |
| Orchestration   | Logic Apps, Azure Monitor                |
| Processing      | Azure Databricks                         |
| Security        | Azure Key Vault, Databricks Secret Scope |
| Analytics       | Azure Synapse Analytics                  |
| Visualization   | Power BI                                 |
| Version Control | Git Integration                          |

---

# 📘 **How to Use This Project**

1. Clone the repo
2. Deploy the ADF JSON pipelines
3. Run the Databricks notebooks
4. Configure Key Vault + Secret Scope
5. Publish data to Synapse
6. Connect Power BI for reporting

Everything is modular so you can reuse components for your own projects.

---

# 🏁 **Final Thoughts**

This project is a **realistic, enterprise-grade, interview-ready** Azure Data Engineering solution.
It demonstrates your ability to build a **complete data lifecycle** — from ingestion to visualization — while applying best practices across governance, monitoring, transformation, and analytics.

If you're working towards **Azure Data Engineer Associate**, **Fabric Analyst**, or building a strong **GitHub portfolio**, this project checks every box.

---

---
title: Vision and Scope Document
project: LocalStore POS
version: 1.1 (Detailed Draft)
date: 2026-01-18
author: Business Analyst Team
template_source: "Software Requirements, 3rd Edition (Wiegers & Beatty) - Chapter 5"
---

# VISION AND SCOPE DOCUMENT
**Project:** LocalStore POS (Point of Sale)

---

## 1. BUSINESS REQUIREMENTS

### 1.1. Background
Currently, many small-scale local retail stores still manage inventory and operational revenue using manual ledgers, sticky notes, or disjointed Excel files. This fragmented approach leads to several critical issues:
*   **Inventory Blindness:** Store owners cannot instantly know the exact stock quantity of a specific item, leading to unannounced stockouts or overstocking of slow-moving items.
*   **Revenue Leakage:** Without a standardized recording system, sales transactions can be missed, miscalculated, or manipulated, causing discrepancy between actual cash and recorded revenue.
*   **Inefficient Checkout:** Manual price lookup and calculation slow down the checkout process during peak hours, reducing customer satisfaction.
*   **Lack of Insight:** End-of-day/month balancing is purely manual and time-consuming; owners lack data-driven insights on "Best Sellers" or "Profit Margins" to make purchasing decisions.

The **LocalStore POS** project has been re-oriented to strictly resolve these core issues by providing a centralized digital solution focused on **Inventory Transparency, Fast Sales Execution, and Accurate Revenue Reporting**.

### 1.2. Business Opportunity
Implementing LocalStore POS addresses the immediate needs of store owners for control and efficiency:
*   **Digital Transformation:** Moving from "pen and paper" to a digital database ensures data persistence and accuracy.
*   **Operational Speed:** Automating the checkout process with barcode scanning and auto-calculation reduces customer wait time significantly.
*   **Loss Prevention:** Strict inventory tracking (Input vs. Output) minimizes goods loss due to theft or mismanagement.
*   **Smart Decision Making:** Real-time dashboards provide instant visibility into financial health, allowing owners to restock the right products at the right time.

### 1.3. Business Objectives
The system aims to achieve the following tangible goals within 3 months of deployment:
*   **BO-1 (Inventory Accuracy):** Reduce the inventory discrepancy rate (System vs. Physical) to under **1%** through strict import/export workflows and barcode verification.
*   **BO-2 (Checkout Efficiency):** Accelerate the average order processing speed at the counter to under **30 seconds per transaction** (from scanning to bill printing).
*   **BO-3 (Revenue Visibility):** Provide **Real-time** Profit & Loss reporting, completely eliminating the 1-2 hours typically spent on manual end-of-day ledger tallying.
*   **BO-4 (Zero Downtime):** Ensure the sales process is uninterrupted even during high-traffic periods through a lightweight and stable architecture.

### 1.4. Success Metrics
Project success will be measured by the following quantitative metrics:
*   **SM-1:** 100% of valuable product details (Price, Cost, Stock) are digitized and accessible via the system.
*   **SM-2:** 95% of sales staff can independently operate the POS sales screen without supervision after receiving 30 minutes of training.
*   **SM-3:** Key financial reports (Daily Revenue) are generated instantaneously (latency < 2 seconds) upon request.
*   **SM-4:** 100% of sales transactions are recorded with audit trails (Who sold, When, What items), enabling full traceability.

### 1.5. Vision Statement
> *"For retail store owners and Shop Managers who prioritize business efficiency and cash flow transparency, **LocalStore POS** is a specialized management system focused strictly on **Inventory and Revenue**. Unlike 'bulky' generic POS systems that are cluttered with unnecessary HR or complex accounting features, LocalStore POS optimizes the core operational loop: **Rapid Import -> Instant Sell -> Accurate Report**. Our product guarantees that store owners always know exactly what they have in stock and how much profit they made today, effortlessly."*

### 1.6. Business Risks
*   **RI-1 (Adoption Resistance):** Older staff members may struggle with using computers/barcode scanners compared to manual calculators.
    *   *Mitigation:* Design an extremely simplified, high-contrast User Interface (UI) for the Checkout screen, minimizing required clicks. Provide "Hands-on" training.
*   **RI-2 (Hardware Compatibility):** Diverse variety of cheap barcode scanners/printers in the market might cause driver conflicts.
    *   *Mitigation:* Standardize on "Plug-and-Play" HID-compliant hardware protocols. Publish a list of "Recommended Hardware".
*   **RI-3 (Data Loss):** Local hardware failure (PC crash) could lead to loss of sales data if not backed up.
    *   *Mitigation:* Implement cloud-sync capabilities or automated daily local backups to an external drive/secondary partition.

### 1.7. Business Assumptions and Dependencies
*   **AS-1:** The store is equipped with a stable internet connection (for web-based access) and basic computer hardware (PC/Laptop).
*   **AS-2:** Store owners are willing to perform an initial "Physical Stock Take" to populate the database with accurate starting quantities.
*   **DE-1:** The project relies on the finalized database schema design (G6_RDS) to ensure data integrity constraints are met from Day 1.

---

## 2. SCOPE AND LIMITATIONS

### 2.1. Major Features
The system is functionally organized into 4 main feature groups:

*   **FE-1: Inventory & Product Management (The Foundation)**
    *   **Product CRUD:** Create and maintain detailed product profiles (Name, Barcode, Selling Price, Cost Price, Unit, Category, Image).
    *   **Stock Management:**
        *   **Import Goods:** Record incoming stock from suppliers (updates quantity and cost price).
        *   **Stock Adjustment:** Manual correction for damaged/lost goods.
    *   **Low Stock Alert:** Visual indicators when item quantity falls below a defined threshold.

*   **FE-2: Sales & POS Operation (The Core)**
    *   **Checkout Screen:** Optimized interface for speed. Supports:
        *   Barcode scanning (via USB scanner).
        *   Quick product search by name/code.
        *   Quantity adjustment.
    *   **Transaction Processing:** Auto-calculate total, change due, and finalize order.
    *   **Receipt Printing:** Generate standardized thermal receipts (58mm/80mm) for customers.
    *   **Return/Refund:** Process returns with reason codes and update inventory automatically.

*   **FE-3: Reporting & Analytics (The Insight)**
    *   **Revenue Reports:** Aggregated sales views by Day, Week, Month, or Custom Range.
    *   **Best-Seller Analysis:** Indentify Top 10 performing products by quantity or revenue.
    *   **Profit Estimates:** Approximate profit calculation (Revenue - Cost of Goods Sold) to gauge business health.

*   **FE-4: System Administration (The Control)**
    *   **User Management:** Create accounts for Owner (Admin) and Staff (Cashier).
    *   **Basic Auth:** Secure Login/Logout mechanism.
    *   **Settings:** Configure store details (Name, Address, Phone) to appear on receipts.

### 2.2. Scope of Initial and Subsequent Releases
The roadmap prioritizes core transactional stability before advanced features.

| Feature Group | Release 1.0 (Foundation - MVP) | Release 2.0 (Growth - Future) |
| :--- | :--- | :--- |
| **Inventory** | **Basic:** Single Unit, standard stock tracking. | **Advanced:** Multi-unit conversion (e.g., Box -> Pieces), Batch/Expiry Date tracking. |
| **Sales POS** | **Online Mode:** Web-based checkout, standard USB scanner support. | **Offline Mode:** LocalStorage support when internet is down. Electronic Scale integration. |
| **Reporting** | **Static Tables:** Grid views, basic totals. | **Visual:** Interactive Charts, Graphs, and Export to Excel/PDF. |
| **Customer** | **Generic:** Walk-in customers only. | **Loyalty:** Member point accumulation, Customer history. |
| **Promotions** | **Manual:** Cashier enters discount amount manually. | **Auto:** System-applied rules (Buy 1 Get 1, Happy Hour). |

### 2.3. Limitations and Exclusions
*   **EX-1 (No Accounting Depth):** The system records sales revenue but is **NOT** a full accounting system. It does not handle tax filing, balance sheets, or detailed expenses (rent, electricity).
*   **EX-2 (No HR/Payroll):** As requested, features related to Employee Shift Scheduling, Timekeeping, and Salary Calculation are strictly **EXCLUDED**.
*   **EX-3 (No Multi-Store Sync):** Release 1.0 is designed for a **Single Store** architecture. Multi-branch inventory syncing is out of scope.
*   **EX-4 (No E-commerce):** This is an in-store POS. It does not integrate with online sales channels (Shopee, Website).

---

## 3. BUSINESS CONTEXT

### 3.1. Stakeholder Profiles

### 3.1. Stakeholder Profiles & External Entities

**Human Stakeholders:**

| Stakeholder | Value/Benefit | Attitude | Key Interests | Constraints |
| :--- | :--- | :--- | :--- | :--- |
| **Manager (Owner)** | Full oversight of operations; Data-driven decision making. | Strongly supportive (Driver). | Revenue reports, Employee mgmt, Product maintenance. | Limited time for deep technical administration. |
| **Warehouse Staff** | Accurate stock control; Efficient receiving process. | Cooperative. | Easy Import/Export flow, clear stock levels. | Needs clear distinction from Sales functions. |
| **Cashier** | Fast, error-free sales processing. | Focused on efficiency. | Ease of use (few clicks), checkout speed, clear shift end. | High pressure during peak hours. |

**Hardware & External Services:**

| Entity | Description | Interaction |
| :--- | :--- | :--- |
| **Barcode Scanner** | Hardware device for identifying products. | Sends barcode data -> System (for item lookup). |
| **Printer** | Hardware device for outputting receipts. | System sends invoice data -> Printer. |
| **Payment Service** | External payment handling component. | System sends request -> Service returns confirmation. |
| **SMS/Gmail Gateway** | External communication service. | System sends OTP/Alerts -> Gateway -> User. |

### 3.2. Project Priorities

| Dimension | Constraint (Must adhere to) | Driver (Key success factor) | Degree of Freedom (Adjustable) |
| :--- | :--- | :--- | :--- |
| **Quality** | **Data Integrity:** Zero tolerance for inventory/revenue calculation errors. | | |
| **Schedule** | | **Release 1.0** must be ready for UAT by [Date]. | |
| **Budget** | Minimal infrastructure cost (utilize existing PC). | | |
| **Features** | | **Checkout Speed** & **Stock Accuracy**. | "Nice-to-have" UI animations or advanced filters can be cut. |
| **Usability** | | Zero-training interface for cashiers. | |

### 3.3. Deployment Considerations
*   **Hardware Setup:**
    *   System runs on a standard Windows PC/Laptop or Tablet via Browser.
    *   Peripherals: USB Barcode Scanner (HID Mode) and Thermal Receipt Printer (USB/LAN).
*   **Data Migration (Critical):**
    *   The system must provide an **"Import from Excel"** feature for Products. Manually entering 1000+ items is a blocker for adoption.
    *   Initial "Stock Take" strategy must be planned with the store owner before Go-Live.
*   **Training Plan:**
    *   **Owner Training:** Focus on Product creation, Import, and Report interpretation.
    *   **Staff Training:** Focus strictly on Checkout flow, Search, and Refund processing.

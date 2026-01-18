# Vision and Scope Document
**Project:** LocalStore POS  
**Version:** 1.0 (Draft)  
**Status:** In Progress  

---

## 1. Business Requirements

### 1.1. Background
Currently, many small-scale local retail stores still manage inventory and revenue using manual ledgers or disjointed Excel files. Failure to grasp accurate stock levels and real-time actual revenue leads to goods loss, unannounced stockouts, and difficulty in evaluating business performance. The **LocalStore POS** project has been re-oriented to strictly resolve the core issues: **Inventory - Sales - Revenue**.

### 1.2. Business Opportunity
Store owners need a simple yet effective tool to control cash flow and goods flow. They do not need complex HR management features (like timekeeping, shift scheduling) but require absolute accuracy in stock figures and sales speed. The opportunity lies in providing a POS system maximizing the fast selling experience and intelligent reporting, helping owners immediately answer: "How much did we sell today?" and "How much stock is left?".

### 1.3. Business Objectives
*   **BO-1:** Reduce inventory discrepancy rate to under 1% after 2 months of deployment thanks to strict import/export processes.
*   **BO-2:** Accelerate order processing speed at the checkout counter, aiming for under 30 seconds per order.
*   **BO-3:** Provide real-time Revenue and Profit reporting, completely eliminating manual end-of-day tallying.

### 1.4. Success Metrics
*   **SM-1:** 100% of sales transactions are recorded in the system and inventory is deducted automatically and immediately.
*   **SM-2:** Daily revenue report is generated accurately with just 1 click.
*   **SM-3:** Training time for new staff to use sales features is under 30 minutes.

### 1.5. Vision Statement
For retail store owners prioritizing business efficiency and cash flow transparency, **LocalStore POS** is a management system focused on Inventory and Revenue. Unlike "bulky" POS systems integrated with too many unnecessary HR administration features, **LocalStore POS** optimizes the core processes: Fast Import - Quick Sell - Accurate Report.

### 1.6. Business Risks
*   **RI-1:** End-users (sales staff) may encounter difficulties if the admin interface is too complex or overly technical.
*   **RI-2:** Integration with specific POS hardware (printers, cash drawers) may encounter unforeseen driver errors.
*   **RI-3:** Data security risks if the authorization mechanism is not thoroughly tested.

### 1.7. Business Assumptions and Dependencies
*   **AS-1:** The store has a stable internet network infrastructure.
*   **AS-2:** The System Administrator has basic knowledge of the store's business processes.
*   **DE-1:** The project depends on the completion of the Database Schema design (as described in the G6_RDS document) before logic coding can begin.

---

## 2. Scope and Limitations

### 2.1. Major Features
*   **Inventory & Stock Management (Core):**
    *   Product List Management (Name, Price, Barcode, Image).
    *   Import and Export Management.
    *   Low stock alerts.
*   **Sales & POS (Core):**
    *   Sales Screen (Checkout) supporting barcode scanning.
    *   Invoice creation, calculation, bill printing.
    *   Return/Refund handling.
*   **Reporting & Analytics:**
    *   Revenue Statistics by Day/Week/Month.
    *   Top-selling products report.
    *   Profit Report (Revenue - Cost of Goods Sold).

### 2.2. Scope of Initial and Subsequent Releases

| Feature | Initial Release (v1.0) | Subsequent Releases (v1.x -> v2.0) |
| :--- | :--- | :--- |
| **Inventory** | Product CRUD, Basic Stock Update | Batch/Date Management, Multi-Unit Management |
| **Sales** | Retail Invoice Creation, Barcode Scanning, Bill Printing | Offline Sales, Electronic Scale Integration |
| **Reporting** | Aggregate Revenue, Invoice History | Trend Analysis, Reorder Forecasting |
| **Other Admin** | Simple Login (Owner/Staff) | Detailed Permissions, Audit Logs |

> *Note: Based on the provided G6_RDS document, the first version focuses heavily on the administrative framework (Admin/Back-office).*

### 2.3. Limitations and Exclusions
*   **L-1:** The first version does not support Offline sales (when internet is lost).
*   **L-2:** Online payment gateway integration (Momo, VNPay) is not included in this stage.
*   **E-1:** CRM features (Loyalty Management) are excluded from Release 1.0.

---

## 3. Business Context

### 3.1. Stakeholder Profiles

| Stakeholder | Value/Benefit | Attitude | Key Interests | Constraints |
| :--- | :--- | :--- | :--- | :--- |
| **Shop Owner** | Full operational control, reduced loss. | Strong supporter | Revenue reports, System security, Cost reduction. | Budget for new hardware. |
| **Administrator** | Centralized management tool, easy system configuration. | Supportive but wary of complexity | User Management, Data Integrity, Ease of config. | Time needed for initial setup. |
| **Sales Staff** | (Future) Streamlined sales process. | Potential resistance to change | Ease of use, Stability, Speed of checkout. | Limited technical skills. |

### 3.2. Project Priorities

| Dimension | Driver (State Objective) | Constraint (State Limit) | Degree of Freedom (State Allowable Range) |
| :--- | :--- | :--- | :--- |
| **Schedule** | | Release 1.0 to be completed by [Date] (Foundation Phase) | |
| **Features** | | | 70% of non-core Admin features can be deferred to v1.1 |
| **Quality** | Data Integrity and Security must be impeccable (0% critical data errors) | | |
| **Cost** | | Minimal infrastructure cost (utilize existing hardware) | |
| **Staff** | | Team size fixed at current capacity | |

### 3.3. Deployment Considerations
*   **Environment:** Web Application (Java-based backend).
*   **Access:** Access via internal web browser or public internet (HTTPS configuration required).
*   **Training:** User manuals needed for Admins on Initial Data Setup.

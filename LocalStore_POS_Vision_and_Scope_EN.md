# Vision and Scope Document
**Project:** LocalStore POS  
**Version:** 1.0 (Draft)  
**Status:** In Progress  

---

## 1. Business Requirements

### 1.1. Background
Currently, many small-scale local retail stores operate using manual processes or disjointed, non-synchronized management tools. Employee management, shift tracking, and regular system status updates are prone to errors, leading to revenue loss and difficulties in scaling. The **LocalStore POS** project was initiated to provide a centralized sales management solution, modernizing operations for these stores.

### 1.2. Business Opportunity
Store owners need a reliable system to manage not just sales transactions but also platform administration (Master Data) and strict employee authorization. The business opportunity lies in providing a lean, easy-to-use POS platform that possesses strong administrative controls (Admin features), which free solutions on the market often lack. This system will address:
*   Strict control of employee access rights.
*   Flexible management of system parameters (Settings/Master Data) without code intervention.
*   A foundation for future chain expansion.

### 1.3. Business Objectives
*   **BO-1:** Reduce time spent on user administration and employee authorization by 50% within the first month of deployment.
*   **BO-2:** Ensure 100% of system configuration changes (Settings/Status) are performed via the Admin interface, completely eliminating direct database edits.
*   **BO-3:** Provide a secure authentication mechanism (Password/OTP) to reduce unauthorized access risks to below 1%.

### 1.4. Success Metrics
*   **SM-1:** System operates stably with > 500 sample data records (Packages/Settings) without Data Integrity errors.
*   **SM-2:** 100% of Administrators can independently perform "Add New Master Data" operations without guidance after one training session.
*   **SM-3:** Response time for list management functions (User List, Setting List) is under 2 seconds.

### 1.5. Vision Statement
For retail store owners and Shop Managers who need strict and flexible control over their operational systems, **LocalStore POS** is a comprehensive sales management solution. Unlike rigid traditional POS systems, **LocalStore POS** focuses on building a strong administrative foundation (Strong Admin Foundation), allowing for customization of operational statuses and detailed authorization, helping businesses operate smoothly and securely.

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
*   **System Administration (Core):**
    *   Admin Dashboard.
    *   Setting List Management: View, Add New, Update Status (Active/Inactive), Filter by type.
*   **User Management:**
    *   New User Registration.
    *   User List Management with detailed info (Role, Status).
    *   Login/Logout and Authentication mechanisms (OTP/Password).
*   **Master Data Management:**
    *   CRUD (Create, Read, Update, Soft Delete) for Master Data entities (Packages, Categories...).

### 2.2. Scope of Initial and Subsequent Releases

| Feature | Initial Release (v1.0) | Subsequent Releases (v1.x -> v2.0) |
| :--- | :--- | :--- |
| **User Mgmt** | Registration, Login, User List (View/Edit Status) | Dynamic Role-based Access Control, User Profile Picture |
| **System Setting** | Basic parameter configuration, Status Act/Inact | UI Configuration (Theme), Multi-language support |
| **POS Feature** | (Not in core scope of current RDS) | Checkout Screen, Invoice Printing, Inventory Management |
| **Reporting** | Grid View Reports | Revenue Charts, Excel/PDF Export |

> *Note: Based on the provided G6_RDS document, the first version focuses heavily on the administrative framework (Admin/Back-office).*

### 2.3. Limitations and Exclusions
*   **L-1:** The first version does not support Offline sales (when internet is lost).
*   **L-2:** Online payment gateway integration (Momo, VNPay) is not included in this stage.
*   **E-1:** CRM features (Loyalty Management) are excluded from Release 1.0.

---

## 3. Business Context

### 3.1. Stakeholder Profiles

| Stakeholder | Value/Benefit | Interest |
| :--- | :--- | :--- |
| **Shop Owner** | Full operational control, reduced loss. | Revenue reports, System security. |
| **Administrator** | Centralized management tool, easy system configuration. | User Management, Setting Management, Data Integrity. |
| **Sales Staff** | (Future) Streamlined sales process. | Ease of use, Stability. |

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

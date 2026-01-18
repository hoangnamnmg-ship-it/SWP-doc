# Vision and Scope Document
**Project:** LocalStore POS  
**Version:** 1.0 (Draft)  
**Status:** In Progress  

---

## 1. Business Requirements

### 1.1. Background
Hiện tại, nhiều cửa hàng bán lẻ quy mô nhỏ (Local Stores) vẫn đang vận hành dựa trên các quy trình thủ công hoặc sử dụng các công cụ quản lý rời rạc, không đồng bộ. Việc quản lý nhân viên, theo dõi ca làm việc, và cập nhật trạng thái hệ thống thường xuyên gặp sai sót, dẫn đến thất thoát doanh thu và khó khăn trong việc mở rộng quy mô. Dự án **LocalStore POS** được khởi xướng nhằm cung cấp một giải pháp quản lý bán hàng tập trung, hiện đại hóa quy trình vận hành cho các cửa hàng này.

### 1.2. Business Opportunity
Các chủ cửa hàng cần một hệ thống đáng tin cậy để quản lý không chỉ giao dịch bán hàng mà còn cả việc quản trị hệ thống nền tảng (Master Data) và phân quyền nhân viên chặt chẽ. Cơ hội kinh doanh nằm ở việc cung cấp một nền tảng POS tinh gọn, dễ sử dụng nhưng có khả năng kiểm soát mạnh mẽ về mặt quản trị (Admin features) mà các giải pháp miễn phí trên thị trường thường thiếu hụt. Hệ thống này sẽ giải quyết bài toán về:
*   Kiểm soát chặt chẽ quyền truy cập của nhân viên.
*   Quản lý linh hoạt các tham số hệ thống (Settings/Master Data) mà không cần can thiệp code.
*   Tạo nền tảng cho việc mở rộng chuỗi cửa hàng trong tương lai.

### 1.3. Business Objectives
*   **BO-1:** Giảm 50% thời gian dành cho việc quản trị người dùng và phân quyền nhân viên trong tháng đầu tiên triển khai.
*   **BO-2:** Đảm bảo 100% các thay đổi về cấu hình hệ thống (Setting/Status) được thực hiện thông qua giao diện Admin, loại bỏ hoàn toàn việc chỉnh sửa trực tiếp vào cơ sở dữ liệu.
*   **BO-3:** Cung cấp cơ chế xác thực bảo mật (Password/OTP) để giảm thiểu rủi ro truy cập trái phép xuống dưới 1%.

### 1.4. Success Metrics
*   **SM-1:** Hệ thống vận hành ổn định với > 500 records dữ liệu mẫu (Packages/Settings) mà không có lỗi về ràng buộc dữ liệu (Data Integrity).
*   **SM-2:** 100% Administrator có thể tự thực hiện thao tác "Add New Master Data" mà không cần hướng dẫn sau 1 buổi training.
*   **SM-3:** Thời gian phản hồi của các chức năng quản lý danh sách (User List, Setting List) dưới 2 giây.

### 1.5. Vision Statement
Dành cho các chủ cửa hàng bán lẻ và quản lý cửa hàng (Shop Managers), những người cần sự kiểm soát chặt chẽ và linh hoạt đối với hệ thống vận hành, **LocalStore POS** là một giải pháp quản lý bán hàng toàn diện. Khác với các hệ thống POS truyền thống cứng nhắc, **LocalStore POS** tập trung xây dựng một nền tảng quản trị vững chắc (Strong Admin Foundation), cho phép tùy biến trạng thái hoạt động và phân quyền chi tiết, giúp doanh nghiệp vận hành trơn tru và bảo mật.

### 1.6. Business Risks
*   **RI-1:** Người dùng cuối (nhân viên bán hàng) có thể gặp khó khăn nếu giao diện quản trị quá phức tạp hoặc mang tính kỹ thuật cao.
*   **RI-2:** Việc tích hợp với các thiết bị phần cứng POS đặc thù (máy in, két tiền) có thể phát sinh lỗi driver chưa lường trước.
*   **RI-3:** Rủi ro về bảo mật dữ liệu nếu cơ chế phân quyền (Authorization) không được kiểm thử kỹ lưỡng.

### 1.7. Business Assumptions and Dependencies
*   **AS-1:** Cửa hàng đã có sẵn hạ tầng mạng internet ổn định.
*   **AS-2:** Người quản trị hệ thống (Admin) có kiến thức cơ bản về quy trình nghiệp vụ của cửa hàng.
*   **DE-1:** Dự án phụ thuộc vào việc hoàn thiện thiết kế Database Schema (như đã mô tả trong tài liệu G6_RDS) trước khi bắt đầu code logic.

---

## 2. Scope and Limitations

### 2.1. Major Features
*   **System Administration (Core):**
    *   Dashboard quản trị tổng quan.
    *   Quản lý danh sách cài đặt (Setting List): Xem, Thêm mới, Cập nhật trạng thái (Active/Inactive), Filter theo loại.
*   **User Management:**
    *   Đăng ký người dùng mới (User Register).
    *   Quản lý danh sách người dùng (User List) với các thông tin chi tiết (Role, Status).
    *   Cơ chế đăng nhập/đăng xuất và xác thực (OTP/Password).
*   **Master Data Management:**
    *   CRUD (Thêm, Xem, Sửa, Xóa mềm) cho các thực thể Master Data (Packages, Categories...).

### 2.2. Scope of Initial and Subsequent Releases

| Feature | Initial Release (v1.0) | Subsequent Releases (v1.x -> v2.0) |
| :--- | :--- | :--- |
| **User Mgmt** | Đăng ký, Đăng nhập, User List (View/Edit Status) | Phân quyền động (Dynamic Role-based Access Control), User Profile Picture |
| **System Setting** | Cấu hình các tham số cơ bản, Status Act/Inact | Cấu hình giao diện (Theme), Đa ngôn ngữ |
| **POS Feature** | (Chưa nằm trong scope lõi của RDS hiện tại) | Màn hình bán hàng (Checkout), In hóa đơn, Quản lý kho hàng |
| **Reporting** | Báo cáo danh sách dạng lưới (Grid View) | Biểu đồ doanh thu (Charts), Xuất Excel/PDF |

> *Lưu ý: Dựa trên tài liệu G6_RDS cung cấp, phiên bản đầu tập trung mạnh vào khung quản trị (Admin/Back-office).*

### 2.3. Limitations and Exclusions
*   **L-1:** Phiên bản đầu tiên chưa hỗ trợ bán hàng Offline (khi mất mạng).
*   **L-2:** Chưa tích hợp thanh toán qua cổng thanh toán điện tử (Momo, VNPay) ở giai đoạn này.
*   **E-1:** Các tính năng CRM (Quản lý khách hàng thân thiết) bị loại trừ khỏi Release 1.0.

---

## 3. Business Context

### 3.1. Stakeholder Profiles

| Stakeholder | Value/Benefit | Interest |
| :--- | :--- | :--- |
| **Shop Owner** | Kiểm soát toàn bộ hoạt động, giảm thất thoát. | Báo cáo doanh thu, Bảo mật hệ thống. |
| **Administrator** | Công cụ quản lý tập trung, dễ dàng cấu hình hệ thống. | Quản lý User, Quản lý Setting, Data Integrity. |
| **Sales Staff** | (Tương lai) Quy trình bán hàng nhanh gọn. | Dễ sử dụng, ổn định. |

### 3.2. Project Priorities
| Dimension | Driver (State Objective) | Constraint (State Limit) | Degree of Freedom (State Allowable Range) |
| :--- | :--- | :--- | :--- |
| **Schedule (Tiến độ)** | | Release 1.0 hoàn thành bộ khung Admin vào [Ngày cụ thể] | |
| **Features (Tính năng)** | | | 70% các tính năng Admin không cốt lõi có thể dời sang v1.1 |
| **Quality (Chất lượng)** | Tính toàn vẹn dữ liệu và Bảo mật phải tuyệt đối (0% lỗi dữ liệu nghiêm trọng) | | |
| **Cost (Chi phí)** | | Tận dụng tối đa phần cứng hiện có, chi phí hạ tầng tối thiểu | |
| **Staff (Nhân sự)** | | Team giữ nguyên quy mô hiện tại, không tuyển thêm | |

### 3.3. Deployment Considerations
*   **Environment:** Web Application (Java-based backend as hinted by 'Bean Interface').
*   **Access:** Truy cập qua trình duyệt web nội bộ hoặc public internet (cần cấu hình HTTPS).
*   **Training:** Cần tài liệu hướng dẫn sử dụng cho Admin về cách thiết lập các thông số ban đầu (Initial Data Setup).

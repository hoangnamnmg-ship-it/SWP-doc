# Tài liệu Vision and Scope
**Dự án:** LocalStore POS  
**Phiên bản:** 1.0 (Dự thảo)  
**Tình trạng:** Đã phê duyệt  

---

## 1. Yêu cầu Nghiệp vụ (Business Requirements)

### 1.1. Bối cảnh (Background)
Hiện nay, nhiều cửa hàng bán lẻ quy mô nhỏ tại địa phương vẫn quản lý hàng hóa và doanh thu bằng sổ sách hoặc file Excel rời rạc. Việc không nắm bắt được số lượng tồn kho chính xác và doanh thu thực tế theo thời gian thực dẫn đến thất thoát hàng hóa, hết hàng không báo trước và khó khăn trong việc đánh giá hiệu quả kinh doanh. Dự án **LocalStore POS** được tái định hướng để tập trung giải quyết triệt để bài toán cốt lõi: **Hàng hóa - Bán hàng - Doanh thu**.

### 1.2. Cơ hội Kinh doanh (Business Opportunity)
Chủ cửa hàng cần một công cụ đơn giản nhưng hiệu quả để kiểm soát dòng tiền và dòng hàng. Họ không cần các tính năng quản lý nhân sự phức tạp (như chấm công, chia ca) mà cần sự chính xác tuyệt đối về số liệu kho và tốc độ bán hàng. Cơ hội nằm ở việc cung cấp một hệ thống POS tập trung tối đa vào trải nghiệm bán hàng nhanh và báo cáo thông minh, giúp chủ cửa hàng trả lời ngay câu hỏi: "Hôm nay bán được bao nhiêu?" và "Kho còn bao nhiêu?".

### 1.3. Mục tiêu Kinh doanh (Business Objectives)
*   **BO-1:** Giảm thiểu tỷ lệ sai lệch hàng tồn kho xuống dưới 1% sau 2 tháng triển khai nhờ quy trình nhập/xuất chặt chẽ.
*   **BO-2:** Tăng tốc độ xử lý đơn hàng tại quầy thanh toán (Checkout), mục tiêu dưới 30 giây/đơn hàng.
*   **BO-3:** Cung cấp báo cáo doanh thu và lợi nhuận theo thời gian thực (Real-time), loại bỏ hoàn toàn việc cộng sổ thủ công cuối ngày.

### 1.4. Chỉ số Thành công (Success Metrics)
*   **SM-1:** 100% giao dịch bán hàng được ghi nhận vào hệ thống và trừ kho tự động ngay lập tức.
*   **SM-2:** Báo cáo doanh thu ngày được xuất ra chính xác chỉ với 1 click chuột.
*   **SM-3:** Thời gian đào tạo nhân viên mới sử dụng tính năng bán hàng dưới 30 phút.

### 1.5. Tuyên bố Tầm nhìn (Vision Statement)
Dành cho các chủ cửa hàng bán lẻ ưu tiên hiệu quả kinh doanh và minh bạch dòng tiền, **LocalStore POS** là hệ thống quản lý tập trung vào Hàng hóa và Doanh thu. Khác với các hệ thống POS "cồng kềnh" tích hợp quá nhiều tính năng quản trị nhân sự không cần thiết, **LocalStore POS** tối ưu hóa quy trình cốt lõi: Nhập hàng nhanh - Bán hàng lẹ - Báo cáo chuẩn.

### 1.6. Rủi ro Kinh doanh (Business Risks)
*   **RI-1:** Người dùng cuối (nhân viên bán hàng) có thể gặp khó khăn nếu giao diện quản trị quá phức tạp hoặc mang tính kỹ thuật cao.
*   **RI-2:** Việc tích hợp với các phần cứng POS cụ thể (máy in, ngăn kéo đựng tiền) có thể gặp lỗi driver không lường trước được.
*   **RI-3:** Rủi ro bảo mật dữ liệu nếu cơ chế phân quyền không được kiểm thử kỹ lưỡng.

### 1.7. Giả định và Phụ thuộc Kinh doanh (Business Assumptions and Dependencies)
*   **AS-1:** Cửa hàng có hạ tầng mạng internet ổn định.
*   **AS-2:** Quản trị viên Hệ thống có kiến thức cơ bản về quy trình kinh doanh của cửa hàng.
*   **DE-1:** Dự án phụ thuộc vào việc hoàn thành thiết kế Sơ đồ Cơ sở dữ liệu (như mô tả trong tài liệu G6_RDS) trước khi bắt đầu viết mã logic.

---

## 2. Phạm vi và Giới hạn (Scope and Limitations)

### 2.1. Các Tính năng Chính (Major Features)
*   **Quản lý Hàng hóa & Kho (Inventory Core):**
    *   Quản lý danh sách Sản phẩm (Tên, Giá, Barcode, Hình ảnh).
    *   Quản lý Nhập kho (Import) và Xuất kho (Export).
    *   Cảnh báo hàng sắp hết (Low stock alert).
*   **Bán hàng & POS (Sales Core):**
    *   Màn hình bán hàng (Checkout) hỗ trợ quét mã vạch.
    *   Tạo hóa đơn, tính tiền, in bill.
    *   Xử lý Trả hàng (Return/Refund).
*   **Báo cáo & Thống kê (Analytics):**
    *   Thống kê doanh thu theo Ngày/Tuần/Tháng.
    *   Báo cáo Top sản phẩm bán chạy.
    *   Báo cáo Lợi nhuận (Doanh thu - Giá vốn).

### 2.2. Phạm vi của Bản phát hành Đầu tiên và Các bản tiếp theo

| Tính năng | Bản phát hành Đầu tiên (v1.0) | Các bản phát hành Tiếp theo (v1.x -> v2.0) |
| :--- | :--- | :--- |
| **Hàng hóa** | CRUD Sản phẩm, Cập nhật tồn kho cơ bản | Quản lý lô/date, Quản lý nhiều Đơn vị tính |
| **Bán hàng** | Tạo hóa đơn bán lẻ, Quét barcode, In bill | Bán hàng Offline, Tích hợp cân điện tử |
| **Báo cáo** | Doanh thu tổng hợp, Lịch sử hóa đơn | Phân tích xu hướng, Dự báo nhập hàng |
| **Quản trị khác** | Login đơn giản (Chủ/Nhân viên) | Phân quyền chi tiết, Nhật ký thao tác (Log) |

> *Lưu ý: Dựa trên tài liệu G6_RDS được cung cấp, phiên bản đầu tiên tập trung mạnh vào khung quản trị (Admin/Back-office).*

### 2.3. Giới hạn và Loại trừ (Limitations and Exclusions)
*   **L-1:** Phiên bản đầu tiên không hỗ trợ bán hàng Ngoại tuyến (Offline - khi mất internet).
*   **L-2:** Tích hợp cổng thanh toán trực tuyến (Momo, VNPay) không được bao gồm trong giai đoạn này.
*   **E-1:** Các tính năng CRM (Quản lý Khách hàng thân thiết) bị loại khỏi Bản phát hành 1.0.

---

## 3. Bối cảnh Kinh doanh (Business Context)

### 3.1. Hồ sơ Các bên Liên quan (Stakeholder Profiles)

| Bên Liên quan | Giá trị/Lợi ích | Thái độ | Mối quan tâm Chính | Ràng buộc |
| :--- | :--- | :--- | :--- | :--- |
| **Chủ Cửa hàng** | Kiểm soát vận hành toàn diện, giảm thất thoát. | Ủng hộ mạnh mẽ | Báo cáo doanh thu, Bảo mật hệ thống, Giảm chi phí. | Ngân sách cho phần cứng mới. |
| **Quản trị viên** | Công cụ quản lý tập trung, cấu hình hệ thống dễ dàng. | Ủng hộ nhưng ngại sự phức tạp | Quản lý Người dùng, Toàn vẹn Dữ liệu, Cấu hình dễ dàng. | Thời gian cần thiết cho thiết lập ban đầu. |
| **Nhân viên Bán hàng** | (Tương lai) Quy trình bán hàng được tinh gọn. | Có thể kháng cự thay đổi | Dễ sử dụng, Ổn định, Tốc độ thanh toán. | Kỹ năng kỹ thuật hạn chế. |

### 3.2. Ưu tiên Dự án (Project Priorities)

| Khía cạnh | Driver (Mục tiêu Tối thượng) | Constraint (Giới hạn Cứng) | Degree of Freedom (Phạm vi Cho phép) |
| :--- | :--- | :--- | :--- |
| **Schedule (Tiến độ)** | | Bản phát hành 1.0 hoàn thành vào [Ngày] (Giai đoạn Nền tảng) | |
| **Features (Tính năng)** | | | 70% các tính năng Admin không cốt lõi có thể hoãn sang v1.1 |
| **Quality (Chất lượng)** | Toàn vẹn Dữ liệu và Bảo mật phải hoàn hảo (0% lỗi dữ liệu nghiêm trọng) | | |
| **Cost (Chi phí)** | | Chi phí hạ tầng tối thiểu (tận dụng phần cứng hiện có) | |
| **Staff (Nhân sự)** | | Quy mô đội ngũ cố định theo năng lực hiện tại | |

### 3.3. Cân nhắc Triển khai (Deployment Considerations)
*   **Môi trường:** Ứng dụng Web (Backend dựa trên Java).
*   **Truy cập:** Truy cập qua trình duyệt web nội bộ hoặc internet công cộng (yêu cầu cấu hình HTTPS).
*   **Đào tạo:** Cần hướng dẫn sử dụng cho Quản trị viên về Thiết lập Dữ liệu Ban đầu.

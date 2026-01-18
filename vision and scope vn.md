# Tài liệu Vision and Scope
**Dự án:** LocalStore POS  
**Phiên bản:** 1.0 (Dự thảo)  
**Tình trạng:** Đã phê duyệt  

---

## 1. Yêu cầu Nghiệp vụ (Business Requirements)

### 1.1. Bối cảnh (Background)
Hiện nay, nhiều cửa hàng bán lẻ quy mô nhỏ tại địa phương hoạt động bằng các quy trình thủ công hoặc sử dụng các công cụ quản lý rời rạc, không đồng bộ. Việc quản lý nhân viên, theo dõi ca làm việc và cập nhật trạng thái hệ thống thường xuyên dễ xảy ra sai sót, dẫn đến thất thoát doanh thu và khó khăn trong việc mở rộng quy mô. Dự án **LocalStore POS** được khởi xướng nhằm cung cấp một giải pháp quản lý bán hàng tập trung, hiện đại hóa quy trình vận hành cho các cửa hàng này.

### 1.2. Cơ hội Kinh doanh (Business Opportunity)
Chủ sở hữu cửa hàng cần một hệ thống đáng tin cậy để không chỉ quản lý giao dịch bán hàng mà còn quản trị nền tảng (Dữ liệu chủ) và phân quyền nhân viên chặt chẽ. Cơ hội kinh doanh nằm ở việc cung cấp một nền tảng POS tinh gọn, dễ sử dụng nhưng sở hữu các tính năng kiểm soát hành chính mạnh mẽ (tính năng Admin), điều mà các giải pháp miễn phí trên thị trường thường thiếu. Hệ thống này sẽ giải quyết:
*   Kiểm soát chặt chẽ quyền truy cập của nhân viên.
*   Quản lý linh hoạt các tham số hệ thống (Cài đặt/Dữ liệu chủ) mà không cần can thiệp vào mã nguồn.
*   Tạo nền tảng cho việc mở rộng chuỗi trong tương lai.

### 1.3. Mục tiêu Kinh doanh (Business Objectives)
*   **BO-1:** Giảm 50% thời gian dành cho việc quản trị người dùng và phân quyền nhân viên trong tháng đầu tiên triển khai.
*   **BO-2:** Đảm bảo 100% các thay đổi cấu hình hệ thống (Cài đặt/Trạng thái) được thực hiện thông qua giao diện Admin, loại bỏ hoàn toàn việc chỉnh sửa trực tiếp cơ sở dữ liệu.
*   **BO-3:** Cung cấp cơ chế xác thực an toàn (Mật khẩu/OTP) để giảm rủi ro truy cập trái phép xuống dưới 1%.

### 1.4. Chỉ số Thành công (Success Metrics)
*   **SM-1:** Hệ thống vận hành ổn định với hơn 500 bản ghi dữ liệu mẫu (Gói/Cài đặt) mà không có lỗi toàn vẹn dữ liệu.
*   **SM-2:** 100% Quản trị viên có thể thực hiện độc lập thao tác "Thêm mới Dữ liệu chủ" mà không cần hướng dẫn sau một buổi đào tạo.
*   **SM-3:** Thời gian phản hồi cho các chức năng quản lý danh sách (Danh sách Người dùng, Danh sách Cài đặt) dưới 2 giây.

### 1.5. Tuyên bố Tầm nhìn (Vision Statement)
Dành cho chủ sở hữu cửa hàng bán lẻ và Quản lý cửa hàng, những người cần sự kiểm soát chặt chẽ và linh hoạt đối với hệ thống vận hành của họ, **LocalStore POS** là một giải pháp quản lý bán hàng toàn diện. Khác với các hệ thống POS truyền thống cứng nhắc, **LocalStore POS** tập trung vào việc xây dựng một nền tảng quản trị vững chắc (Strong Admin Foundation), cho phép tùy chỉnh trạng thái hoạt động và phân quyền chi tiết, giúp doanh nghiệp vận hành trơn tru và an toàn.

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
*   **Quản trị Hệ thống (Cốt lõi):**
    *   Bảng điều khiển Admin.
    *   Quản lý Danh sách Cài đặt: Xem, Thêm mới, Cập nhật Trạng thái (Hoạt động/Không hoạt động), Lọc theo loại.
*   **Quản lý Người dùng:**
    *   Đăng ký Người dùng Mới.
    *   Quản lý Danh sách Người dùng với thông tin chi tiết (Vai trò, Trạng thái).
    *   Cơ chế Đăng nhập/Đăng xuất và Xác thực (OTP/Mật khẩu).
*   **Quản lý Dữ liệu Chủ:**
    *   CRUD (Tạo, Xem, Cập nhật, Xóa mềm) cho các thực thể Dữ liệu Chủ (Gói, Danh mục...).

### 2.2. Phạm vi của Bản phát hành Đầu tiên và Các bản tiếp theo

| Tính năng | Bản phát hành Đầu tiên (v1.0) | Các bản phát hành Tiếp theo (v1.x -> v2.0) |
| :--- | :--- | :--- |
| **Quản lý Người dùng** | Đăng ký, Đăng nhập, Danh sách Người dùng (Xem/Sửa Trạng thái) | Kiểm soát Truy cập dựa trên Vai trò Động, Ảnh đại diện Người dùng |
| **Cài đặt Hệ thống** | Cấu hình tham số cơ bản, Trạng thái Hoạt động/Không hoạt động | Cấu hình Giao diện (Theme), Đa ngôn ngữ |
| **Tính năng POS** | (Không nằm trong phạm vi cốt lõi của RDS hiện tại) | Màn hình Thanh toán, In Hóa đơn, Quản lý Kho |
| **Báo cáo** | Báo cáo Chế độ xem Lưới | Biểu đồ Doanh thu, Xuất Excel/PDF |

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

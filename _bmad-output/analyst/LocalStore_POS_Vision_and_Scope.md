---
title: Tài liệu Vision and Scope
project: LocalStore POS
version: 1.1 (Bản chi tiết)
date: 2026-01-18
author: Nhóm Phân tích Nghiệp vụ
template_source: "Software Requirements, 3rd Edition (Wiegers & Beatty) - Chapter 5"
---

# TÀI LIỆU VISION AND SCOPE
**Dự án:** LocalStore POS (Point of Sale)

---

## 1. YÊU CẦU NGHIỆP VỤ (BUSINESS REQUIREMENTS)

### 1.1. Bối cảnh (Background)
Hiện nay, nhiều cửa hàng bán lẻ quy mô nhỏ tại địa phương vẫn quản lý kho và doanh thu vận hành bằng sổ sách thủ công, giấy nhớ, hoặc các file Excel rời rạc. Cách tiếp cận manh mún này dẫn đến nhiều vấn đề nghiêm trọng:
*   **Mù mờ về Tồn kho (Inventory Blindness):** Chủ cửa hàng không thể biết ngay lập tức số lượng tồn kho chính xác của một mặt hàng cụ thể, dẫn đến việc hết hàng không báo trước hoặc tồn đọng vốn ở các mặt hàng bán chậm.
*   **Thất thoát Doanh thu (Revenue Leakage):** Không có hệ thống ghi nhận chuẩn hóa, các giao dịch bán hàng dễ bị bỏ sót, tính toán sai hoặc gian lận, gây ra sự chênh lệch giữa tiền mặt thực tế và doanh thu ghi sổ.
*   **Thanh toán Chậm chạp (Inefficient Checkout):** Việc tra cứu giá và tính tiền thủ công làm chậm quy trình thanh toán trong giờ cao điểm, giảm sự hài lòng của khách hàng.
*   **Thiếu Thông tin chi tiết (Lack of Insight):** Việc cân đối sổ sách cuối ngày/cuối tháng hoàn toàn thủ công và tốn thời gian; chủ cửa hàng thiếu các thông tin chi tiết dựa trên dữ liệu như "Sản phẩm bán chạy nhất" hoặc "Biên lợi nhuận" để đưa ra quyết định nhập hàng.

Dự án **LocalStore POS** đã được tái định hướng để giải quyết triệt để các vấn đề cốt lõi này bằng cách cung cấp một giải pháp kỹ thuật số tập trung vào **Minh bạch Tồn kho, Bán hàng Nhanh chóng và Báo cáo Doanh thu Chính xác**.

### 1.2. Cơ hội Kinh doanh (Business Opportunity)
Việc triển khai LocalStore POS giải quyết các nhu cầu cấp thiết của chủ cửa hàng về kiểm soát và hiệu quả:
*   **Chuyển đổi số:** Chuyển từ "giấy bút" sang cơ sở dữ liệu số đảm bảo tính bền vững và chính xác của dữ liệu.
*   **Tốc độ Vận hành:** Tự động hóa quy trình thanh toán với quét mã vạch và tự động tính toán giúp giảm đáng kể thời gian chờ đợi của khách hàng.
*   **Ngăn chặn Thất thoát:** Theo dõi tồn kho chặt chẽ (Đầu vào vs Đầu ra) giảm thiểu mất mát hàng hóa do trộm cắp hoặc quản lý yếu kém.
*   **Ra quyết định Thông minh:** Bảng điều khiển thời gian thực cung cấp cái nhìn tức thì về sức khỏe tài chính, cho phép chủ cửa hàng nhập đúng hàng vào đúng thời điểm.

### 1.3. Mục tiêu Kinh doanh (Business Objectives)
Hệ thống nhằm đạt được các mục tiêu hữu hình sau trong vòng 3 tháng triển khai:
*   **BO-1 (Độ chính xác Kho):** Giảm tỷ lệ sai lệch tồn kho (Hệ thống vs Thực tế) xuống dưới **1%** thông qua quy trình nhập/xuất nghiêm ngặt và kiểm tra mã vạch.
*   **BO-2 (Hiệu quả Thanh toán):** Tăng tốc độ xử lý đơn hàng trung bình tại quầy xuống dưới **30 giây mỗi giao dịch** (từ lúc quét đến lúc in hóa đơn).
*   **BO-3 (Minh bạch Doanh thu):** Cung cấp báo cáo Lợi nhuận & Lỗ **Thời gian thực**, loại bỏ hoàn toàn 1-2 giờ thường tiêu tốn cho việc cộng sổ thủ công cuối ngày.
*   **BO-4 (Vận hành liên tục):** Đảm bảo quy trình bán hàng không bị gián đoạn ngay cả trong thời gian cao điểm thông qua kiến trúc nhẹ và ổn định.

### 1.4. Chỉ số Thành công (Success Metrics)
Sự thành công của dự án sẽ được đo lường bằng các chỉ số định lượng sau:
*   **SM-1:** 100% chi tiết sản phẩm có giá trị (Giá bán, Giá vốn, Tồn kho) được số hóa và truy cập được qua hệ thống.
*   **SM-2:** 95% nhân viên bán hàng có thể vận hành độc lập màn hình bán hàng POS mà không cần giám sát sau khi nhận được 30 phút đào tạo.
*   **SM-3:** Các báo cáo tài chính chính (Doanh thu Ngày) được tạo ra ngay lập tức (đổ trễ < 2 giây) khi có yêu cầu.
*   **SM-4:** 100% giao dịch bán hàng được ghi nhận với dấu vết kiểm toán (Ai bán, Khi nào, Mặt hàng gì), cho phép truy xuất nguồn gốc đầy đủ.

### 1.5. Tuyên bố Tầm nhìn (Vision Statement)
> *"Dành cho các chủ cửa hàng bán lẻ và Quản lý cửa hàng ưu tiên hiệu quả kinh doanh và sự minh bạch dòng tiền, **LocalStore POS** là một hệ thống quản lý chuyên biệt tập trung nghiêm ngặt vào **Hàng hóa và Doanh thu**. Khác với các hệ thống POS 'cồng kềnh' tích hợp quá nhiều tính năng nhân sự không cần thiết hay kế toán phức tạp, LocalStore POS tối ưu hóa vòng lặp vận hành cốt lõi: **Nhập hàng Nhanh -> Bán hàng Lẹ -> Báo cáo Chuẩn**. Sản phẩm của chúng tôi đảm bảo rằng chủ cửa hàng luôn biết chính xác họ có gì trong kho và họ đã kiếm được bao nhiêu lợi nhuận ngày hôm nay, một cách dễ dàng."*

### 1.6. Rủi ro Kinh doanh (Business Risks)
*   **RI-1 (Kháng cự Thay đổi):** Nhân viên lớn tuổi có thể gặp khó khăn khi sử dụng máy tính/máy quét mã vạch so với máy tính bỏ túi thủ công.
    *   *Giảm thiểu:* Thiết kế Giao diện Người dùng (UI) màn hình Thanh toán cực kỳ đơn giản, tương phản cao, giảm thiểu số lần nhấp chuột. Cung cấp đào tạo "Cầm tay chỉ việc".
*   **RI-2 (Tương thích Phần cứng):** Đa dạng các loại máy quét/máy in giá rẻ trên thị trường có thể gây xung đột driver.
    *   *Giảm thiểu:* Chuẩn hóa các giao thức phần cứng tuân thủ HID "Cắm là chạy". Công bố danh sách "Phần cứng Khuyên dùng".
*   **RI-3 (Mất Dữ liệu):** Hỏng hóc phần cứng cục bộ (hỏng PC) có thể dẫn đến mất dữ liệu bán hàng nếu không được sao lưu.
    *   *Giảm thiểu:* Triển khai khả năng đồng bộ đám mây hoặc tự động sao lưu cục bộ hàng ngày sang ổ cứng ngoài/phân vùng phụ.

### 1.7. Giả định và Phụ thuộc Kinh doanh
*   **AS-1:** Cửa hàng được trang bị kết nối internet ổn định (để truy cập nền tảng web) và phần cứng máy tính cơ bản (PC/Laptop).
*   **AS-2:** Chủ cửa hàng sẵn sàng thực hiện "Kiểm kê Kho Vật lý" ban đầu để nhập số lượng khởi điểm chính xác vào cơ sở dữ liệu.
*   **DE-1:** Dự án phụ thuộc vào thiết kế lược đồ cơ sở dữ liệu (G6_RDS) đã được chốt để đảm bảo các ràng buộc toàn vẹn dữ liệu được đáp ứng ngay từ Ngày đầu.

---

## 2. PHẠM VI VÀ GIỚI HẠN (SCOPE AND LIMITATIONS)

### 2.1. Các Tính năng Chính (Major Features)
Hệ thống được tổ chức theo chức năng thành 4 nhóm tính năng chính:

*   **FE-1: Quản lý Kho & Sản phẩm (Nền tảng)**
    *   **CRUD Sản phẩm:** Tạo và duy trì hồ sơ sản phẩm chi tiết (Tên, Mã vạch, Giá bán, Giá vốn, Đơn vị, Danh mục, Hình ảnh).
    *   **Quản lý Kho:**
        *   **Nhập hàng:** Ghi nhận hàng nhập từ nhà cung cấp (cập nhật số lượng và giá vốn).
        *   **Điều chỉnh Kho:** Sửa lỗi thủ công cho hàng hóa hư hỏng/mất mát.
    *   **Cảnh báo Hàng sắp hết:** Chỉ báo trực quan khi số lượng mặt hàng giảm xuống dưới ngưỡng xác định.

*   **FE-2: Vận hành Bán hàng & POS (Cốt lõi)**
    *   **Màn hình Thanh toán:** Giao diện tối ưu cho tốc độ. Hỗ trợ:
        *   Quét mã vạch (qua máy quét USB).
        *   Tìm kiếm nhanh sản phẩm theo tên/mã.
        *   Điều chỉnh số lượng.
    *   **Xử lý Giao dịch:** Tự động tính tổng tiền, tiền thừa trả khách và chốt đơn hàng.
    *   **In Hóa đơn:** Tạo hóa đơn nhiệt tiêu chuẩn (58mm/80mm) cho khách hàng.
    *   **Trả hàng/Hoàn tiền:** Xử lý trả hàng với mã lý do và tự động cập nhật lại tồn kho.

*   **FE-3: Báo cáo & Phân tích (Thông tin chi tiết)**
    *   **Báo cáo Doanh thu:** Xem tổng hợp doanh số theo Ngày, Tuần, Tháng hoặc Khoảng thời gian tùy chỉnh.
    *   **Phân tích Bán chạy:** Xác định Top 10 sản phẩm hiệu quả nhất theo số lượng hoặc doanh thu.
    *   **Ước tính Lợi nhuận:** Tính toán lợi nhuận ước tính (Doanh thu - Giá vốn hàng bán) để đánh giá sức khỏe kinh doanh.

*   **FE-4: Quản trị Hệ thống (Kiểm soát)**
    *   **Quản lý Người dùng:** Tạo tài khoản cho Chủ (Admin) và Nhân viên (Thu ngân).
    *   **Xác thực Cơ bản:** Cơ chế Đăng nhập/Đăng xuất bảo mật.
    *   **Cài đặt:** Cấu hình thông tin cửa hàng (Tên, Địa chỉ, SĐT) để hiển thị trên hóa đơn.

### 2.2. Phạm vi của Bản phát hành Đầu tiên và Các bản tiếp theo
Lộ trình ưu tiên sự ổn định của các giao dịch cốt lõi trước các tính năng nâng cao.

| Nhóm Tính năng | Release 1.0 (Nền tảng - MVP) | Release 2.0 (Tăng trưởng - Tương lai) |
| :--- | :--- | :--- |
| **Kho hàng** | **Cơ bản:** Đơn vị tính đơn lẻ, theo dõi tồn kho chuẩn. | **Nâng cao:** Quy đổi đa đơn vị (VD: Thùng -> Cái), Theo dõi Lô/Hạn sử dụng. |
| **Bán hàng POS** | **Chế độ Online:** Thanh toán trên nền web, hỗ trợ máy quét USB chuẩn. | **Chế độ Offline:** Hỗ trợ LocalStorage khi mất mạng. Tích hợp Cân điện tử. |
| **Báo cáo** | **Bảng Tĩnh:** Chế độ xem lưới, tổng cộng cơ bản. | **Trực quan:** Biểu đồ tương tác, Đồ thị và Xuất ra Excel/PDF. |
| **Khách hàng** | **Chung:** Chỉ khách vãng lai (Walk-in). | **Thân thiết:** Tích điểm thành viên, Lịch sử mua hàng của khách. |
| **Khuyến mãi** | **Thủ công:** Thu ngân nhập số tiền giảm giá bằng tay. | **Tự động:** Quy tắc hệ thống áp dụng (Mua 1 Tặng 1, Giờ Vàng). |

### 2.3. Giới hạn và Loại trừ
*   **EX-1 (Không có Kế toán chuyên sâu):** Hệ thống ghi nhận doanh thu bán hàng nhưng **KHÔNG** phải là một hệ thống kế toán đầy đủ. Nó không xử lý kê khai thuế, bảng cân đối kế toán hay chi phí chi tiết (tiền thuê nhà, điện nước).
*   **EX-2 (Không có Nhân sự/Lương):** Theo yêu cầu, các tính năng liên quan đến Xếp ca làm việc, Chấm công và Tính lương bị **LOẠI TRỪ** hoàn toàn.
*   **EX-3 (Không đồng bộ Đa chi nhánh):** Release 1.0 được thiết kế cho kiến trúc **Một Cửa hàng**. Đồng bộ tồn kho đa chi nhánh nằm ngoài phạm vi.
*   **EX-4 (Không Thương mại điện tử):** Đây là POS bán tại quầy. Nó không tích hợp với các kênh bán hàng trực tuyến (Shopee, Website).

---

## 3. BỐI CẢNH KINH DOANH (BUSINESS CONTEXT)

### 3.1. Hồ sơ Các bên Liên quan

| Bên Liên quan | Giá trị/Lợi ích | Thái độ | Mối quan tâm Chính | Ràng buộc |
| :--- | :--- | :--- | :--- | :--- |
| **Chủ Cửa hàng** | Kiểm soát hoàn toàn tồn kho và tiền mặt, loại bỏ thất thoát. | Ủng hộ mạnh mẽ (Động lực chính). | Dữ liệu Lãi/Lỗ chính xác, Chống trộm cắp, Dễ dàng thiết lập. | Ngân sách hạn chế cho phần cứng, ít chấp nhận thời gian chết. |
| **Nhân viên Bán hàng** | Thanh toán nhanh hơn, không lỗi tính nhẩm, kiểm tra kho tự động. | Trái chiều (E ngại bị giám sát). | Dễ sử dụng (ít thao tác), Ổn định (không treo máy giờ cao điểm), Bàn giao ca rõ ràng. | Kỹ năng kỹ thuật hạn chế, tỷ lệ thay thế nhân sự cao. |
| **Admin** | Cấu hình tập trung, quản lý người dùng dễ dàng. | Ủng hộ. | Toàn vẹn dữ liệu, Bảo mật, Nhật ký kiểm toán. | Thời gian có hạn cho việc nhập liệu ban đầu. |

### 3.2. Ưu tiên Dự án

| Khía cạnh | Ràng buộc (Phải tuân thủ) | Động lực (Yếu tố thành công chính) | Độ linh hoạt (Có thể điều chỉnh) |
| :--- | :--- | :--- | :--- |
| **Chất lượng** | **Toàn vẹn Dữ liệu:** Không khoan nhượng với lỗi tính toán tồn kho/doanh thu. | | |
| **Tiến độ** | | **Release 1.0** phải sẵn sàng cho UAT vào [Ngày]. | |
| **Ngân sách** | Chi phí hạ tầng tối thiểu (tận dụng PC hiện có). | | |
| **Tính năng** | | **Tốc độ Thanh toán** & **Độ chính xác Kho**. | Các hiệu ứng UI "đẹp mắt" hoặc bộ lọc nâng cao có thể bị cắt giảm. |
| **Khả năng sử dụng** | | Giao diện không cần đào tạo cho thu ngân. | |

### 3.3. Cân nhắc Triển khai
*   **Thiết lập Phần cứng:**
    *   Hệ thống chạy trên PC/Laptop hoặc Máy tính bảng Windows tiêu chuẩn qua Trình duyệt.
    *   Thiết bị ngoại vi: Máy quét mã vạch USB (Chế độ HID) và Máy in hóa đơn nhiệt (USB/LAN).
*   **Chuyển đổi Dữ liệu (Quan trọng):**
    *   Hệ thống phải cung cấp tính năng **"Nhập từ Excel"** cho Sản phẩm. Việc nhập thủ công hơn 1000 mặt hàng là rào cản cho việc áp dụng.
    *   Chiến lược "Kiểm kê Kho" ban đầu phải được lên kế hoạch với chủ cửa hàng trước khi Go-Live.
*   **Kế hoạch Đào tạo:**
    *   **Đào tạo Chủ cửa hàng:** Tập trung vào Tạo sản phẩm, Nhập hàng và Đọc báo cáo.
    *   **Đào tạo Nhân viên:** Tập trung nghiêm ngặt vào quy trình Thanh toán, Tìm kiếm và Xử lý Hoàn tiền.

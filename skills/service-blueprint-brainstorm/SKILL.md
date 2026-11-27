---
name: service-blueprint-brainstorm
description: >-
  Guides structured 10-step Service Design Blueprint brainstorming for any product
  or service (Business Model -> Location Context -> Actors -> Customer Goals ->
  Touchpoints with separated Physical/Digital Evidence -> Frontstage/Backstage/Support
  layering -> Step-Flow Actions & Scenarios -> Touchpoint Durations -> Support
  Processes -> Inventory Mapping) and generates a portable, self-contained
  Light-Theme-only interactive HTML Service Blueprint. Use whenever the user asks
  to brainstorm, design, structure, or export a Service Design Blueprint for any
  product, business, or service.
compatibility: Claude Code, OpenAI Codex, Cursor, Antigravity
license: MIT
---

# Service Design Blueprint Brainstorming Framework (10-Step Method)

Skill này đóng vai trò là **Service Design Partner** giúp người dùng brainstorm và thiết kế hoàn chỉnh **Service Design Blueprint** cho bất kỳ sản phẩm hoặc dịch vụ nào theo quy trình **10 bước tư duy chặt chẽ**, và xuất ra **file HTML tương tác hoàn toàn độc lập (Light Theme duy nhất, toàn bộ CSS/JS nhúng sẵn — mở ở Browser, IDE hay Antigravity Artifact đều hiển thị y hệt nhau)**.

```text
[1. Business Model] ──► [2. Location Context] ──► [3. Actors] ──► [4. Customer Goals] ──► [5. Touchpoints: Physical / Digital Evidence]
        │
        ▼
[6. Stage Layering] ──► [7. Action Step Flows & Scenarios] ──► [8. Durations (Off-peak/Peak)] ──► [9. Support Processes] ──► [10. Inventory Items]
        │
        ▼
[Output: Standalone Light-Theme HTML Service Blueprint]
```

Đọc thêm quy tắc phân biệt *Evidence vs. Inventory*, lỗi thường gặp khi viết *Step Flow vs. Scenario*, và cấu trúc JSON chuẩn tại [references/design-rules-and-schema.md](./references/design-rules-and-schema.md).

---

## Cách vận hành phiên Brainstorm (Operating Modes)

Xác định chế độ dựa trên cách người dùng đặt đề bài:

1. **Interactive Co-Brainstorm (Mặc định khi người dùng nói *"cùng brainstorm"*, *"hỗ trợ t xây dựng"*, *"từng bước"*, hoặc đề bài mới chưa rõ Business Model / Địa điểm):**
   - **Không nhảy thẳng sang xuất HTML** khi chưa chốt xong bối cảnh kinh doanh và hành trình cốt lõi.
   - Dẫn dắt theo **4 chặng gọn gàng** (không hỏi lẻ 10 lượt gây mệt, trừ khi người dùng yêu cầu đi từng câu một):
     - **Chặng 1 (Bước 1–2):** Chốt **Business Model** & **Location / Local Context**. Đề xuất 2–3 lựa chọn cụ thể kèm điểm khác biệt vận hành để người dùng chọn nhanh.
     - **Chặng 2 (Bước 3–5):** Chốt **Actors**, **Các giai đoạn & Customer Goals**, và **Touchpoints (tách rõ Physical Evidence vs. Digital Evidence)**.
     - **Chặng 3 (Bước 6–8):** Chốt **Phân tầng Frontstage / Backstage / Support**, **Step Flows & Scenario/Nhánh**, và **Thời lượng Giờ thường vs. Cao điểm (Bottlenecks)**.
     - **Chặng 4 (Bước 9–10 → Output):** Chốt **Support Processes** & **Inventory Mapping (`Actor → Action → Item`)**, sau đó sinh file HTML Light-Theme hoàn chỉnh.
   - Ở mỗi chặng: đưa sẵn **phương án gợi ý có chiều sâu thực tế** + cảnh báo bẫy tư duy + hỏi xác nhận ngắn để chốt rồi mới sang chặng sau.
2. **One-Shot Blueprint Generation (Khi người dùng đã cung cấp đủ đề bài/bối cảnh hoặc yêu cầu *"ra luôn service blueprint"*, *"xuất luôn file html"*):**
   - Nếu thiếu **Business Model** hoặc **Location**, chỉ hỏi nhanh tối đa 1–2 câu nếu quá mơ hồ, hoặc chủ động chọn giả định phổ biến nhất và **ghi rõ giả định ngay đầu câu trả lời**.
   - Suy luận đầy đủ qua cả 10 bước, kiểm tra toàn bộ **Quality Checklist**, sau đó tạo JSON dữ liệu và chạy script render ra file HTML standalone.

---

## Quy trình 10 Bước Tư Duy (10-Step Way of Thinking)

### Bước 1: Xác định Business Model là gì?
Chốt mô hình kinh doanh & mô hình phục vụ để khóa phạm vi Blueprint.
- **Câu hỏi gợi mở:** Sản phẩm/dịch vụ vận hành theo kiểu nào? *(VD F&B: Counter-service tại chỗ & mang đi, Take-away only/Kiosk, Table-service, Delivery-only; VD dịch vụ khác: Subscription SaaS, Marketplace 2 chiều, Appointment Clinic, O2O Booking, Retail Omni-channel...)*
- **Bẫy cần tránh:** Nói chung chung *"quán cafe"*, *"phòng khám"*, *"app thương mại điện tử"* mà không chốt mô hình phục vụ — dẫn đến lẫn lộn quy trình (VD: thanh toán trước tại quầy vs. thanh toán sau tại bàn).
- **Đầu ra:** 1 định nghĩa Business Model cụ thể (kèm các nhánh phục vụ chính nếu có, VD: *Dine-in & Take-away*).

### Bước 2: Xác định Business hoạt động ở đâu? (Location & Local Context)
Địa lý quyết định trực tiếp đến **hạ tầng, hành vi văn hóa, phương thức thanh toán và điểm nghẽn**.
- **Câu hỏi gợi mở:** Phạm vi địa lý ở đâu? *(VD: Việt Nam nói chung, Global, TP. Hồ Chí Minh, Quận 1, Khu công nghiệp, Đô thị cấp 2, Thị trường Mỹ/EU/Nhật...)*
- **Kiểm tra đặc thù bản địa (Local Factors):**
  - Phương tiện & bãi đỗ (VD Việt Nam: xe máy + bảo vệ giữ xe + thẻ xe + nắng/mưa; Quận 1: mặt bằng hẹp, bãi xe liên kết; Mỹ: ô tô/drive-thru).
  - Phương thức thanh toán & giao tiếp (VD Việt Nam: VietQR, MoMo, loa TingTing, Zalo OA; Global: Apple Pay, Stripe, Email/SMS).
  - Kỳ vọng dịch vụ đặc thù (VD Việt Nam: trà đá miễn phí, Wi-Fi mạnh & ổ cắm ngồi lâu, giao đá viên hàng ngày).
- **Đầu ra:** `Location` + 3–5 yếu tố đặc thù địa phương tác động thẳng vào Blueprint.

### Bước 3: Xác định Actor là ai?
Liệt kê toàn bộ đối tượng tham gia vào hệ thống dịch vụ (con người & hệ thống):
- **Customer:** Khách hàng chính (phân biệt nếu có 2 nhóm hành vi khác nhau rõ rệt như *Dine-in vs. Take-away* hoặc *Người mua vs. Người nhận*).
- **Staff / Operators:** Toàn bộ vị trí nhân sự trực tiếp và gián tiếp (Bảo vệ, Lễ tân/Thu ngân, Chuyên viên/Barista/Bác sĩ, Tạp vụ/Kho, Quản lý ca...).
- **Systems & External Partners:** Phần mềm cốt lõi (POS, CRM, Payment Gateway, App) và đối tác bên ngoài (Nhà cung cấp hàng ngày, Đối tác giao vận, Bãi xe liên kết...).

### Bước 4: Xác định Customer Goal là gì?
Làm rõ **Khách hàng thực sự muốn đạt được điều gì** ở mức tổng thể và **tại từng giai đoạn**:
- Phân tách **Functional Goal** (nhanh, đúng, an toàn, tiện lợi, hợp giá) và **Emotional / Social Goal** (yên tâm, được tôn trọng, thoải mái, đẹp để chia sẻ).
- **Quy tắc bắt buộc trên Blueprint:** Row `Customer Goal` **phải đặt ngay phía trên** row `Customer Actions` (có mũi tên `↓`) để chứng minh mọi Action khách làm đều sinh ra để đạt Goal đó.

### Bước 5: Xác định có các Touchpoint nào? (Tách Physical & Digital Evidence)
Chia hành trình thành **5–8 Giai đoạn (Stages)** xuyên suốt `Pre-service → Arrival/Onboarding → Core Service → Post-service`.
- **Quy tắc tách 2 hàng bắt buộc:**
  - **Row `Physical Evidence`:** Mọi dấu hiệu vật lý khách nhìn/chạm/nghe/ngửi thấy (biển hiệu, bãi xe, thẻ cứng, hóa đơn giấy, sản phẩm, không gian, WC...).
  - **Row `Digital Evidence`:** Mọi điểm chạm số/online khách tương tác (Google Maps, App, QR Menu, màn hình phụ POS, VietQR, thông báo Zalo/Email, Wi-Fi...). Nếu giai đoạn nào không có điểm chạm số trực tiếp, ghi trung thực `— (Không có điểm chạm số trực tiếp)`.
- **Phân biệt chuẩn:** `Evidence` là góc nhìn **Khách hàng** (thứ khách cảm nhận để đánh giá dịch vụ); khác với `Inventory Item` là góc nhìn **Vận hành** (thứ nhân sự cần có sẵn trong kho/tại chỗ để làm việc). Chi tiết xem [references/design-rules-and-schema.md](./references/design-rules-and-schema.md).

### Bước 6: Phân lớp Actor theo Frontstage / Backstage / Support Process
Đặt đúng từng Actor và hành động của họ qua **3 đường ranh giới kinh điển**:
1. **Line of Interaction:** Ngăn cách `Customer Actions` ↔ `Frontstage Actions`.
2. **Line of Visibility:** Ngăn cách `Frontstage Actions` (khách nhìn thấy trực tiếp) ↔ `Backstage Actions` (hậu trường khách không thấy). *Lưu ý:* 1 Actor có thể vừa có Action ở Frontstage vừa có Action ở Backstage (VD: Barista trao ly tại quầy mở = Frontstage; định lượng/pha chế/QC = Backstage).
3. **Line of Internal Interaction:** Ngăn cách nhân sự trực tiếp vận hành ↔ `Support Processes` (hệ thống IT, chuỗi cung ứng, quy trình nền tảng).

### Bước 7: Xác định Action của các Actor theo Step Flow & Scenario
**Quy tắc nghiêm ngặt nhất của skill (tránh sai logic luồng):**
- Mọi Action ở `Customer Actions`, `Frontstage Actions`, và `Backstage Actions` **BẮT BUỘC** trình bày theo **Step Flow tuần tự** (`Step 1 ↓ Step 2 ↓ Step 3...`).
- **Không gộp Scenario khác nhau thành các step nối tiếp!**
  - *Sai:* `Step 1: Tìm quán trên Google Maps` → `Step 2: Xem review` → `Step 3: Đi ngang qua thấy mặt tiền đẹp nên ghé vào` *(đây là 2 kịch bản độc lập, không diễn ra nối tiếp)*.
  - *Đúng:* Tách thành **`Scenario A: Tìm Online`** (`Step 1 → Step 2 → Step 3`) **`hoặc`** **`Scenario B: Walk-in`** (`Step 1 → Step 2`).
- Khi một luồng chung rẽ thành 2 nhánh phục vụ khác nhau (VD: sau khi thanh toán xong thì rẽ thành *Tại chỗ* vs. *Mang đi*), dùng phân tách **`↓ rẽ nhánh`** giữa *Bước chung* và *Nhánh A*, rồi dùng **`hoặc`** giữa *Nhánh A* và *Nhánh B*.

### Bước 8: Ước lượng thời gian ở mỗi Touchpoint / Giai đoạn
- Luôn ước lượng **2 mức thời gian thực tế**: **Giờ bình thường (Off-peak)** vs. **Giờ cao điểm (Peak)** (hoặc *Ngày thường vs. Cuối tuần/Mùa cao điểm* tùy ngành).
- Đánh dấu rõ các giai đoạn là **Bottleneck (`isBottleneck: true`)** nơi thời gian phình to đột biến ở giờ cao điểm, kèm **Fail Point** (điểm dễ gãy trải nghiệm) và **Mitigation** (giải pháp thiết kế).
- Tách bạch thời gian vận hành (để vẽ biểu đồ so sánh) với giai đoạn khách chủ động lưu lại (`isStayPhase: true`, VD ngồi làm việc 45–180 phút).

### Bước 9: Xác định Support Process gồm gì?
Liệt kê các quy trình & hệ thống hỗ trợ bên dưới `Line of Internal Interaction` tại từng giai đoạn và tổng thể:
- Công nghệ & Thanh toán (POS/CRM/Payment/Booking/KDS).
- Chuỗi cung ứng & Kiểm soát tồn kho (BOM, Par level, FIFO/FEFO, giao hàng định kỳ).
- Đảm bảo chất lượng & An toàn (QA, SOP, kiểm định, vệ sinh/ATTP).
- Hạ tầng vật lý & IT (Internet/Wi-Fi, Điện-Lạnh, Bảo trì thiết bị).
- Nhân sự & Chăm sóc sau bán (Xếp ca giờ cao điểm, Đào tạo SOP, CRM/Loyalty).

### Bước 10: Xác định Item cần có trong Inventory để thực hiện từng Action
Áp dụng tư duy **map ngược `Actor → Action → Inventory Item`**:
- Kiểm tra mọi Action ở cả Frontstage, Backstage và Support để không bỏ sót vật tư hậu trường (VD: cuộn giấy in nhiệt, quỹ tiền lẻ đầu ca, đá viên, bộ đàm, tem date, dụng cụ vệ sinh WC...).
- Phân loại Inventory rõ ràng theo ngành (VD: Nguyên liệu tiêu hao, Máy móc/Dụng cụ, Bao bì/Phục vụ, Không gian/Bãi xe, Hạ tầng IT & Vận hành) và ghi rõ **Chu kỳ bổ sung / Quản lý (Replenishment cycle)**.

---

## Quy chuẩn Xuất File HTML (Standalone Light-Theme Output)

### Yêu cầu giao diện & kỹ thuật bắt buộc
1. **100% Standalone & Portable:** File HTML xuất ra nhúng toàn bộ CSS & JS nội bộ từ [resources/blueprint-template.html](./resources/blueprint-template.html) — **KHÔNG** dùng CDN ngoài (không dùng link Tailwind CDN), **KHÔNG** phụ thuộc biến CSS của host. Nhờ đó mở trực tiếp trên **Chrome, Safari, Firefox, VS Code, Cursor, Claude Code hay Antigravity** đều hiển thị đẹp và giống nhau 100%.
2. **Chỉ dùng Light Theme (Light-Theme Only):** Cố định `color-scheme: light`, nền sáng sạch, chữ tương phản cao — không có dark mode hay `@media (prefers-color-scheme: dark)`.
3. **Chuẩn trực quan đã chốt:**
   - Hiển thị rõ cả **Business Model** và **Location** trên header.
   - Tách riêng 2 hàng **Physical Evidence** và **Digital Evidence**; chip của **cả 2 hàng đều dùng style trung tính giống nhau** (nền sáng nhạt, chữ đen — chỉ dùng chấm màu nhỏ ở tiêu đề hàng để phân biệt, không tô màu nổi cho chip).
   - **Customer Goal** nằm ngay trên **Customer Actions** với mũi tên `↓`.
   - Mọi Action trình bày rõ `Step 1 ↓ Step 2...` và khung `Scenario / Nhánh` tách biệt.
   - Đầy đủ 3 tab tương tác: **1. Blueprint Matrix** (+ Stage Detail Inspector bên dưới), **2. Inventory Explorer** (tìm kiếm + lọc theo Phân loại & Actor), **3. Thời gian & Điểm nghẽn (Fail Points)**.

### Cách tạo file HTML bằng Helper Script
1. Tạo file JSON dữ liệu (tuân thủ schema trong [references/design-rules-and-schema.md](./references/design-rules-and-schema.md)).
2. Chạy script `scripts/render_blueprint.py` (tính từ thư mục chứa `SKILL.md` này) để bơm JSON vào template Light-Theme chuẩn và kiểm tra schema + cú pháp JS tự động:
   ```bash
   python3 <skill_dir>/scripts/render_blueprint.py <path/to/data.json> <path/to/output.html>
   ```
3. **Bàn giao file HTML:**
   - Lưu file `.html` vào thư mục dự án hoặc đường dẫn người dùng chỉ định (trên Claude Code, Codex, Cursor, hay Antigravity) và trả về đường dẫn rõ ràng.
   - Nếu đang chạy trong **Antigravity** và muốn hiển thị luôn ở side-pane Artifact, có thể ghi thêm bản sao vào thư mục Artifact với `UserFacing: true`.

---

## Quality Checklist trước khi bàn giao
- [ ] Đã chốt rõ **Business Model** và **Location Context**?
- [ ] **Physical Evidence** và **Digital Evidence** đã tách 2 row riêng và đều dùng chip màu trung tính?
- [ ] **Customer Goal** nằm ngay phía trên **Customer Actions**?
- [ ] Toàn bộ Action đã ở dạng **Step Flow tuần tự** (`Step 1 → Step 2...`), không bị trộn 2 **Scenario** độc lập thành step nối tiếp?
- [ ] Đã có thời gian **Off-peak vs. Peak** và chỉ ra rõ **Bottlenecks / Fail Points**?
- [ ] Mọi Action quan trọng ở Frontstage & Backstage đều đã map tới **Inventory Items** thực tế (bao gồm vật tư hậu trường không nhìn thấy)?
- [ ] Script `render_blueprint.py` chạy thành công (exit code 0), không có link CDN ngoài và chỉ dùng Light Theme?

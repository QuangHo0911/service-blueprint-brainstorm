# Service Blueprint Design Rules & JSON Schema Reference

Tài liệu tham khảo cho skill `service-blueprint-brainstorm`: bao gồm các quy tắc phân biệt khái niệm cốt lõi và chuẩn JSON đầu vào cho `scripts/render_blueprint.py`.

---

## 1. Quy tắc cốt lõi tránh sai lệch tư duy

### A. Phân biệt `Evidence` vs. `Inventory Item`
| Tiêu chí | Evidence (Physical / Digital) | Inventory Item |
| :--- | :--- | :--- |
| **Góc nhìn** | **Khách hàng** (thứ khách nhìn/chạm/nghe/ngửi thấy để đánh giá chất lượng) | **Vận hành** (nguyên liệu, thiết bị, vật tư Actor cần để thực thi Action) |
| **Vị trí trên Blueprint** | Tầng trên cùng (tách 2 hàng: `Physical Evidence` & `Digital Evidence`) | Phục vụ cả Frontstage, Backstage & Support |
| **Ví dụ chỉ là Evidence** | Mùi hương, nhạc nền, độ mát điều hòa, đánh giá 4.8 sao Google Maps | *(Không kiểm kê như tồn kho)* |
| **Ví dụ chỉ là Inventory** | *(Nằm dưới Line of Visibility — khách không thấy)* | Cuộn giấy in K80, tem decal, quỹ tiền lẻ đầu ca, đá viên dự trữ, bộ đàm, hóa chất vệ sinh |
| **Vùng giao nhau** | Ly mang đi (đẹp, chắc tay?), thẻ rung (sạch, dễ nhận biết?) | Ly mang đi (tồn kho, COGS, Par level?), thẻ rung (số lượng bộ, kiểm đếm thất lạc?) |

### B. Quy tắc viết `Action` theo `Step Flow` & Tách `Scenario`
1. **Luôn viết tuần tự `Step 1 → Step 2 → Step 3...`** cho cả Customer Actions, Frontstage Actions và Backstage Actions.
2. **Phát hiện & tách Scenario độc lập:** Nếu hành động B **không xảy ra nối tiếp sau** hành động A mà là một cách tiếp cận/nhánh phục vụ khác, phải tách thành object riêng trong `customerFlows`:
   - 2 kịch bản khởi đầu độc lập (VD: `Scenario A: Tìm Online` vs. `Scenario B: Walk-in`): đặt `"connectorBefore": "hoặc"` cho Scenario B.
   - 1 luồng chung rẽ thành 2 nhánh (VD: sau khi thanh toán xong thì rẽ thành `Nhánh A: Tại chỗ` vs. `Nhánh B: Mang đi`):
     - Khối 1 (`Bước chung`): `"connectorBefore": null`
     - Khối 2 (`Nhánh A`): `"connectorBefore": "↓ rẽ nhánh"`
     - Khối 3 (`Nhánh B`): `"connectorBefore": "hoặc"`

### C. Quy tắc trực quan Light Theme (Đã chuẩn hóa)
- **Chỉ dùng Light Theme** — tuyệt đối không chèn dark mode media query hay host CSS variables.
- **Physical Evidence & Digital Evidence:** Chip ở cả 2 hàng đều dùng màu trung tính (nền sáng, chữ đen) để tránh lệch trọng số thị giác và tránh trùng màu với badge Actor/Scenario.
- **Customer Goal** nằm trực tiếp phía trên **Customer Actions** kèm mũi tên `↓`.

---

## 2. Cấu trúc JSON đầu vào (`data.json`)

File JSON truyền vào `scripts/render_blueprint.py` phải có cấu trúc sau:

```json
{
  "title": "Service Blueprint — [Tên sản phẩm / dịch vụ]",
  "subtitle": "Mô tả ngắn mô hình, đối tượng phục vụ và phạm vi quy trình.",
  "businessModel": "VD: Counter-Service (Tại chỗ & Mang đi)",
  "location": "VD: Việt Nam (Đô thị lớn / TP.HCM)",
  "offPeakLabel": "Giờ thường",
  "peakLabel": "Giờ cao điểm",
  "peakDescription": "VD: 7h30–9h30, 12h30–14h, 19h30–21h30",
  "timeUnit": "phút",
  "stayPhaseNote": "Ghi chú cho giai đoạn khách tự chọn lưu lại (nếu có isStayPhase: true).",
  "kpis": [
    { "label": "Cấu trúc Blueprint", "valueOffPeak": "7 Stages • 9 Lanes", "valuePeak": "7 Stages • 9 Lanes", "accent": "default" },
    { "label": "Luồng nhanh", "valueOffPeak": "6 – 11 phút", "valuePeak": "16 – 30 phút", "accent": "dynamic" }
  ],
  "actors": [
    { "name": "Tên ngắn (khớp với field actor)", "label": "Tên hiển thị trên dropdown", "color": "c1" }
  ],
  "stages": [
    {
      "id": 1,
      "code": "S1",
      "name": "1. Tên giai đoạn",
      "en": "English Subtitle",
      "goal": "Customer Goal tại giai đoạn này (dẫn xuống Action).",
      "timeOffPeak": "2 – 5 phút",
      "timePeak": "2 – 5 phút",
      "maxOff": 5,
      "maxPeak": 5,
      "isStayPhase": false,
      "isBottleneck": false,
      "physicalEvidence": ["Mặt tiền & Biển hiệu"],
      "digitalEvidence": ["Google Maps & Review"],
      "customerFlows": [
        {
          "label": "Scenario A: Tìm Online",
          "connectorBefore": null,
          "color": "c1",
          "steps": [
            { "num": 1, "text": "Bước 1..." },
            { "num": 2, "text": "Bước 2..." }
          ]
        },
        {
          "label": "Scenario B: Walk-in",
          "connectorBefore": "hoặc",
          "color": "c4",
          "steps": [
            { "num": 1, "text": "Bước 1..." }
          ]
        }
      ],
      "frontstageSteps": [
        { "step": "Step 1", "actor": "Tên Actor", "text": "Hành động Frontstage..." }
      ],
      "backstageSteps": [
        { "step": "Step 1", "actor": "Tên Actor", "text": "Hành động Backstage..." }
      ],
      "support": [
        { "actor": "Hệ thống", "text": "Mô tả quy trình/hệ thống hỗ trợ..." }
      ],
      "failPoint": "Rủi ro / điểm dễ gãy trải nghiệm tại giai đoạn này.",
      "mitigation": "Giải pháp thiết kế để khắc phục.",
      "inventoryMapping": [
        {
          "actor": "Tên Actor",
          "action": "Action cụ thể",
          "items": ["Item 1", "Item 2"]
        }
      ]
    }
  ],
  "inventoryCatalog": [
    {
      "item": "Tên vật tư / thiết bị / nguyên liệu",
      "cat": "Nhóm phân loại",
      "actor": "Tên Actor",
      "action": "Phục vụ hành động gì",
      "stage": "S1, S2 • Tên giai đoạn",
      "cycle": "Chu kỳ bổ sung / kiểm tra"
    }
  ],
  "failPoints": [
    {
      "stage": "S5 • Pha chế",
      "title": "Tên điểm nghẽn",
      "impact": "Tác động lên khách hàng / vận hành",
      "fix": "Cách khắc phục cụ thể"
    }
  ]
}
```

### Mã màu hợp lệ (`color`)
- `c1` (Xanh dương), `c2` (Xanh lá/Ngọc), `c3` (Xanh cyan), `c4` (Tím), `c5` (Cam), `c6` (Xám xanh), `primary`, `success`, `warning`, `error`.
- Field `accent` trong `kpis`: `"default"` (đen), `"primary"` (xanh dương), `"warning"` (cam), hoặc `"dynamic"` (tự đổi từ xanh dương ở Off-peak sang cam ở Peak).

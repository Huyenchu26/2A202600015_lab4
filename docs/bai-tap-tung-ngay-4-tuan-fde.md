# Bài tập theo ngày — FDE Intern (Data/AI Deployment), bản 4 tuần

**Quy ước:** 5 ngày làm việc/tuần (20 ngày). Mỗi ngày có mục tiêu, đề bài, thời lượng gợi ý, **hướng dẫn đáp án** (dành cho mentor đối chiếu — không phát cho intern trước khi làm), và **DoD** (checklist "hoàn thành").
**Nhịp ngày:** standup 10 phút đầu ngày · cuối tuần review + feedback 1-1.
**Ghi chú giãn/nén độ khó:** với intern Beginner, tăng thời lượng và giảm quy mô dữ liệu; với Advanced, thêm yêu cầu nâng cao ghi ở cuối mỗi tuần.

---

# TUẦN 1 — Onboarding & Nền tảng dữ liệu
**Deliverable cuối tuần:** Notebook làm sạch + phân tích 1 dataset "bẩn", rút ra 3 insight có dẫn chứng.
**KPI tuần:** ≥90% bài daily đạt DoD · notebook chạy end-to-end không lỗi · insight đọc được bởi người không chuyên.

### Ngày 1 — Onboarding & môi trường ⏱ cả ngày
**Mục tiêu:** Sẵn sàng môi trường làm việc; nắm quy trình Git cơ bản; hiểu vai trò FDE.

**Bài tập:**
0. **Gửi email lịch làm việc tuần** (06/07 → 11/07) cho chị huyenctn@v365.vn.
1. **Thiết lập môi trường & làm quen Git:**
   - Cài Python + virtualenv, Jupyter/VS Code, Git.
   - Đọc hiểu Git và các lệnh cơ bản (init/clone, add, commit, push/pull, branch, checkout).
   - Clone repo dự án (được invite qua email), tạo nhánh riêng `feature/huynq`, và tạo commit đầu tiên trên nhánh đó.
2. **Viết 2 bài thu hoạch** (mỗi file giới hạn 500 từ):
   - *"FDE làm gì?"* — bằng lời của mình.
   - *"Git là gì & các lệnh cơ bản"* — tóm tắt những gì đã học.

**Hướng dẫn đáp án:**
- Môi trường: `python --version` chạy được, mở được notebook.
- Git: hiểu luồng `add → commit → push`; biết tạo và chuyển nhánh (`branch`/`checkout`); commit nằm đúng trên nhánh `feature/huynq`, không commit thẳng lên `main`.
- Bài "FDE làm gì" phải nêu được **cả hai mặt**: kỹ thuật (code, data, tích hợp) và tư vấn (làm rõ yêu cầu, demo, bàn giao) — nếu chỉ nói về code là chưa đạt.
- Bài "Git" giải thích đúng các khái niệm lõi (repo, commit, branch, push/pull) bằng ngôn ngữ của mình, không copy tài liệu.

**DoD:**
- [ ] Đã gửi email lịch làm việc tuần cho chị huyenctn@v365.vn.
- [ ] `python`, `jupyter`, `git` chạy được trên máy.
- [ ] Đã clone repo, tạo nhánh `feature/huynq`, và push commit đầu tiên lên nhánh này.
- [ ] Nộp 2 bài thu hoạch (FDE + Git), **mỗi bài ≤ 500 từ**; bài FDE nêu đủ 2 nhóm năng lực.

### Ngày 2 — Python cho dữ liệu (pandas cơ bản) ⏱ cả ngày
**Mục tiêu:** Đọc, khám phá, lọc dữ liệu bằng pandas.
**Bài tập:** Dùng dataset `docs/users_7_7_2026 2_49_38 AM.csv` (bản export danh bạ người dùng Microsoft 365). Trả lời 5 câu hỏi phân tích sau bằng pandas trong notebook:
1. Tổng cộng có bao nhiêu bản ghi người dùng trong file?
2. Phân bố người dùng theo `Usage location` (hoặc `CountryOrRegion`) — mỗi giá trị có bao nhiêu tài khoản, sắp xếp giảm dần?
3. Top 5 `Department` (phòng ban) có nhiều tài khoản nhất là gì?
4. Có bao nhiêu tài khoản đặt `Password never expires = True`? Chiếm bao nhiêu % tổng số? (góc nhìn bảo mật)
5. Số tài khoản được tạo mới (`When created`) theo từng năm là bao nhiêu?
**Hướng dẫn đáp án:** Dùng `read_csv`, `.head()/.info()/.describe()`, boolean indexing, `.loc`, `value_counts()`, `groupby().agg()`, `sort_values`; với câu 5 chuyển `When created` sang datetime bằng `pd.to_datetime(...)` rồi lấy `.dt.year`. Bẫy thường gặp: sai dtype khi đọc (nhiều cột toàn NaN), ô trống ở `Usage location`/`Department` bị bỏ sót làm lệch thống kê (cân nhắc `dropna=False` trong `value_counts`). Đáp án tốt có ghi chú ngắn cho mỗi kết quả.
**DoD:**
- [ ] Notebook chạy từ trên xuống không lỗi.
- [ ] 5 câu hỏi đều có code + kết quả + 1 câu diễn giải.

### Ngày 3 — Làm sạch dữ liệu ⏱ cả ngày
**Mục tiêu:** Xử lý dữ liệu bẩn có phương pháp.
**Bài tập:** Dùng lại chính file `docs/users_7_7_2026 2_49_38 AM.csv` — đây là dữ liệu thật nên đã "bẩn" sẵn. Làm sạch có phương pháp và **ghi lại quyết định** cho từng vấn đề. Tối thiểu xử lý 5 loại lỗi sau:
1. **Giá trị không đồng nhất** ở `Usage location`: có cả `VN`, `Việt Nam`, `Thái Bình`, `Văn phòng Hà Nội`, `VBIM`… — chuẩn hóa về một bộ mã nhất quán (VD gom về `VN`).
2. **Ô thiếu (NaN)**: nhiều cột trống nhiều (VD `Department` ~959 ô trống, `Preferred language`, `City`). Quyết định giữ NaN / điền `"Unknown"` / bỏ cột — và **giải thích vì sao**.
3. **Sai định dạng thời gian**: `When created`, `Last password change time stamp` có hậu tố `Z` — đổi sang datetime bằng `pd.to_datetime(...)`.
4. **Chuỗi lộn xộn / sai cột**: `Preferred language` lẫn cả số điện thoại (`'+84...`, `0964...`); số điện thoại ở `Mobile Phone`/`Phone number` nhiều định dạng — chuẩn hóa (`str.strip/replace`, regex) hoặc đánh dấu giá trị không hợp lệ.
5. **Bản ghi trùng**: kiểm tra trùng theo `User principal name` (khóa định danh) thay vì theo `Display name` — giải thích lý do chọn khóa.
**Hướng dẫn đáp án:** `drop_duplicates(subset=...)`; xử lý thiếu bằng `dropna`/`fillna` — **phải giải thích vì sao chọn cách đó**, không xóa/điền tùy tiện; `astype`/`pd.to_datetime` đổi kiểu; `str.strip/lower/replace`, `.replace({...})`, regex để chuẩn hóa; nhận diện outlier/giá trị lạc cột. Điểm mấu chốt: **mọi thao tác đều có lý do ghi chú**, vì với dữ liệu người dùng thật, xóa nhầm = mất thông tin thật.
**DoD:**
- [ ] Sau làm sạch: 0 dòng trùng, dtypes đúng, chuỗi đã chuẩn hóa.
- [ ] Có bảng/ghi chú "vấn đề → cách xử lý → lý do" cho từng loại lỗi.

### Ngày 4 — SQL trên dữ liệu ⏱ cả ngày
**Mục tiêu:** Truy vấn dữ liệu bằng SQL.
**Bài tập:** Nạp file `docs/users_7_7_2026 2_49_38 AM.csv` vào SQLite/DuckDB thành bảng `users` (VD `df.to_sql("users", conn)`). Tự tạo thêm **1 bảng tra cứu `departments`** gồm các cột `dept_code, dept_name, company` (khoảng 6–10 dòng cho các mã phòng có thật: `TDI`, `BKVN`, `TDME`, `TDICONS`, `Techcon`, `PTC`, `XL247`…) để phục vụ JOIN. Viết 6 truy vấn trả lời 6 câu hỏi nghiệp vụ sau:
1. **(WHERE)** Có bao nhiêu tài khoản bị chặn đăng nhập (`"Block credential" = 1`)?
2. **(GROUP BY + COUNT + ORDER BY)** Mỗi `Department` có bao nhiêu tài khoản? Sắp xếp giảm dần, lấy top 5.
3. **(GROUP BY theo năm)** Số tài khoản tạo mới mỗi năm — trích năm từ `"When created"` bằng `substr("When created",1,4)`.
4. **(WHERE + COUNT + %)** Tỷ lệ tài khoản `"Password never expires" = 1` trên tổng số (góc nhìn bảo mật).
5. **(JOIN)** Join `users` với `departments` theo khóa `users."Department" = departments.dept_code`, đếm số tài khoản theo **`company`** (khối/công ty) và hiển thị `dept_name`.
6. **(NULL / data quality)** Có bao nhiêu tài khoản **không có** `Department` (giá trị NULL)?
Khuyến khích intern trả lời **cùng 1 câu hỏi bằng cả SQL và pandas** (VD câu 2, 3) để thấy hai cách tương đương.
**Hướng dẫn đáp án:** `WHERE`, `GROUP BY` + `COUNT/SUM/AVG`, `ORDER BY`, `JOIN ... ON`, `IS NULL`. Lưu ý: tên cột có dấu cách phải để trong nháy kép (`"Block credential"`); bool trong pandas nạp vào SQLite thành `0/1`; `"When created"` là text có hậu tố `Z` nên dùng `substr(...,1,4)` để lấy năm thay vì `strftime`. Bẫy: quên `GROUP BY` khi dùng hàm tổng hợp; join sai khóa (dept_code ↔ Department); quên `IS NULL` (dùng `= NULL` sẽ luôn sai).
**DoD:**
- [ ] 6 truy vấn chạy đúng, trả đúng 6 câu hỏi.
- [ ] Có ít nhất 1 truy vấn dùng `JOIN` và 1 dùng `GROUP BY`.

**Cách nộp bài:** Nộp notebook `docs/day4.ipynb` (đã có khung sẵn: nạp bảng `users` + `departments` + placeholder 6 câu). Trong notebook, **mỗi câu = 1 ô markdown (câu hỏi) + 1 ô code (`pd.read_sql`) + 1 câu diễn giải kết quả**; câu SQL đặt trong chuỗi `"""..."""`. Có thể kèm file `docs/day4.sql` gom SQL thuần cho mentor đọc nhanh. Trước khi nộp: **Restart & Run All** chạy không lỗi. Làm trên nhánh `feature/huynq`, commit `day 4: SQL queries on users dataset`, **không commit lại file CSV** (dữ liệu nội bộ — ghi rõ đường dẫn để mentor tự đặt vào `docs/`).

> **Nâng cao (Advanced) — SQL phức tạp hơn:** làm thêm ≥3 trong 5 câu sau (mỗi câu buộc dùng một kỹ thuật nâng cao):
> 7. **(HAVING)** Liệt kê các `Department` có **hơn 100** tài khoản — dùng `GROUP BY ... HAVING COUNT(*) > 100` (không được lọc bằng `WHERE COUNT(*)`).
> 8. **(Window — running total)** Số tài khoản tạo **lũy kế** theo năm: `SUM(COUNT(*)) OVER (ORDER BY nam)` — so sánh với số tạo mới mỗi năm ở câu 3 để thấy tổng cộng dồn tiến tới 1900.
> 9. **(Window RANK + PARTITION + JOIN)** Sau khi join `departments`, trong **mỗi `company`** hãy xếp hạng các phòng ban theo số tài khoản: `RANK() OVER (PARTITION BY company ORDER BY COUNT(*) DESC)` và chỉ giữ hạng 1 của mỗi khối.
> 10. **(CTE + tỷ trọng)** Dùng `WITH` tính số tài khoản mỗi `Department`, rồi tính **% của từng phòng trên tổng toàn công ty** bằng `COUNT(*) * 100.0 / SUM(COUNT(*)) OVER ()`.
> 11. **(CASE WHEN — conditional aggregation / pivot)** Với mỗi năm tạo, đếm **song song** trên cùng một hàng: số tài khoản bị chặn và số tài khoản hoạt động — `SUM(CASE WHEN "Block credential"=1 THEN 1 ELSE 0 END)` vs `SUM(CASE WHEN "Block credential"=0 THEN 1 ELSE 0 END)`.
>
> **Nâng cao (xử lý cột `Licenses` đa giá trị):**
> 12. Đếm số tài khoản có gán gói `Microsoft 365 Business Basic` — dùng `WHERE "Licenses" LIKE '%Business Basic%'`.
> 13. Ước lượng **số license trung bình mỗi tài khoản**: các gói nối bằng dấu `+`, nên số license = `LENGTH("Licenses") - LENGTH(REPLACE("Licenses",'+','')) + 1`; lấy `AVG(...)` (bỏ qua ô rỗng bằng `WHERE "Licenses" <> ''`).
> 14. *(DuckDB)* Nếu dùng DuckDB, tách `Licenses` thành nhiều dòng bằng `string_split` + `UNNEST`, rồi `GROUP BY` để tìm **top 5 gói license phổ biến nhất** trong toàn hệ thống.
>
> **Bẫy nâng cao:** dùng `WHERE` cho điều kiện trên hàng, `HAVING` cho điều kiện trên nhóm; window function không được đặt trong `WHERE` (phải bọc bằng subquery/CTE rồi lọc ở ngoài); `RANK` vs `ROW_NUMBER` khác nhau khi có đồng hạng.

### Ngày 5 — EDA + insight + review tuần ⏱ cả ngày
**Mục tiêu:** Tổng hợp kỹ năng tuần thành sản phẩm có giá trị.
**Bài tập:** Trên dataset đã làm sạch ở Ngày 3 (`docs/users_7_7_2026 2_49_38 AM.csv`), làm EDA và rút **3 insight** có số liệu + biểu đồ; viết đoạn tóm tắt cho người **không chuyên**. Làm theo 3 phần:

**A. EDA có cấu trúc (tối thiểu 3 biểu đồ, dùng matplotlib):**
1. **Tăng trưởng tài khoản theo năm** — biểu đồ cột/đường số tài khoản tạo mới theo `When created` (2018→2026). Chú ý năm đỉnh.
2. **Top 10 `Department`** — biểu đồ cột ngang (`barh`), sắp xếp giảm dần.
3. **Chất lượng dữ liệu** — biểu đồ cột **tỷ lệ ô trống (%)** của từng cột (`df.isna().mean().sort_values()`), để lộ các cột gần như rỗng.
4. *(khuyến khích)* Một biểu đồ về **bảo mật**: tỷ lệ `Password never expires` và `Block credential` (tài khoản hoạt động vs bị chặn).

**B. Rút 3 insight** — mỗi insight = **1 con số cụ thể + hàm ý hành động** (không mô tả suông). Gợi ý hướng khai thác (intern tự kiểm chứng lại số từ dữ liệu):
- *Tăng trưởng:* năm nào onboard nhiều nhất, gấp bao nhiêu lần năm trước → hàm ý về quy mô/đợt tuyển.
- *Bảo mật:* tỷ lệ tài khoản `Password never expires = True` cao bất thường → khuyến nghị chính sách hết hạn mật khẩu.
- *Chất lượng dữ liệu:* bao nhiêu % tài khoản thiếu `Department`/`City`/`Title` → danh bạ chưa đủ để phân tích tổ chức, cần chuẩn hóa khâu nhập liệu.

**C. Tóm tắt cho người không chuyên** — 1 đoạn ≤150 từ, không thuật ngữ kỹ thuật, nêu được "phát hiện chính + nên làm gì".

**Hướng dẫn đáp án:** EDA có cấu trúc (phân bố, nhóm nổi bật, mức độ đầy đủ dữ liệu), biểu đồ cơ bản bằng matplotlib (đặt title/nhãn trục rõ ràng). Insight tốt = **có số liệu chứng minh + hàm ý hành động**, không phải mô tả suông ("nhóm A gấp 3 nhóm B → nên ưu tiên…"). Điểm cộng: intern **tự phản biện con số bất thường** (VD 100% password-never-expires thì phải nghi ngờ và nêu rủi ro, không im lặng chấp nhận). Tóm tắt tránh thuật ngữ kỹ thuật, viết như báo cáo cho quản lý.
**DoD:**
- [ ] Notebook chạy end-to-end; có ≥3 biểu đồ.
- [ ] 3 insight, mỗi cái kèm số liệu; 1 đoạn tóm tắt ≤150 từ cho người không chuyên.

> **Nâng cao (Advanced):** thêm feature engineering đơn giản hoặc 1 phép kiểm định thống kê để củng cố insight.

---

# TUẦN 2 — AI/LLM, Prompt & RAG/Eval
**Deliverable cuối tuần:** Tool trích xuất dữ liệu có cấu trúc + RAG prototype nhỏ + báo cáo eval sơ bộ.
**KPI tuần:** độ chính xác trích xuất đạt mốc đặt ra · RAG trả lời có trích nguồn · eval ≥15 câu, đo được tỉ lệ sai/bịa.

### Ngày 6 — Gọi LLM API lần đầu ⏱ cả ngày
**Mục tiêu:** Gọi được LLM API, hiểu request/response và chi phí/độ trễ.
**Bài tập:** Viết script gọi API cho 1 tác vụ đơn giản (tóm tắt / phân loại). Thử đổi `temperature`, `max_tokens` và quan sát khác biệt.
**Hướng dẫn đáp án:** Cấu trúc messages, đọc field kết quả, `try/except` cho lỗi mạng. **Bắt buộc:** API key để trong biến môi trường (`os.environ`), **không hardcode, không commit key**. Nhận biết token ↔ chi phí ↔ độ trễ.
**DoD:**
- [ ] Script gọi API trả kết quả đúng cho ≥3 input.
- [ ] Key nằm trong env var; repo không chứa key.

### Ngày 7 — Prompt engineering ⏱ cả ngày
**Mục tiêu:** Viết prompt hiệu quả và biết so sánh.
**Bài tập:** Chọn 1 task (VD phân loại ticket hỗ trợ). Viết ≥3 biến thể prompt (zero-shot, few-shot, có ràng buộc định dạng). Lập bảng so sánh kết quả và chọn bản tốt nhất.
**Hướng dẫn đáp án:** Nguyên tắc: hướng dẫn rõ ràng, ví dụ (few-shot), dùng dấu phân tách, yêu cầu chia bước. Đánh giá trên cùng bộ input để so sánh công bằng. Đáp án tốt **giải thích được vì sao** bản thắng lại thắng.
**DoD:**
- [ ] ≥3 biến thể prompt cho cùng 1 task, chạy trên cùng ≥5 input.
- [ ] Bảng so sánh + kết luận chọn bản nào & lý do.

### Ngày 8 — Structured output & trích xuất ⏱ cả ngày
**Mục tiêu:** Lấy dữ liệu máy-đọc-được (JSON) từ tài liệu tự do.
**Bài tập:** Xây tool trích xuất các trường có cấu trúc (VD hóa đơn/email → JSON) trên ≥15 tài liệu mẫu.
**Hướng dẫn đáp án:** Yêu cầu model trả **JSON đúng schema**; parse an toàn bằng `try/except`, **retry** khi JSON hỏng; có thể validate bằng pydantic. Phải xử lý được ít nhất 1 ca output lệch chuẩn (không sập chương trình).
**DoD:**
- [ ] Tool chạy trên ≥15 tài liệu, xuất JSON/bảng đúng schema.
- [ ] Có xử lý lỗi khi model trả JSON sai (không crash).
- [ ] Đo độ chính xác trích xuất trên tập mẫu (VD ≥85%).

### Ngày 9 — RAG cơ bản ⏱ cả ngày
**Mục tiêu:** Dựng pipeline RAG chạy đầu-cuối.
**Bài tập:** Trên một bộ tài liệu nhỏ: chunk → embed → vector search → đưa ngữ cảnh vào prompt → trả lời có **trích nguồn**.
**Hướng dẫn đáp án:** Chunk hợp lý (không quá to/nhỏ); embed + tìm theo cosine similarity; nhồi đoạn liên quan vào prompt và yêu cầu trả lời **chỉ dựa trên ngữ cảnh**, kèm nguồn. Bẫy: chunk sai làm retrieval kém; không trích nguồn khiến khó kiểm chứng.
**DoD:**
- [ ] Hỏi–đáp chạy được trên bộ tài liệu; câu trả lời kèm nguồn.
- [ ] Pipeline chạy end-to-end bằng 1 lệnh/1 hàm.

### Ngày 10 — Đánh giá (eval) + review tuần ⏱ cả ngày
**Mục tiêu:** Đo chất lượng giải pháp AI một cách khách quan.
**Bài tập:** Tạo eval set ≥15 câu hỏi có đáp án tham chiếu cho RAG ngày 9. Đo độ đúng + độ bám nguồn (groundedness), phân tích lỗi. Review tuần.
**Hướng dẫn đáp án:** Định nghĩa tiêu chí (đúng/sai, có bịa không, có bám nguồn không); chấm thủ công hoặc LLM-as-judge; phân loại lỗi (retrieval sai vs generation bịa). Báo cáo tốt nêu ≥3 lỗi điển hình + đề xuất cải thiện khả thi.
**DoD:**
- [ ] Eval set ≥15 câu có đáp án tham chiếu.
- [ ] Báo cáo: điểm tổng + tỉ lệ trả lời sai/bịa + ≥3 ví dụ lỗi + đề xuất.

> **Nâng cao (Advanced):** thêm reranking hoặc thử 2 chiến lược chunking và so sánh bằng eval.

---

# TUẦN 3 — Kỹ năng FDE: Scoping, Demo & Mini-project khách hàng
**Deliverable cuối tuần:** Đề xuất giải pháp + demo/POC cho một brief khách hàng giả lập + buổi trình bày.
**KPI tuần:** làm rõ được yêu cầu · scope có tiêu chí thành công đo được · demo chạy · trình bày mạch lạc, trung thực về giới hạn.

### Ngày 11 — Phỏng vấn lấy yêu cầu ⏱ cả ngày
**Mục tiêu:** Biến yêu cầu mơ hồ thành hiểu biết rõ ràng.
**Bài tập:** Nhận brief khách hàng giả lập (cố tình mơ hồ). Chuẩn bị ≥10 câu hỏi làm rõ; mentor đóng vai khách hàng để intern phỏng vấn. Viết biên bản tóm tắt.
**Hướng dẫn đáp án:** Hỏi về **mục tiêu, người dùng, dữ liệu sẵn có, tiêu chí thành công, ràng buộc**. Lỗi phổ biến: **nhảy ngay vào giải pháp** trước khi hiểu vấn đề. Đáp án tốt cho thấy intern gỡ được điểm mơ hồ then chốt.
**DoD:**
- [ ] Danh sách ≥10 câu hỏi làm rõ (không câu nào giả định sẵn giải pháp).
- [ ] Biên bản tóm tắt: vấn đề thật, người dùng, dữ liệu, ràng buộc.

### Ngày 12 — Scoping & đề xuất giải pháp ⏱ cả ngày
**Mục tiêu:** Chốt phạm vi và tiêu chí thành công đo được.
**Bài tập:** Viết tài liệu scope 1–2 trang: vấn đề · giải pháp đề xuất · **tiêu chí nghiệm thu (acceptance)** · dữ liệu cần · rủi ro/giả định · kế hoạch sơ bộ.
**Hướng dẫn đáp án:** Tiêu chí thành công phải **đo được** (VD "độ chính xác ≥85% trên 50 mẫu"), không chung chung ("hoạt động tốt"). Scope thực tế trong thời gian có; nêu rõ giả định & rủi ro.
**DoD:**
- [ ] Tài liệu có đủ 6 mục nêu trên.
- [ ] Ít nhất 1 tiêu chí nghiệm thu định lượng được.

### Ngày 13 — Dựng POC (phần 1) ⏱ cả ngày
**Mục tiêu:** Có luồng chính chạy được sớm.
**Bài tập:** Bắt đầu dựng demo theo scope, tái dùng kỹ năng tuần 2 (trích xuất/RAG). Ưu tiên **lát cắt mỏng đầu-cuối** trước, chưa cần hoàn hảo.
**Hướng dẫn đáp án:** Xây "thin slice" chạy được toàn luồng trên dữ liệu mẫu rồi mới cải thiện; ghi lại giả định. Lỗi thường gặp: cầu toàn 1 phần mà chưa có luồng chạy nào.
**DoD:**
- [ ] Luồng chính chạy được đầu-cuối trên dữ liệu mẫu (dù còn thô).
- [ ] Ghi chú giả định & phần còn thiếu.

### Ngày 14 — Hoàn thiện POC + chuẩn bị demo ⏱ cả ngày
**Mục tiêu:** Demo bấm-chạy-được và kể được câu chuyện.
**Bài tập:** Hoàn thiện phần lõi, thêm giao diện đơn giản (CLI/notebook/Streamlit). Soạn kịch bản demo 5–7 phút + điểm nói chính; xử lý ít nhất 1 edge case.
**Hướng dẫn đáp án:** Demo theo mạch **vấn đề → giải pháp → kết quả**; chuẩn bị trước câu hỏi khó; trung thực về giới hạn. Giao diện chỉ cần đủ để trình diễn.
**DoD:**
- [ ] Demo chạy được đầu-cuối bằng thao tác đơn giản.
- [ ] Kịch bản demo + slide/nói 5–7 phút; xử lý được 1 edge case.

### Ngày 15 — Trình bày & feedback + review tuần ⏱ nửa–cả ngày
**Mục tiêu:** Trình bày thuyết phục, tiếp thu phản hồi.
**Bài tập:** Trình bày demo cho "khách hàng"/mentor, trả lời Q&A, nhận feedback và lập kế hoạch sửa.
**Hướng dẫn đáp án:** Diễn đạt cho người không chuyên, nêu rõ giá trị & giới hạn, giữ bình tĩnh khi bị hỏi vặn. Đánh giá cả **nội dung lẫn cách giao tiếp**.
**DoD:**
- [ ] Hoàn thành buổi trình bày + Q&A.
- [ ] Ghi nhận ≥3 điểm feedback + kế hoạch sửa cụ thể.

> **Nâng cao (Advanced):** thêm 1 tiêu chí phi chức năng (chi phí/độ trễ) vào scope và thể hiện trong demo.

---

# TUẦN 4 — Capstone: Triển khai End-to-End
**Deliverable cuối tuần:** Giải pháp AI hoàn chỉnh (chạy được) + báo cáo eval + bài trình bày nghiệm thu + **tài liệu bàn giao**.
**KPI tuần:** đạt tiêu chí nghiệm thu đã chốt · chạy end-to-end ổn định · tài liệu bàn giao đầy đủ, rõ ràng.

### Ngày 16 — Chốt scope capstone & kế hoạch ⏱ cả ngày
**Mục tiêu:** Kế hoạch capstone được duyệt.
**Bài tập:** Nhận brief + **bộ dữ liệu khách hàng "bẩn"** + mục tiêu nghiệp vụ. Áp dụng kỹ năng scoping tuần 3: chốt phạm vi, tiêu chí nghiệm thu, chia task. Mentor duyệt.
**Hướng dẫn đáp án:** Scope vừa sức 1 tuần; chia nhỏ task có thứ tự; định nghĩa "done" cho capstone. Duyệt trước khi code để tránh lệch hướng.
**DoD:**
- [ ] Kế hoạch + tiêu chí nghiệm thu được mentor duyệt.
- [ ] Danh sách task có thứ tự ưu tiên.

### Ngày 17 — Ingest & xử lý dữ liệu ⏱ cả ngày
**Mục tiêu:** Chuẩn hóa dữ liệu thô sẵn sàng cho giải pháp.
**Bài tập:** Ingest dữ liệu bẩn, làm sạch, chuẩn bị cho bước AI. Ghi lại vấn đề dữ liệu & cách xử lý.
**Hướng dẫn đáp án:** Tái dùng kỹ năng tuần 1; tài liệu hóa quyết định làm sạch (quan trọng khi bàn giao). Kiểm tra chất lượng dữ liệu sau xử lý.
**DoD:**
- [ ] Pipeline ingest → clean chạy được.
- [ ] Ghi chú vấn đề dữ liệu & cách xử lý; dữ liệu sẵn sàng cho bước AI.

### Ngày 18 — Xây giải pháp AI ⏱ cả ngày
**Mục tiêu:** Giải pháp lõi chạy đầu-cuối trên dữ liệu thật.
**Bài tập:** Xây phần AI theo brief (trích xuất/RAG/phân loại), chạy trên dữ liệu capstone.
**Hướng dẫn đáp án:** "Thin slice" trước, cải thiện sau; tổ chức prompt/config gọn gàng, dễ chỉnh. Bám tiêu chí nghiệm thu khi phát triển.
**DoD:**
- [ ] Giải pháp chạy đầu-cuối trên dữ liệu capstone.
- [ ] Code/config tổ chức rõ ràng, có thể chạy lại được.

### Ngày 19 — Eval, tinh chỉnh & đóng gói ⏱ cả ngày
**Mục tiêu:** Đạt tiêu chí nghiệm thu và đưa lên chạy được.
**Bài tập:** Đánh giá theo tiêu chí nghiệm thu, sửa lỗi, đóng gói thành **endpoint (API) hoặc UI đơn giản**. Viết **tài liệu bàn giao**: cách chạy · giả định · giới hạn · hướng phát triển.
**Hướng dẫn đáp án:** Đo lại đúng theo tiêu chí đã chốt; endpoint (FastAPI/Flask) hoặc Streamlit; tài liệu bàn giao phải **đủ để người khác chạy lại được**.
**DoD:**
- [ ] Đạt (hoặc nêu rõ khoảng cách tới) tiêu chí nghiệm thu, có số liệu.
- [ ] Chạy được qua endpoint/UI.
- [ ] Tài liệu bàn giao đủ 4 mục.

### Ngày 20 — Nghiệm thu & bàn giao ⏱ cả ngày
**Mục tiêu:** Trình bày nghiệm thu và bàn giao chuyên nghiệp.
**Bài tập:** Trình bày cuối (demo + kết quả so với tiêu chí), Q&A, bàn giao. Nhìn lại toàn chương trình, so với kết quả khảo sát đầu vào.
**Hướng dẫn đáp án:** Demo mạch lạc; nêu kết quả **đối chiếu tiêu chí nghiệm thu**; trung thực về giới hạn; bàn giao gọn gàng. Buổi retrospective giúp intern thấy tiến bộ và điểm cần học tiếp.
**DoD:**
- [ ] Hoàn thành nghiệm thu + Q&A.
- [ ] Nộp đủ 4 deliverable: giải pháp chạy được · báo cáo eval · slide trình bày · tài liệu bàn giao.

> **Nâng cao (Advanced):** thêm giám sát/logging cơ bản cho giải pháp và một mục "kế hoạch vận hành" trong tài liệu bàn giao.

---

## Gợi ý dùng kèm
- Mỗi ngày, phát cho intern **phần đề bài + DoD**; giữ lại **hướng dẫn đáp án** để chấm.
- Đối chiếu DoD hằng ngày để phát hiện sớm intern đuối hoặc cần thử thách thêm.
- Tôi có thể đóng gói bộ này thành **file Excel theo dõi** (mỗi dòng 1 ngày: đề bài, DoD, trạng thái, điểm) hoặc **file Word** để in phát — cho tôi biết nếu bạn cần.

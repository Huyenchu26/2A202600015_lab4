# -*- coding: utf-8 -*-
"""
Bộ 20 ticket hỗ trợ khách hàng Ngày 7 (prompt engineering).

Đặc điểm gây khó cho model:
- Đa ý định (multi-intent): 1 ticket nhắc cả thanh toán lẫn lỗi kỹ thuật.
- Gây nhiễu (distractor): nhắc "đăng nhập", "trừ tiền"... nhưng vấn đề CHÍNH lại khác.
- Văn phong dài dòng, lộn xộn, có cảm xúc như khách thật.

Quy ước gán nhãn: gold = Ý ĐỊNH CHÍNH (primary intent) mà khách cần giải quyết.
Nhãn: Billing | Technical | Account | Other
Các ca khó có ghi chú lý do trong `notes` để mentor đối chiếu.
"""

tickets = [
    # --- Billing (5) ---
    "Tôi bị trừ tiền hai lần cho cùng một giao dịch gói Premium tháng này, mỗi lần 199k. Nhờ kiểm tra và hoàn lại một khoản.",
    "Hóa đơn tháng này của tôi là 299k nhưng gói tôi đăng ký chỉ 199k. Cho tôi xin giải thích khoản chênh lệch 100k này.",
    "Tôi vừa chuyển khoản nâng cấp lên Premium từ hôm qua nhưng tài khoản vẫn hiển thị gói Free. Tôi đã thử đăng xuất đăng nhập lại nhiều lần mà vẫn vậy.",
    "Gói của tôi tự động gia hạn cả năm mà tôi không hề muốn. Tôi mới bị trừ 2 triệu sáng nay, cho tôi hủy và hoàn tiền được không?",
    "Cho tôi xin hóa đơn VAT của giao dịch ngày 12/06, xuất theo tên công ty TNHH Minh An, mã số thuế 0301234567.",

    # --- Technical (5) ---
    "Mỗi lần tôi bấm nút Thanh toán thì app hiện màn hình trắng rồi tự thoát ra. Tôi thử trên cả điện thoại Android và iPhone đều bị y hệt.",
    "Tôi cố tải tệp hợp đồng lên hệ thống nhưng lần nào cũng báo lỗi 'Upload failed' dù file chỉ 2MB và mạng vẫn bình thường.",
    "Website tải cực kỳ chậm từ sáng nay, nhiều hình ảnh không hiển thị và có trang bị lỗi 503. Không rõ do hệ thống của các bạn hay do máy tôi.",
    "Tôi xuất báo cáo ra PDF thì toàn bộ chữ tiếng Việt bị vỡ font, dấu bị mất hết. Bản xem trên web thì vẫn đúng.",
    "Hệ thống gửi cho tôi 27 email thông báo giống hệt nhau chỉ trong 5 phút cho cùng một đơn hàng. Chắc chắn có lỗi gì đó.",

    # --- Account (5) ---
    "Tôi bấm 'Quên mật khẩu' đến 5 lần nhưng không nhận được email đặt lại nào, kiểm tra cả hộp thư rác cũng không thấy.",
    "Tôi đổi điện thoại mới và mất thiết bị cài 2FA cũ nên giờ không đăng nhập được. Làm sao để tắt 2FA hoặc khôi phục quyền truy cập?",
    "Tôi muốn đổi email đăng nhập từ an.nguyen@gmail.com sang email công ty an@minhan.vn mà không tìm thấy chỗ chỉnh trong phần cài đặt.",
    "Tài khoản của tôi bị khóa sau khi tôi nhập sai mật khẩu vài lần. Giờ tôi nhớ mật khẩu rồi, nhờ mở khóa giúp tôi.",
    "Tôi có hai tài khoản tạo nhầm bằng hai email khác nhau, muốn gộp lịch sử về một tài khoản và xóa hẳn tài khoản kia theo yêu cầu bảo mật dữ liệu.",

    # --- Other (5) ---
    "Cho tôi hỏi bộ phận hỗ trợ làm việc mấy giờ, cuối tuần có trực không? Tôi muốn gọi vào lúc tiện.",
    "Bên tôi là công ty phân phối thiết bị, muốn hợp tác làm đại lý cho sản phẩm của các bạn. Liên hệ bộ phận nào để bàn?",
    "Tôi muốn đề xuất một tính năng: cho phép hẹn giờ gửi báo cáo tự động hằng tuần. Nhiều đồng nghiệp của tôi cũng mong có tính năng này.",
    "Chỉ muốn nói cảm ơn đội ngũ, dịch vụ dùng rất ổn và hỗ trợ nhiệt tình. Cứ giữ phong độ nhé!",
    "Sản phẩm của các bạn có dùng được khi tôi ra nước ngoài công tác không, hay chỉ hoạt động ở Việt Nam?",
]

gold_labels = [
    # Billing
    "Billing",
    "Billing",
    "Billing",   # TRICKY: nhắc "đăng xuất đăng nhập" (Account) nhưng vấn đề chính là tiền đã trả chưa vào gói
    "Billing",
    "Billing",
    # Technical
    "Technical", # TRICKY: nhắc "Thanh toán" (Billing) nhưng vấn đề chính là app crash
    "Technical",
    "Technical",
    "Technical",
    "Technical",
    # Account
    "Account",   # TRICKY: email không tới có thể trông như lỗi Technical, nhưng ý định chính là khôi phục truy cập
    "Account",
    "Account",
    "Account",
    "Account",
    # Other
    "Other",
    "Other",
    "Other",     # feature request — không phải bug nên xếp Other, không phải Technical
    "Other",
    "Other",
]

# Ghi chú cho các ca khó (index 0-based) — mentor dùng để đối chiếu, KHÔNG đưa cho model.
notes = {
    2: "Đã thanh toán nhưng gói chưa cập nhật -> Billing (provisioning), dù có tín hiệu Account (đăng nhập lại).",
    5: "App crash khi bấm Thanh toán -> Technical (lỗi ứng dụng), không phải Billing dù có từ 'Thanh toán'.",
    10: "Email reset không tới -> Account (khôi phục truy cập). Distractor: nghe giống lỗi gửi mail (Technical).",
    17: "Đề xuất tính năng mới -> Other, không phải Technical (không có lỗi nào cả).",
}

assert len(tickets) == len(gold_labels) == 20, "tickets và gold_labels phải cùng 20 phần tử"

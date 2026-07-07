# Bài thu hoạch: Git là gì? Các khái niệm cốt lõi và lệnh cơ bản

## Git là gì?

Git là một hệ thống quản lý phiên bản giúp theo dõi toàn bộ quá trình thay đổi của một dự án. Thay vì lưu nhiều bản sao của cùng một dự án, Git ghi lại từng lần chỉnh sửa theo từng mốc thời gian. Nhờ đó, lập trình viên có thể biết ai đã sửa gì, sửa khi nào và dễ dàng quay lại phiên bản trước nếu xảy ra lỗi.

Git đặc biệt hữu ích khi nhiều người cùng phát triển một dự án vì mỗi người có thể làm việc trên máy của mình rồi đồng bộ các thay đổi lên kho lưu trữ chung.

## Các khái niệm cốt lõi

### Repository (Repo)

Repository là nơi chứa toàn bộ mã nguồn và lịch sử thay đổi của dự án. Có thể hiểu đơn giản repo giống như một "thư mục thông minh", ngoài việc lưu các file còn lưu cả lịch sử chỉnh sửa, các nhánh và các phiên bản đã tạo.

Repository có thể nằm trên máy tính cá nhân (Local Repository) hoặc trên các dịch vụ như GitHub (Remote Repository).

### Commit

Commit là một lần lưu lại trạng thái của dự án tại một thời điểm. Mỗi commit đều có nội dung mô tả để giải thích những gì đã thay đổi, ví dụ như sửa lỗi, thêm chức năng hoặc cập nhật giao diện.

Các commit tạo thành lịch sử phát triển của dự án, giúp dễ dàng theo dõi và khôi phục khi cần.

### Branch

Branch (nhánh) là một phiên bản phát triển riêng của dự án. Thay vì sửa trực tiếp trên nhánh chính, lập trình viên thường tạo nhánh mới để phát triển tính năng hoặc sửa lỗi. Khi hoàn thành và đã kiểm tra, nhánh đó sẽ được gộp trở lại nhánh chính.

Cách làm này giúp nhiều người có thể làm việc song song mà không ảnh hưởng đến nhau.

### Push và Pull

* **Push** là thao tác đưa các commit từ máy tính cá nhân lên repository trên máy chủ để chia sẻ với các thành viên khác.
* **Pull** là thao tác lấy các thay đổi mới nhất từ repository trên máy chủ về máy tính để cập nhật dự án.

Hai lệnh này giúp dữ liệu giữa các thành viên luôn được đồng bộ.

## Các lệnh Git cơ bản

* `git init`: Khởi tạo một Git Repository.
* `git clone`: Sao chép một repository có sẵn về máy.
* `git status`: Kiểm tra trạng thái các file trong dự án.
* `git add`: Đưa các thay đổi vào vùng chờ (staging).
* `git commit -m "message"`: Lưu các thay đổi thành một commit mới.
* `git branch`: Xem hoặc tạo nhánh.
* `git switch <branch>` hoặc `git checkout <branch>`: Chuyển sang nhánh khác.
* `git merge`: Gộp một nhánh vào nhánh hiện tại.
* `git pull`: Cập nhật thay đổi mới nhất từ repository từ xa.
* `git push`: Đẩy các commit từ máy lên repository từ xa.
* `git log`: Xem lịch sử các commit.

## Kết luận

Git là công cụ quản lý phiên bản giúp việc phát triển phần mềm trở nên an toàn và hiệu quả hơn. Việc hiểu rõ các khái niệm như Repository, Commit, Branch và Push/Pull sẽ giúp lập trình viên quản lý mã nguồn tốt hơn, phối hợp làm việc nhóm dễ dàng hơn và hạn chế rủi ro trong quá trình phát triển dự án. Bên cạnh đó, nắm vững các lệnh Git cơ bản là nền tảng cần thiết để làm việc với các dự án thực tế.

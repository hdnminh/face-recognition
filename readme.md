# **Face Recognition - **

## I. THÔNG TIN CHUNG

### 1. THÔNG TIN NHÓM
#### 1.1. Thông tin thành viên trong nhóm
|**STT**|**MSSV**|**Họ và tên**|**Email**|
|---|-----------------------|--------|---------------------|
|01|20120210|Trần Thị Kim Tiến|20120210@student.hcmus.edu.vn|
|02|20120246|Nguyễn Hoàng Anh|20120246@student.hcmus.edu.vn|
|03|20120307|Phạm Gia Khiêm|20120307@student.hcmus.edu.vn|
|04|20120328|Hoàng Đức Nhật Minh|20120328@student.hcmus.edu.vn|

#### 1.2. Phân chia công việc
![image](https://github.com/hoangducnhatminh/face-recognition/assets/76483242/578ac0ae-d3ce-4be7-98a7-678dcf9a81ab)


### 2. GIỚI THIỆU VỀ BÀI BÁO
- Tên của bài báo là: “ArcFace: Additive Angular Margin Loss for Deep Face Recognition”.
- Tác giả: Jiankang Deng, Jia Guo, Xiannan Xue, Stefanos Zafeiriou.
- Được công bố vào tại hội nghị IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR) năm 2019.
- Ngày bài báo được công bố lên IEEE: ngày 09/01/2020.

## II. QUÁ TRÌNH HOÀN THIỆN CODE DEMO
### Nguồn tham khảo code
- Nhóm tham khảo code từ repo: https://github.com/santapo/face_surveillance
- Fix code và chạy được code.
- Vì code sử dụng mô hình pretrain, nên nhóm không cần train lại mô hình.
- Xây dựng bộ dữ liệu để test.

### Test code
- Tạo thư mục: face_db tại thư mục gốc. Bên trong face_db, tạo các thư mục con, với mỗi thư mục con là một class - hay một người. Bên trong thư mục con đó là tập tất cả các ảnh của người đó.
- cd vào thư mục tests, chạy lệnh: python test_main.py
## III. KẾT QUẢ ĐẠT ĐƯỢC
### 1. Kết quả đạt được thực nghiệm
- Không tốt như bài báo, có lẽ là do vì data test khác điều kiện với data được dùng để train.

### 2. Những khó khăn và hạn chế trong quá trình thực hiện đồ án
- Đồ án khó, cần đọc và nghiên cứu nhiều về bài toán face recognition.







1
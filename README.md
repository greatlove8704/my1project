# Dự đoán giá vé máy bay
Project 16: https://drive.google.com/drive/folders/18FkSxMvTpR2KQrP5OZTRWZtPMIuz7amW?usp=sharing

Nhóm gồm: Nguyễn Bảo Sơn 22022539 và Chu Huỳnh Đức 22022612

1.Tổng quan: 

Dự án như cái tên nhằm mục đích dự đoán giá vé máy bay dựa trên 1 tập dự liệu nhất định. Giá vé được dự đoán dựa trên hãng máy bay, địa điểm, trạm dừng, ngày giờ, hạng vé thường hay business. Dự án bao gồm 1 số tính năng:

-Phân tích dữ liệu: Dữ liệu được phân tích sâu chuyên sâu để tìm các mẫu và ẩn thông tin chi tiết có thể được sử dụng để đưa ra độ chính xác dự đoán.

-Lựa chọn và đào tạo mô hình: Dự án bao gồm một số mô hình được đào tạo và thử nghiệm để tìm ra mô hình tốt nhất để đưa ra dự đoán.

-Kiểm tra dự đoán và độ chính xác: Dự án bao gồm tính năng đưa ra dự đoán dựa trên mô hình đã chọn. Các dự đoán được kiểm tra độ chính xác so với tập dữ liệu thử nghiệm.

2.Dataset:

Tập dữ liệu được sử dụng trong dự án này là tập dữ liệu chuyến bay chứa hơn 10000 bản ghi và 11 tính năng. Các tính năng này bao gồm tên hãng hàng không, ngày hành trình, thành phố nguồn và điểm đến, tuyến đường, thời gian khởi hành và đến, thời gian, số điểm dừng, thông tin bổ sung và giá vé . Bộ dữ liệu bao gồm cả tính năng phân loại và tính năng số, đồng thời sẽ được sử dụng để đưa ra dự đoán về giá đặt vé máy bay.

3.Analysis and Model Training:

1.setting up Python environment for data analysis and visualization:



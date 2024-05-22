# Dự đoán giá vé máy bay
Project 16: (file random_model.pkl quá lớn nên để tại đây) https://drive.google.com/drive/folders/18FkSxMvTpR2KQrP5OZTRWZtPMIuz7amW?usp=sharing

Nhóm gồm: Chu Huỳnh Đức 22022612

1.Tổng quan: 

Dự án như cái tên nhằm mục đích dự đoán giá vé máy bay dựa trên 1 tập dự liệu nhất định. Giá vé được dự đoán dựa trên hãng máy bay, địa điểm, trạm dừng, ngày giờ, hạng vé thường hay business. Dự án bao gồm 1 số tính năng:

-Phân tích dữ liệu: Dữ liệu được phân tích sâu chuyên sâu để tìm các mẫu và ẩn thông tin chi tiết có thể được sử dụng để đưa ra độ chính xác dự đoán.

-Lựa chọn và đào tạo mô hình: Dự án bao gồm một số mô hình được đào tạo và thử nghiệm để tìm ra mô hình tốt nhất để đưa ra dự đoán.

-Kiểm tra dự đoán và độ chính xác: Dự án bao gồm tính năng đưa ra dự đoán dựa trên mô hình đã chọn. Các dự đoán được kiểm tra độ chính xác so với tập dữ liệu thử nghiệm.

2.Dataset:

Tập dữ liệu được sử dụng trong dự án này là tập dữ liệu chuyến bay chứa hơn 10000 bản ghi và 11 tính năng. Các tính năng này bao gồm tên hãng hàng không, ngày hành trình, thành phố nguồn và điểm đến, tuyến đường, thời gian khởi hành và đến, thời gian, số điểm dừng, thông tin bổ sung và giá vé . Bộ dữ liệu bao gồm cả tính năng phân loại và tính năng số, đồng thời sẽ được sử dụng để đưa ra dự đoán về giá đặt vé máy bay.

3.Analysis and Model Training:

1.setting up Python environment for data analysis and visualization:

<img width="623" alt="Screenshot 2024-05-22 at 23 41 59" src="https://github.com/greatlove8704/my1project/assets/150203007/9965de63-a339-4c28-9b44-47d39db82722">

![](https://private-user-images.githubusercontent.com/150203007/331850282-93997b42-10ad-479f-b716-5e3462cbb1d1.png?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3MTYwOTgxMTcsIm5iZiI6MTcxNjA5NzgxNywicGF0aCI6Ii8xNTAyMDMwMDcvMzMxODUwMjgyLTkzOTk3YjQyLTEwYWQtNDc5Zi1iNzE2LTVlMzQ2MmNiYjFkMS5wbmc_WC1BbXotQWxnb3JpdGhtPUFXUzQtSE1BQy1TSEEyNTYmWC1BbXotQ3JlZGVudGlhbD1BS0lBVkNPRFlMU0E1M1BRSzRaQSUyRjIwMjQwNTE5JTJGdXMtZWFzdC0xJTJGczMlMkZhd3M0X3JlcXVlc3QmWC1BbXotRGF0ZT0yMDI0MDUxOVQwNTUwMTdaJlgtQW16LUV4cGlyZXM9MzAwJlgtQW16LVNpZ25hdHVyZT05NGRjYmE3ZWU4NmJiYTUxZjFjMjM3NjVkZTA4MzBmMTVlMDkzODAyM2MyODBiMDJkMDM5ZTk1ZDBmN2U2NGRhJlgtQW16LVNpZ25lZEhlYWRlcnM9aG9zdCZhY3Rvcl9pZD0wJmtleV9pZD0wJnJlcG9faWQ9MCJ9.xoHTD_RVpgB4vrMzXbJnQgu4-kAuwux2T3r20vYQeL0)

2.display dataframe:

3 hàng đầu:

<img width="624" alt="Screenshot 2024-05-22 at 23 43 47" src="https://github.com/greatlove8704/my1project/assets/150203007/5db12dde-3f10-41ad-b36a-2092f2bdf0e1">

Các hãng hàng không:

<img width="624" alt="Screenshot 2024-05-22 at 23 44 07" src="https://github.com/greatlove8704/my1project/assets/150203007/d187f1f1-2c21-49a8-b2fe-51549d0d2e97">

Giá cả các hãng hàng không(dùng seaborn tạo catplot):

<img width="637" alt="Screenshot 2024-05-22 at 23 44 21" src="https://github.com/greatlove8704/my1project/assets/150203007/57b4c4eb-1dfe-4349-99f7-46310d1a3899">

Các hãng nhỏ lẻ được tổng hợp dưới cái tên others để dễ quan sát hơn, đa số là những hãng vô danh tiểu tốt vắng tanh như chùa bà đanh nếu so với hãng khác:

<img width="622" alt="Screenshot 2024-05-22 at 23 44 43" src="https://github.com/greatlove8704/my1project/assets/150203007/1fa45fef-badd-4ea1-bfe5-6b0df4f5ab0b">

Loại bỏ những hàng có missing values, dọn đường để tiến tới dataframe sạch nhất có thể:

<img width="623" alt="Screenshot 2024-05-22 at 23 44 57" src="https://github.com/greatlove8704/my1project/assets/150203007/19615d5d-76e1-451a-9090-0315b9c39bb1">

Giải quyết các giá trị ngoại lệ bằng iqr, biểu diễn mức giá giới hạn bằng biểu đồ cho dễ nhìn:

<img width="623" alt="Screenshot 2024-05-22 at 23 45 13" src="https://github.com/greatlove8704/my1project/assets/150203007/e67d1067-1fa6-4871-98d4-d4c274a038d1">

Sau khi xử lý các giá trị ngoại lệ, biểu đồ giá cả đã chính xác hơn trước:

<img width="623" alt="Screenshot 2024-05-22 at 23 45 29" src="https://github.com/greatlove8704/my1project/assets/150203007/45088f2b-be25-49e9-9bcb-8241ada311d5">

Xử lý ngày giờ: convert to datetime, trích xuất thành phần năm, tháng, ngày, tuần trong năm, thời gian khởi hành trích xuất giờ, phút; thời gian đến trích xuất giờ, phút tương tự; khoảng thời gian bay tương tự

<img width="623" alt="Screenshot 2024-05-22 at 23 46 10" src="https://github.com/greatlove8704/my1project/assets/150203007/763308e7-8793-4e80-a38f-880f0bc900dd">

Dùng hàm stops Xác định số điểm dừng, 4 đồng nghĩa với non ko có điểm dừng

<img width="621" alt="Screenshot 2024-05-22 at 23 47 12" src="https://github.com/greatlove8704/my1project/assets/150203007/9654fb73-7860-4cc2-a70b-03c6c9604e91">

biểu đồ số chuyến đi dựa trên ngày trong tháng:

<img width="623" alt="Screenshot 2024-05-22 at 23 47 24" src="https://github.com/greatlove8704/my1project/assets/150203007/9dccd0c2-674d-4d1c-b738-7a17b46fdbc2">

biểu đồ số chuyến đi dựa trên ngày trong tuần:

<img width="624" alt="Screenshot 2024-05-22 at 23 47 38" src="https://github.com/greatlove8704/my1project/assets/150203007/ffd4a9f1-70d3-43ed-8aa2-dea9e3f8fad1">

Biểu đồ số chuyến đi dựa trên tháng trong năm:

<img width="621" alt="Screenshot 2024-05-22 at 23 48 19" src="https://github.com/greatlove8704/my1project/assets/150203007/fb5c51a4-b828-44ad-b8d2-434228831b86">

Và hàng loạt những hình ảnh phân tích khác như:

Biểu đồ ngày trong tháng vs tháng

<img width="624" alt="Screenshot 2024-05-22 at 23 48 38" src="https://github.com/greatlove8704/my1project/assets/150203007/9766c5ee-e2c5-475b-8e41-0f7ef33d4831">

Biểu đồ tuần trong năm và tháng

<img width="624" alt="Screenshot 2024-05-22 at 23 48 53" src="https://github.com/greatlove8704/my1project/assets/150203007/a0e10ac3-2bac-42cf-b9b8-9fdccd7a0be8">

Biểu đồ tuần trong năm và ngày trong tháng

<img width="624" alt="Screenshot 2024-05-22 at 23 49 13" src="https://github.com/greatlove8704/my1project/assets/150203007/4bfeb248-e0ea-4126-b43c-b722a823a017">

Biểu đồ tuần trong năm và ngày trong tuần

<img width="624" alt="Screenshot 2024-05-22 at 23 49 49" src="https://github.com/greatlove8704/my1project/assets/150203007/5e27d59d-a135-4687-a831-1a0d3f5f8401">

Biểu đồ hãng hàng không và ngày trong tuần

<img width="626" alt="Screenshot 2024-05-22 at 23 50 11" src="https://github.com/greatlove8704/my1project/assets/150203007/0053a20e-9eff-4590-b75a-73c090eba1f0">

Biểu đồ hãng hàng không và tháng

<img width="624" alt="Screenshot 2024-05-22 at 23 50 29" src="https://github.com/greatlove8704/my1project/assets/150203007/2a331b37-11e2-4390-9932-909742ff629f">

Biểu đồ địa điểm đi

<img width="624" alt="Screenshot 2024-05-22 at 23 50 50" src="https://github.com/greatlove8704/my1project/assets/150203007/585e347f-b7ce-4ee2-bee2-79b69faf2bf7">


Biểu đồ địa điểm đến

<img width="625" alt="Screenshot 2024-05-22 at 23 51 05" src="https://github.com/greatlove8704/my1project/assets/150203007/4b61f4cb-782f-45dc-8501-9e91f583f471">


Chuẩn bị và check các dataframe chuẩn bị train

<img width="626" alt="Screenshot 2024-05-22 at 23 51 20" src="https://github.com/greatlove8704/my1project/assets/150203007/40a4a801-0062-4dcd-8cf8-dd855f9f530a">

Chuẩn bị dataframe để dùng machine learning:

<img width="626" alt="Screenshot 2024-05-22 at 23 51 38" src="https://github.com/greatlove8704/my1project/assets/150203007/15787dce-8d70-419d-929c-ffee817dd687">

3. Train test split: chia tập dữ liệu thành các tập huấn luyện và kiểm tra:

Sử dụng hàng loạt các thuật toán hồi quy như linear, dicision tree, random forest,extra tree, adaboost,gradientboosting,bagging để tìm ra thuật toán hiệu quả

<img width="626" alt="Screenshot 2024-05-22 at 23 51 51" src="https://github.com/greatlove8704/my1project/assets/150203007/39d7e99c-5f6e-4721-82b1-1b2ba7020def">

Dễ thấy randomforest là thuật toán hiệu suất cao nhất, vậy còn chần chừ gì nữa:

<img width="625" alt="Screenshot 2024-05-22 at 23 52 09" src="https://github.com/greatlove8704/my1project/assets/150203007/c6db26c9-3fdb-4547-97d4-732d1ff459fa">

Bảng features value

<img width="624" alt="Screenshot 2024-05-22 at 23 52 43" src="https://github.com/greatlove8704/my1project/assets/150203007/6de37616-a143-4c4a-b507-4d3f17ef3534">

Dùng seaborn để visualize dễ thấy sự chênh lệch giữa giá thực tế và dự đoán:

<img width="625" alt="Screenshot 2024-05-22 at 23 52 58" src="https://github.com/greatlove8704/my1project/assets/150203007/a3e2fbe4-319d-4bf3-9a6e-ad3b1d0d49a3">

Dùng seaborn để visualize dễ thấy sai số giữa dự đoán và thực tế:

<img width="1163" alt="Screenshot 2024-05-19 at 13 18 22" src="https://github.com/greatlove8704/my1project/assets/150203007/d7de6eee-98fb-46f6-9f17-5f0ba2da7964">
Mối quan hệ giữa giá dự đoán và thực tế:

<img width="1163" alt="Screenshot 2024-05-19 at 13 19 10" src="https://github.com/greatlove8704/my1project/assets/150203007/5ddce461-ec17-4953-818d-295e00e05aba">
4. installation và run web app:


Các file cần thiết:


- app.py: là main file để chạy web app, chứa neural network model, front end design python dash


- Model.pkl: là model đã train sử dụng random forest regression, chứa trọng số và architecture của resnet50 model


- Test_data.csv: dữ liệu được sử dụng để huấn luyện


- function.py: web app interface dùng để creat input field, processing user selection và đưa ra kết quả 


cách run: hãy mở untitled9.ipynb trong google colab, sau đó upload các file cần thiết: app.py, function.py, df.csv, test_data.csv, random_model.pkl, tạo thêm 1 folder đặt tên là assets sau đó upload 2 hình ảnh ở trong assets vào. Sau cùng ấn run all là được


- Display prediction:
<img width="1159" alt="Screenshot 2024-05-19 at 13 21 24" src="https://github.com/greatlove8704/my1project/assets/150203007/29d5ec91-75fc-499e-bdf9-1a94d77aa5d4">
- Others features:
<img width="1158" alt="Screenshot 2024-05-19 at 13 22 05" src="https://github.com/greatlove8704/my1project/assets/150203007/888a3126-f791-4cfe-b42c-9fe57a9415c9">
<img width="1159" alt="Screenshot 2024-05-19 at 13 22 37" src="https://github.com/greatlove8704/my1project/assets/150203007/1b38622e-5d89-4524-95c0-8a98ff126df2">
<img width="1160" alt="Screenshot 2024-05-19 at 13 22 59" src="https://github.com/greatlove8704/my1project/assets/150203007/b22fb352-26e0-419f-b954-abb13022e73c">
<img width="1162" alt="Screenshot 2024-05-19 at 13 23 14" src="https://github.com/greatlove8704/my1project/assets/150203007/bc77f96a-3adf-4b2a-b3d0-96ec22668c27">
Thanks for watching :))












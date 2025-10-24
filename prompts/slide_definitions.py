# -*- coding: utf-8 -*-
"""
This file contains the definitions for the slides to be generated in the presentation.
"""

slide_definitions = [
    # Slide 1: Title
    {
        "slide_type": "title_slide",
        "title": "PHÂN TÍCH HIỆU QUẢ KINH DOANH 2025 & ĐỊNH HƯỚNG CHIẾN LƯỢC 2026-2030",
        "subtitle": "Đánh giá hoạt động 2025 so với 2024 & Lộ trình phát triển trong bối cảnh vĩ mô mới",
        "notes": "Trình bày bởi Techcombank. Mục tiêu: Tổng quan hiệu quả tài chính 2025, đánh giá rủi ro, đề xuất chiến lược 2026-2030."
    },
    # Slide 2: Executive Summary
    {
        "slide_type": "title_and_content",
        "title": "Tóm Tắt Điều Hành (Executive Summary)",
        "content_bullets": [
            "Điểm sáng 2025: Tăng trưởng lợi nhuận vượt kế hoạch, tỷ lệ CASA tiếp tục được cải thiện.",
            "Thách thức chính 2025: Tỷ lệ NPL tăng nhẹ, NIM chịu áp lực từ chi phí vốn.",
            "Định hướng chiến lược 2026-2030: Tăng trưởng bền vững, tăng tốc chuyển đổi số, đa dạng hóa nguồn thu.",
            "Khuyến nghị trọng yếu: Tập trung vào chất lượng tài sản, tối ưu hóa chi phí vận hành và đầu tư vào công nghệ."
        ]
    },
    # Slide 3: Financial Overview
    {
        "slide_type": "title_and_chart",
        "title": "Tổng Quan Hiệu Quả Tài Chính 6M/2025 vs 6M/2024",
        "chart_definition": {
            "data_source_title": "1H25 Financial Highlights",
            "data_key": "Total assets",
            "chart_type": "bar",
            "x_axis_keys": ["6M24", "6M25"],
            "chart_title": "Tổng Tài Sản (Tỷ VND)",
            "x_label": "Kỳ",
            "y_label": "Tỷ VND"
        },
        "content_bullets": [
            "So sánh các chỉ số chính giữa 6M/2025 và 6M/2024:",
            "Tổng tài sản (Total Assets)",
            "Tiền gửi khách hàng (Customer Deposits)",
            "Lợi nhuận trước thuế (PBT)"
        ]
    },
    # Slide 4: Profitability & Operational Efficiency
    {
        "slide_type": "title_and_chart",
        "title": "Phân Tích Hiệu Quả Sinh Lời & Hiệu Suất Hoạt Động",
        "chart_definition": {
            "data_source_title": "1H25 Financial Highlights",
            "data_key": "NIM (LTM)",
            "chart_type": "bar",
            "x_axis_keys": ["6M24", "6M25"],
            "chart_title": "Tỷ Lệ Thu Nhập Lãi Thuần (NIM)",
            "x_label": "Kỳ",
            "y_label": "Tỷ lệ (%)"
        },
        "content_bullets": [
            "Các chỉ số hiệu quả sinh lời chính:",
            "ROA (Return on Assets)",
            "ROE (Return on Equity)",
            "CIR (Cost-to-Income Ratio)"
        ]
    },
    # Slide 5: Asset Quality & Funding Structure
    {
        "slide_type": "title_and_chart",
        "title": "Phân Tích Chất Lượng Tài Sản & Nguồn Vốn",
        "chart_definition": {
            "data_source_title": "1H25 Financial Highlights",
            "data_key": "NPL",
            "chart_type": "bar",
            "x_axis_keys": ["6M24", "6M25"],
            "chart_title": "Tỷ Lệ Nợ Xấu (NPL Ratio)",
            "x_label": "Kỳ",
            "y_label": "Tỷ lệ (%)"
        },
        "content_bullets": [
            "Các chỉ số chất lượng tài sản và nguồn vốn:",
            "Tỷ lệ bao phủ nợ xấu (Coverage Ratio)",
            "Tỷ lệ CASA (CASA Ratio)",
            "Tỷ lệ LDR (Loan-to-Deposit Ratio)"
        ]
    },
    # Slide 6: Key Risks & Outlook
    {
        "slide_type": "title_and_content",
        "title": "Đánh Giá Rủi Ro Chính & Triển Vọng",
        "content_bullets": [
            "Rủi ro tín dụng: Diễn biến NPL, rủi ro tập trung ngành/khách hàng.",
            "Rủi ro thanh khoản: Tình hình LDR, khả năng huy động vốn.",
            "Rủi ro thị trường: Biến động lãi suất, tỷ giá hối đoái.",
            "Rủi ro hoạt động: An ninh mạng, tuân thủ quy định.",
            "Rủi ro vĩ mô: Lạm phát, tăng trưởng GDP, chính sách tiền tệ."
        ]
    },
    # Slide 7: Financial Forecast
    {
        "slide_type": "title_and_content",
        "title": "Dự Báo Tài Chính 2026-2030",
        "content_bullets": [
            "Giả định vĩ mô: Tăng trưởng GDP, lạm phát, lãi suất điều hành.",
            "Giả định kinh doanh: Tốc độ tăng trưởng tín dụng, mục tiêu CASA, NPL, CIR.",
            "Dự báo các chỉ tiêu chính: Tổng tài sản, Lợi nhuận, ROE, NIM, CIR."
        ]
    },
    # Slide 8: Strategic Pillars
    {
        "slide_type": "title_and_content",
        "title": "Các Trụ Cột & Sáng Kiến Chiến Lược 2026-2030",
        "content_bullets": [
            "Tăng trưởng Bền vững & Phát triển Khách hàng trọng tâm.",
            "Nâng cao Chất lượng Tài sản & Quản trị Rủi ro hiệu quả.",
            "Tối ưu hóa Hiệu quả Hoạt động & Chuyển đổi số toàn diện.",
            "Đa dạng hóa Nguồn Thu & Phát triển Dịch vụ Giá trị Gia tăng."
        ]
    },
    # Slide 9: Investment Strategy
    {
        "slide_type": "title_and_content",
        "title": "Gợi Ý Chiến Lược Đầu Tư & Phân Bổ Nguồn Lực",
        "content_bullets": [
            "Công nghệ & Chuyển đổi số: Core banking, cloud, AI/ML.",
            "Nguồn nhân lực: Đào tạo kỹ năng số, thu hút nhân tài.",
            "Phát triển sản phẩm & kênh phân phối: Sản phẩm mới, ngân hàng số.",
            "Cơ sở hạ tầng quản trị rủi ro: Hệ thống quản lý rủi ro tích hợp."
        ]
    },
    # Slide 10: Conclusion
    {
        "slide_type": "title_slide",
        "title": "Kết Luận & Các Bước Tiếp Theo",
        "subtitle": "Thảo luận, phê duyệt kế hoạch và triển khai các sáng kiến chiến lược.",
        "notes": "Q&A"
    }
]

image_assets = {
    "company_logo": "images/company_logo.png",
    "q2_summary_icon": "images/q2_summary_icon.png",
    "rnd_investment": "images/rnd_investment.jpg",
    "marketing_strategy": "images/marketing_strategy.png",
    "sales_achievement": "images/sales_achievement.png",
    "team_photo": "images/team_photo.jpg"
}

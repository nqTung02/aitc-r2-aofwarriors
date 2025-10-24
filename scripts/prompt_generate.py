import requests
import json
import os
from dotenv import load_dotenv

def generate_presentation_script():
    """
    Generates a Python script for creating a PowerPoint presentation by calling an AI API.
    """
    # --- Prompt Definition ---
    prompt = """Tôi muốn bạn tạo một mã Python hoàn chỉnh, chạy trên Jupyter Notebook, để tự động tạo một tệp `.pptx` (PowerPoint presentation) dựa trên các thông tin và dữ liệu từ các file local.

**Yêu cầu:**
1.  **Sử dụng thư viện:** `python-pptx`, `pandas`, `matplotlib.pyplot`.
2.  **Đọc dữ liệu:**
    *   Đọc cấu trúc slide và danh sách ảnh từ file `prompts/slide_definitions.py`. File này chứa 2 biến: `slide_definitions` (list) và `image_assets` (dict).
    *   Đọc dữ liệu tài chính từ file `data/financial_highlights.json`.
3.  **Cấu trúc code:** Code phải rõ ràng, có comment giải thích các bước chính.
4.  **Tạo biểu đồ:** Từ dữ liệu JSON đã đọc, tạo các biểu đồ theo định nghĩa trong `slide_definitions`.
5.  **Chèn ảnh:** Chèn các ảnh tĩnh có sẵn vào slide.
6.  **Tên file PPTX đầu ra:** `Bao_Cao_Tai_Chinh_Doanh_Nghiep.pptx`

Hãy tạo code Python hoàn chỉnh cho tôi dựa trên các yêu cầu trên. Code cần import `slide_definitions` và `image_assets` từ `prompts.slide_definitions`.
"""

    # --- API Configuration ---
    load_dotenv()
    AI_API_BASE = os.getenv("AI_API_BASE", "https://api.thucchien.ai/v1")
    AI_API_KEY = os.getenv("AI_API_KEY")

    if not AI_API_KEY:
        print("Error: AI_API_KEY not found. Please set it in a .env file.")
        return

    # --- API Execution ---
url = f"{AI_API_BASE}/chat/completions"
headers = {
  "Content-Type": "application/json",
  "Authorization": f"Bearer {AI_API_KEY}"
}
data = {
  "model": "gemini-2.5-flash",
  "messages": [
      {
          "role": "system",
                "content": "Bạn là một chuyên gia trong phân tích kinh doanh và lập trình Python. Nhiệm vụ của bạn là tạo ra mã Python sạch, hiệu quả và có thể chạy được để tự động hóa các báo cáo."
      },
      {
          "role": "user",
          "content": prompt
            }
  ]
}

    try:
        response = requests.post(url, headers=headers, data=json.dumps(data), timeout=180)
        response.raise_for_status()

  result = response.json()
        generated_code = result['choices'][0]['message']['content']

        if generated_code.startswith("```python"):
            generated_code = generated_code[9:]
        if generated_code.endswith("```"):
            generated_code = generated_code[:-3]

        output_path = "scripts/generated_report_script.py"
        with open(output_path, "w", encoding="utf-8") as f:
            f.write(generated_code)
        
        print(f"Successfully generated and saved the script to '{output_path}'")

    except requests.exceptions.RequestException as e:
        print(f"An error occurred during the API request: {e}")
    except (KeyError, IndexError) as e:
        print(f"Error parsing the API response: {e}")
        print("Full response:", response.text)

if __name__ == "__main__":
    generate_presentation_script()
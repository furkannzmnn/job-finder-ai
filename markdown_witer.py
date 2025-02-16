import json

import re

# jobs.json dosyasını oku
jobs_data =  None
with open("jobs.json", "r", encoding="utf-8") as file:
    jobs_data = json.load(file)


# Markdown içeriğini oluştur
markdown_content = """\
# Java Developer İş İlanları - Türkiye

Bu dosya, Türkiye konumundaki Java Developer iş ilanlarını içermektedir.

## 📌 İş İlanları

| 🔹 İş Unvanı | 🏢 Şirket | 📍 Konum | 🔗 İlan Linki |
|-------------|----------|---------|--------------|
"""

for job in jobs_data:
    markdown_content += f"| {job['job_title']} | {job['company_name']} | {job['location']} | [İlana Git]({job['url']}) |\n"

markdown_content += """\

---
📅 **Güncellenme Tarihi:** `YYYY-MM-DD`  
🔍 **Kaynak:** LinkedIn
"""

# Markdown dosyasına yaz
with open("README.md", "w", encoding="utf-8") as file:
    file.write(markdown_content)

print("✅ README.md dosyası başarıyla oluşturuldu!")

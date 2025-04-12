Pengujian otomasi skenario end to end pada portal https://saucesdemo.com menggunakan selenium python dengan Pytest framework dan pytest-html untuk export report dalam format html.

Struktur:
project/
├── conftest.py
├── tests/
│   └── test_endtoend_saucedemo.py
├── pages/
│   ├── cart.py
│   ├── checkout_complete.py
│   ├── checkout_info.py
│   ├── checkout_overview.py
│   ├── inventory.py
│   ├── locators.py
│   └── login.py 
└── reports/

- Install virtual environment:
python -m venv venv-tugas-akhir

- Aktivasi virtual environment:
.\venv-tugas-akhir\Scripts\activate
 
- Install beberapa dependency yang diperlukan:
pip install selenium
pip install pytest
pip install pytest-html
pip install webdriver-manager

- Run:
pytest -s
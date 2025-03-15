Pengujian otomasi skenario login pada portal https://opensource-demo.orangehrmlive.com menggunakan selenium python dengan Pytest framework dan pytest-html untuk export report dalam format .html.

Struktur:
project/ (i.e. tugas6)
├── tests/
│   ├── test_login.py  # File test menggunakan setup_browser yang telah di-set pada file conftest.py
├── conftest.py        # Fixture pytest global (nama file harus "conftest" agar fixture pytest bisa terbaca)
├── pytest.ini         # (opsional)

- Install virtual environment:
python -m venv venv-tugas6

- Aktivasi virtual environment:
.\venv-tugas6\Scripts\activate

- Install beberapa dependency yang diperlukan:
pip install selenium
pip install pytest
pip install pytest-html
pip install webdriver-manager

- Run:
pytest -s tests/ → run test tanpa mencetak report.html, namun output dari print() akan tercetak di terminal
pytest -s tests/ --html=report.html → run test dengan mencetak report.html
pytest -s tests/ --html=report.html --self-contained-html --log-cli-level=INFO → run test dengan mencetak report.html beserta log nya
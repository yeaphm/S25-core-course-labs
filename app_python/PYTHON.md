# Python Web Application

## Framework Choice: **Flask**

- **Justification**:
  - Lightweight and minimalistic for a simple time-display app.
  - No unnecessary overhead (unlike Django).
  - Easy to set up and deploy.

---

## Best Practices Applied

1. **Coding Standards**:
   - Followed **PEP8** guidelines (e.g., snake_case naming, line length ≤ 79 chars).  
   - Used `pytz` for accurate timezone handling (MSK time = UTC+3).  

2. **Code Quality**:
   - Isolated dependencies using a **virtual environment**.  

3. **Project Structure**:
   - Separated application code (`app.py`) from documentation.  
   - Added `.gitignore` to exclude virtual environments and cache files.  

---

## Manual Testing

- **Verification Steps**:  
  1. Run `python app.py` and access `http://localhost:5000` in a browser.  
  2. Confirm the displayed time matches [Moscow’s current time](https://time.is/Moscow).  

---

## How to Run

```bash
python app.py

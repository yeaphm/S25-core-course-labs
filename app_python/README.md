# Moscow Time Web Application

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)  
![Flask](https://img.shields.io/badge/Framework-Flask-green)  

## Overview

A simple web application that displays the current time in **Moscow (MSK)** using Python and Flask.  

---

## Features  

- Real-time Moscow time (UTC+3) using `pytz`.  
- PEP8-compliant code with clean structure.  

---

## Prerequisites  

- **Python 3.8 or later** must be installed on your system.  
  - Download Python: [https://www.python.org/downloads/](https://www.python.org/downloads/)  
  - Verify installation:  

    ```bash
    python --version  # Should return "Python 3.x.x"
    ```

---

## Local Installation  

1. **Clone the repository**:  

   ```bash
   git clone https://github.com/yeaphm/S25-core-course-labs.git
   cd app_python
   ```

2. **Set up a virtual environment**:  

   ```bash
   python -m venv venv
   source venv/bin/activate  # macOS/Linux
   venv\Scripts\activate     # Windows
   ```

3. **Install dependencies**:  

   ```bash
   pip install -r requirements.txt
   ```

4. **Run the application**:  

   ```bash
   python app.py
   ```

5. **Access the app**:  
   Open `http://localhost:5000` in your browser.  

---

## Dependencies  

- Flask (web framework)  
- pytz (timezone handling)  

See [`requirements.txt`](./requirements.txt) for details.

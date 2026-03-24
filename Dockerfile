FROM python:3.10-slim

WORKDIR /app

# Ensure these files are in your GitHub repo
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Render will override this port, but 5000 is a safe default
EXPOSE 5000

# Run using gunicorn. 'app' is your filename, 'myshit' is your Flask variable.
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "app:myshit"]
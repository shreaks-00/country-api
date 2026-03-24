# Use a lightweight Python image
FROM python:3.10-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements file and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of your application code
COPY . .

# Expose the port Flask will run on
EXPOSE 5000

# Run the app using gunicorn (better for production)
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "app:myshit"]
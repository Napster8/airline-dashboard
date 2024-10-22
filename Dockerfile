# Use the official Python image
FROM python:3.11-slim

# Set the working directory inside the container
WORKDIR /app

# requirements may not be there in location: /app so copy it to /app
COPY requirements.txt /app/ 

# Install required Python packages
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

# Copy Entire project into the container
COPY . /app

# Expose the port Taipy will run on
EXPOSE 5000

# Command to run the Taipy dashboard
CMD ["python", "app.py"]
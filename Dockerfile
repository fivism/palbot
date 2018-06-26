# Python type
FROM python:3.6

# Set cwd to /app
WORKDIR /app

# Copy current directory into container at /app
ADD . /app

# Install any needfed packages 
RUN pip install --trusted-host pypi.python.org -r requirements.txt

# Expose 80 to outside world outside the container
EXPOSE 80

# Run app.py when the container launches
CMD ["python3", "palbot.py"]



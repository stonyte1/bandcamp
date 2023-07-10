# Use an official Python runtime as the base image
FROM python:3.9

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file and install dependencies
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copy the project code into the container
COPY . .

# Expose the port that the Django development server will run on
EXPOSE 8000

# Set the command to run when the container starts
CMD ["python", "bandcamp/manage.py", "runserver", "0.0.0.0:8000"]

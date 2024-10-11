FROM python:3.10-slim

# Set the working directory 
WORKDIR /app

# Copy the plotting script into container
COPY plotting.py /app/

# Install packages
RUN pip install pandas matplotlib

# Run the plotting script
CMD ["python", "plotting.py"]

# Step 1: Start from an official Python image
FROM python:3.11-slim

# Step 2: Set where our code will live inside the container
WORKDIR /app

# Step 3: Copy the file that lists your dependencies
COPY requirements.txt .

# Step 4: Install Python packages
RUN pip install --no-cache-dir -r requirements.txt

# Step 5: Copy the rest of your project into the container
COPY . .

# Step 6: Collect static files (for admin, CSS, etc.)
RUN python manage.py collectstatic --noinput

# Step 7: Run database migrations
RUN python manage.py migrate

# Step 8: Tell Docker which port Django will use
EXPOSE 8000

# Step 9: Start Django with Gunicorn (a production web server)
CMD ["gunicorn", "visionvault.wsgi:application", "--bind", "0.0.0.0:8000"]

FROM python:3.10-slim
WORKDIR  /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
RUN mkdir -p reports
ENV PYTHONPATH=/app
CMD ["pytest", "-m", "sanity or regression or parametrize", "tests", "--html=reports/report.html", "--self-contained-html"]

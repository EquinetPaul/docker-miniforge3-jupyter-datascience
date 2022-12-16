FROM condaforge/miniforge3
ENTRYPOINT ["tail", "-f", "/dev/null"]
COPY requirements.txt /app/shared/
COPY generate_data.py /app/shared/
COPY compute.py /app/shared/
COPY pyLogs.py /app/shared/
WORKDIR /app/shared/
RUN pip install -r requirements.txt
RUN python generate_data.py
RUN python compute.py
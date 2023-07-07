# FROM python:3.8-alpine

# WORKDIR /src

# COPY . /src

# RUN python -m pip install --upgrade pip && \
#     pip install pipenv && pipenv install --dev --deploy

# EXPOSE 80

# CMD ["pipenv", "run", "start"]

# Build stage
FROM python:3.8-alpine as builder
WORKDIR /src
COPY . /src
RUN python -m pip install --upgrade pip && \
    pip install pipenv && pipenv install --dev --deploy

# Runtime stage
FROM python:3.8-alpine
WORKDIR /src
COPY --from=builder /src .
EXPOSE 80
CMD ["pipenv", "run", "start"]



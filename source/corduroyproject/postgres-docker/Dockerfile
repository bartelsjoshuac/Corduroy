# Use the official PostgreSQL image as the base
FROM postgres:latest

# Set environment variables for Postgres
ENV POSTGRES_USER=postgres
ENV POSTGRES_PASSWORD=password
ENV POSTGRES_DB=corduroydb

# Copy any custom initialization SQL or scripts
# Not doing this anymore
#COPY ./init.sql /docker-entrypoint-initdb.d/

# Expose the PostgreSQL port
EXPOSE 5432
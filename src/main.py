import psycopg2
conn = psycopg2.connect(
    host="db-postgres-nhl-stats-do-user-2581384-0.b.db.ondigitalocean.com",
    database="nhlstats",
    user="readonly",
    password="n1rzp9p16pr9s905",
    port="25060",
    sslmode="require")

print(conn)

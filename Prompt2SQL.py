import mysql.connector
import ollama
import datetime
import os
import sys

# Configuration
DB_CONFIG = {
    "host": "localhost",
    "user": "root",
    "password": "amit.gujar",
    "database": "NBFC_Customers"
}
LOG_FILE = "query_log.txt"
MODEL_NAME = "mistral:latest"  # Not shown in logs

# Table schema to be used by the model
TABLE_SCHEMA = (
    "NBFC_Customers(id INT PRIMARY KEY, full_name VARCHAR(100), city VARCHAR(50), "
    "loan_type VARCHAR(20), loan_amount INT, interest_rate DECIMAL(5,2), "
    "loan_term INT, start_date DATE, status VARCHAR(20))"
)

def log_step(message: str):
    timestamp = datetime.datetime.now().strftime("[%Y-%m-%d %H:%M:%S]")
    log_message = f"{timestamp} {message}\n"
    print(log_message, end='')
    try:
        with open(os.path.abspath(LOG_FILE), "a", encoding="utf-8") as f:
            f.write(log_message)
    except Exception as e:
        print(f"Logging error: {e}", file=sys.stderr)

def main():
    log_step("Connecting to MySQL database...")
    try:
        conn = mysql.connector.connect(**DB_CONFIG)
        cursor = conn.cursor()
        log_step("Connected to MySQL database successfully.")
    except mysql.connector.Error as err:
        log_step(f"Database connection failed: {err}")
        return

    nl_query = input("Ask your question: ")
    log_step(f"Received NL query: {nl_query}")

    prompt = (
        f"Using this table schema:\n{TABLE_SCHEMA}\n"
        f"Convert the following natural language question into a valid MySQL query:\n{nl_query}\n"
        "Only return the SQL query without explanation."
    )

    log_step("Converting NL to SQL...")
    try:
        response = ollama.chat(
            model=MODEL_NAME,
            messages=[{"role": "user", "content": prompt}]
        )
        sql_query = response['message']['content'].strip()

        if sql_query.startswith("```sql") or sql_query.startswith("```"):
            sql_query = sql_query.replace("```sql", "").replace("```", "").strip()

        log_step("Generated SQL query:")
        print("\n\033[1m" + sql_query + "\033[0m\n")

    except Exception as e:
        log_step(f"Failed to convert NL to SQL: {e}")
        cursor.close()
        conn.close()
        return

    try:
        cursor.execute(sql_query)
        results = cursor.fetchall()
        columns = cursor.column_names

        print("Results:\n")
        print("\t".join(columns))
        for row in results:
            print("\t".join(str(col) for col in row))

        log_step("SQL query executed successfully.")

    except mysql.connector.Error as err:
        log_step(f"SQL execution error: {err}")

    cursor.close()
    conn.close()
    log_step("Closed MySQL connection.")

if __name__ == "__main__":
    main()
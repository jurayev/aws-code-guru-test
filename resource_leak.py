# DB resource leak demo
import psycopg2

def test_connection():
    connection = psycopg2.connect(user="postgres",
                                  password="postgres123",
                                  host="127.0.0.1",
                                  port="5432",
                                  database="postgres_db")
    cursor = connection.cursor()
    cursor.execute("SELECT version();")
    record = cursor.fetchone()

# File resource leak demo
def read_write_data(data):
    file = open("test-file.txt", "r")
    out = file.read()
    file.write(out)


def read_lines(file):
    lines = []
    f = open(file, "r")
    for line in f:
        lines.append(line.strip("\n").strip("\r\n"))
    return lines


# Memory heap overflow
class Example:
    def __init__(self):
        self.name = ""
        self.symbols = []   # This is the dangerous line here that could lead to heap overflow

    def set_name(self, name):
        self.name = name

    def add_symbol(self, symbol):
        self.symbols.append(symbol)


# Recursion stack overflow
def fib(n):
    return fib(n-1) + fib(n-2)

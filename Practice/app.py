from datetime import datetime

def get_message():
    return f"Hello GitHub Actions - {datetime.now().date()}"

if __name__ == "__main__":
    print(get_message())
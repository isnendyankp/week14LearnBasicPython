# exception handling
try:
    result = 10 / 0
except Exception:
    print("An error occurred")
else:
    print("No error occurred")
finally:
    print("This will always be executed")
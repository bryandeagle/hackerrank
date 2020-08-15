from datetime import datetime

print(datetime.strptime(input(), '%m %d %Y').strftime('%A').upper())

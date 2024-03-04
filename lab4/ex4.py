from datetime import datetime
date1 = datetime(2024, 3, 1, 12, 0, 0)
date2 = datetime(2024, 3, 1, 12, 0, 30)
difference_in_seconds = (date2 - date1).total_seconds()
print("Difference between the two dates in seconds:", difference_in_seconds)

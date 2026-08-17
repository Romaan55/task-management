from datetime import datetime, timedelta  # Date ke liye

def get_completed(appointments):  # Function
    last_30 = datetime.now() - timedelta(days=30)  # 30 din pehle
    count = {}  # Provider count

    for a in appointments:  # Har appointment
        date = datetime.strptime(a["date"], "%Y-%m-%d")  # Date convert

        if a["status"] == "completed" and date >= last_30: 
            p = a["provider"]  # Provider name
            count[p] = count.get(p, 0) + 1  # Count +1

    result = [(p, n) for p, n in count.items() if n > 5]  #>5 providers
    return sorted(result, key=lambda x: x[1], reverse=True)  # High to low

appointments = [
    {"provider": "Ali", "status": "completed", "date": "2026-08-15"},
    {"provider": "Ali", "status": "completed", "date": "2026-08-14"},
    {"provider": "Sara", "status": "pending", "date": "2026-08-13"},
]

print(get_completed(appointments))  # Result
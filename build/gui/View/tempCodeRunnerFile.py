te(f"Select TicketID from Purchase")
y = cursor.fetchall()
for i in range(len(y)):
    print(i)
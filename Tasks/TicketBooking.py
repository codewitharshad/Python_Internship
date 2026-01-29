def book_movie_ticket(movie_name, available_seats, tickets_requested, price_per_ticket):
    
    if not movie_name.strip():
        return "Movie name cannot be empty."

    try:
        tickets_requested = int(tickets_requested)
    except ValueError:
        return "Number of tickets must be a valid number."
    
    if tickets_requested <= 0 or tickets_requested > 6:
        return "You must atleast book 1 ticket and at max 6 tickets."
    if tickets_requested > available_seats:
        return f"Only {available_seats} seats are available."
    
    total_cost = tickets_requested * price_per_ticket

    return f"Booking successful! 🎉\nMovie: {movie_name}\nTickets: {tickets_requested}\nTotal Cost: ₹{total_cost}"


movie = input("Enter the Movie name: ")
available = 50
tickets = input("Enter mumber of tickets: ")
price = 250

print(book_movie_ticket(movie, available, tickets, price))
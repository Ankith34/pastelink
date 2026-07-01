# PasteLink

**PasteLink** is a lightweight, Pastebin-inspired web application built from scratch as a **learning project** — the goal is to deeply understand how web applications work under the hood, not to produce a polished resume piece.

The app lets a user paste text, get back a unique shareable link, and retrieve the stored content through that link. Simple on the surface, but building it correctly touches almost every core backend concept: client-server communication, routing, data storage, and (eventually) database design, caching, and auth.

## Why This Project Exists

Most tutorials hand you a finished app to copy. PasteLink is being built the opposite way: incrementally, one concept at a time, with an emphasis on understanding *why* each piece works the way it does — not just getting it to run.

## Current Architecture

- **Frontend:** Plain HTML
- **Backend:** Flask
- **Data flow:** Form-based text submission via HTTP POST
- **Routing:** Dynamic route handling in Flask
- **ID generation:** Unique paste ID generated per submission
- **Storage:** In-memory Python dictionary (temporary — no persistence yet)
- **Retrieval:** Pastes fetched and rendered via dynamic URL

## Current Workflow

1. User visits the homepage.
2. User enters text into a textarea.
3. Frontend submits the content to the Flask backend via POST.
4. Backend generates a unique identifier for the paste.
5. Text is stored in memory, keyed by that identifier.
6. A unique URL is returned, pointing to the paste.
7. Visiting the URL retrieves and displays the stored content.

## Learning Objectives

This project is deliberately built in stages to build real understanding of:

- Client-server architecture
- HTTP requests and responses
- Routing and endpoint design
- Form handling
- Dynamic URL parameters
- Data structures for storage
- Backend application design
- Database integration *(planned)*
- Authentication and authorization *(planned)*
- Caching and scalability concepts *(planned)*
- 
🚧 Actively under development as part of a structured, from-scratch learning path in backend development and system design fundamentals.

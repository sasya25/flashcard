# Color Flashcard Backend

This is a simple REST API for managing color flashcards. It allows you to create, retrieve, update, and delete color flashcards. You can use this API as a backend for a color flashcard application or any other project that requires color-related information.

## Table of Contents

- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
  - [Endpoints](#endpoints)

## Getting Started

These instructions will help you set up and run the project on your local machine.

### Prerequisites

- Python 3.x
- Flask

### Installation

1. Clone the repository to your local machine:

   ```bash
   git clone https://github.com/your-username/color-flashcard-backend.git
   
2. Change to the project directory:
   ```bash
   cd flashcard
3. Run the application:
   ```bash
    ./bootstrap.sh
   
The API will start and be accessible at http://localhost:5000.

### Usage
### Endpoints
1. GET /flashcards: Get a list of all color flashcards.
2. POST /flashcards: Create a new color flashcard.

   Request body example:
   
    json
    {
        "color": "Yellow",
        "description": "The color of sunshine and happiness."
    }
4. GET /flashcards/<flashcard_id>: Get a specific color flashcard by its ID.
5. PUT /flashcards/<flashcard_id>: Update a color flashcard by its ID.
   
    Request body example (partial update):
   
    json
    {
        "description": "The color of warmth and optimism."
    }
7. DELETE /flashcards/<flashcard_id>: Delete a color flashcard by its ID.




# thato-builds

A collection of Python projects showcasing my journey as a software developer.  
These projects span game development, data visualization, backend APIs, and database integration — each one tackling unique problems and demonstrating practical solutions.

This repository reflects my approach to **hands-on learning, problem-solving, and building structured applications**.  
Many projects are evolving, and there’s more to come — including full-stack applications, new challenges, and increasingly complex problems to solve.

---

## Projects

### 1. Alien Invasion Game
- Based on the textbook *Python Crash Course* by Eric Matthes.  
- A 2D arcade-style game where the player controls a ship to shoot down alien fleets.  
- Demonstrates use of **Pygame**, object-oriented programming, and event-driven logic.  
- Features include player movement, bullet firing, alien fleet generation, and collision detection.

---

### 2. Data Visualization Activities
- A collection of scripts and notebooks exploring Python’s data visualization libraries.  
- Demonstrates use of **Matplotlib**, **Plotly**, and **Pygal** for charts and interactive graphs.  
- Includes activities such as:
  - Line and scatter plots
  - Histograms
  - Random walk simulations
  - Dice roll probability visualizations

---

### 3. Task & Workflow Management API
- A RESTful API built with **Flask** and **SQLite** for managing tasks and workflows.  
- Features:
  - CRUD operations for tasks
  - Role-based access (Admin vs Worker)
  - Task assignment and status tracking (`Completed`, `Incomplete`, `In Progress`)
- Integrated **SQLAlchemy models** for persistent storage.  
- Endpoints include task creation, editing, deletion, assignment, and status updates.

---

### 4. “I Can’t Be The Only One” API (ICBTOO) *(In Development)*
- A backend API designed to allow users to anonymously share relatable thoughts and experiences.  
- Focused on backend architecture and database integration.  
- **Current progress:**
  - Flask project setup
  - Successful connection to :contentReference[oaicite:0]{index=0} (MSSQL)
  - Configured `pyodbc` driver
  - Database connectivity testing
- **Next steps:**
  - Design SQLAlchemy models
  - Implement user registration & authentication
  - Create post creation and retrieval endpoints
  - Add validation and error handling
  - Implement role-based access control
- **Future vision:**
  - Expand into a full-stack application
  - Integrate a frontend (e.g., React)
  - Implement JWT-based authentication
  - Add commenting and reaction features
  - Deploy to a cloud platform

> ⚠️ Note: This is the only project in this repository currently using Microsoft SQL Server.

---

## Tech Stack

- **Languages:** Python  
- **Libraries & Frameworks:** Pygame, Flask, SQLAlchemy, Matplotlib, Plotly, Pygal  
- **Databases:**  
  - SQLite (Task & Workflow API)  
  - Microsoft SQL Server (ICBTOO API)  
- **Database Driver (ICBTOO):** pyodbc  

---

## How to Run

Clone the repository and navigate to the project folder you want to run:

```bash
git clone https://github.com/thatomoreti/Projects.git
cd Projects/<project-folder>

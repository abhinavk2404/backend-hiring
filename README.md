## What This Is About

This project implements a **dynamic asynchronous task execution system** designed for a **multi-tenant environment** where resources are shared across different customers. The goal is to efficiently manage and execute tasks (referred to as **jobs**) submitted by customers based on their type and the nature of the job.

### Key Concepts

- **Multi-Tenant Architecture**:  
  Customers (stored in the `Site` table) share infrastructure, so tasks need to be handled with resource prioritization in mind.

- **Job Classification**:  
  Jobs are categorized into **five types** based on their execution time (in seconds), allowing the system to prioritize or balance loads accordingly.

- **Customer Classification**:  
  Customers are grouped into **three types** based on the volume of data they generate. This impacts how resource-intensive their jobs may be.

- **Task Execution**:  
  Workers are designed to pick up and execute jobs by considering both the **customer type** and **job type**.  
  Each worker executes **only one job at a time**, ensuring simplicity and predictable behavior.

### System Features

- 📦 Data structures to store and manage job types and customer types  
- 📡 RESTful APIs to interact with the system (e.g., submit tasks, check status)  
- ⚙️ Background workers that continuously fetch and execute jobs based on defined rules and priorities  
- 🔄 Flexible integration with databases, message queues, and libraries to handle queuing and execution


# Setup:

```
install python3.5, pip3 and venv
$ python3.5 -m venv almabase-venv
$ source almabase-venv/bin/activate
$ pip install --upgrade pip --trusted-host pypi.python.org
$ pip3 install -r requirements.txt
```

---

This project simulates a real-world asynchronous job processing system as seen in scalable SaaS platforms—prioritizing **fairness**, **efficiency**, and **maintainability**.

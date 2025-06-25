# 🗂️ TrackTask System

**TrackTask** is an intelligent command-line Task Management System designed to simplify and enhance project coordination between **Project Managers** and **Team Members**. Built with a focus on clarity, collaboration, and ease of use, the system incorporates AI-generated task suggestions using the **OpenAI API**, making it more than just a manual task tracker.

## 🚀 Overview

TrackTask is a versatile online tool designed for seamless project and task management. It serves two key user roles:

- **Project Managers**: Plan, assign, and monitor tasks across the team.
- **Team Members**: Stay updated with assigned tasks, provide progress updates, and communicate blockers.

By integrating prompt-based task generation using the OpenAI API, TrackTask helps streamline project setup and keeps management intelligent and proactive.

## 👩‍💼 Project Manager Features

As a Project Manager, you can:

- ➕ **Add, edit, and delete tasks** to ensure projects remain up-to-date and relevant.
- 👀 **View all tasks and their statuses** across all team members for comprehensive oversight.
- 🤖 **Generate tasks using AI** when creating a new project to accelerate planning and ideation.

## 👷 Team Member Features

As a Team Member, you can:

- 📋 **View tasks assigned** to you for effective workload management.
- ✅ **Update task statuses** to reflect progress and stay aligned with deadlines.
- 💬 **Add or edit comments** to keep the Project Manager informed of updates or blockers.

## 🧠 Built with:
- Python
- OpenAI API (Prompt-based task suggestions)
- Command-line interface (CLI)

---

## 📘 User Guide

### 🆕 New Project Manager

- **Start Setup**: Type `new` to create a new project and auto-generate tasks via AI.
- Follow on-screen instructions to enter project details.

### 👩‍💼 Project Manager Panel

- **Login**: Type `Project Manager` to log in as a manager.
- **Add a Task**: Type `add`, then provide:
  - Task Title  
  - Responsible Person  
  - Start Date (`YYYY-MM-DD`)  
  - End Date (`YYYY-MM-DD`)  
  - Task ID
- **Delete a Task**: Type `delete` and enter the Task ID.
- **Edit a Task**: Type `edit`, provide Task ID, and modify:
  - Task Title  
  - Responsible Person  
  - Start Date / End Date  
  - Status
- **View All Tasks**: Type `info` to see the full task list.
- **View Member's Tasks**: Type `member tasks` and enter the member's name.
- **Exit**: Type `exit` to leave the manager panel.

### 🧑‍💻 Team Member Panel

- **Login**: Type `member` to access your assigned tasks.
- **Update Task Status**: Type `edit status`, then enter Task ID and new status.
- **Add/Edit Comment**: Type `comment`, then enter Task ID and your message.
- **View Your Tasks**: Type `info` to list your assigned tasks.

---

## 📌 Note

This system currently runs on the command line and is designed as a prototype.


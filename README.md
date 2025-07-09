# 🎶 Orininu Streaming Service Database

This project focuses on creating, managing, and migrating the database for the Orininu Streaming Service. Starting with **PostgreSQL**, the data model was designed and structured, synthetic data was generated using **Python**, and later transitioned the system to **MongoDB Atlas** for better flexibility and scalability.

The process also involved automating data synchronization using **Task Scheduler** to ensure PostgreSQL data remained up-to-date in MongoDB.

---

## 📌 Project Overview

This project establishes the Orininu Streaming Service database from scratch, covering:

✅ PostgreSQL database creation  
✅ Data generation using Python  
✅ Full migration to MongoDB Atlas  

---

## ⚙️ Technologies Used

 ⏺ PostgreSQL: Relational Database Setup  
 ⏺ SQL Schema Design: Defining Tables & Relationships  
 ⏺ Python (`pandas`, `faker`): Synthetic Data Generation  
 ⏺ MongoDB Atlas: Database Migration  
 ⏺ MongoDB Shell (`mongosh`): Database Management  
 ⏺ MongoDB Database Tools (`mongoimport`): Importing Data into MongoDB  
 ⏺ Windows Task Scheduler: Scheduling and Importing Data into MongoDB  

---

## 🔄 Full Database Setup Workflow

### 1. Generate Synthetic Data Using Python

- Used `faker` and `pandas` to create realistic user profiles, songs, artists, albums, etc.  
- Stored and exported generated data in a CSV format  

### 2. Design & Create PostgreSQL Database

- Defined schema with `DDL.sql`  
- Created tables for:
  - `users`
  - `artists`
  - `albums`
  - `songs`
  - `user_interaction`
  - `playlists`
  - `playlist_songs`  
- Established foreign key relationships  

### 3. Populate PostgreSQL with Generated Data

- Imported CSV data  
- Ran queries with `DQL.sql` to validate relationships  

### 4. Transform and Migrate Data to MongoDB

- Converted CSV files to JSON format for MongoDB compatibility  
- Imported JSON files into MongoDB Atlas  

### 5. Implement Scheduled Data Synchronization

- Exported new PostgreSQL data as CSV  
- Converted it to JSON automatically  
- Imported it into MongoDB at a set interval of 5 minutes using Windows Task Scheduler  

---

## 📄 Results & Final Verification

✅ PostgreSQL database successfully created  
✅ Synthetic data generated & formatted for migration  
✅ MongoDB collections accurately imported  
✅ MongoDB queries returning expected results  
✅ GitHub repository ready for submission  

---

## 📝 Notes

 ⏺ Python (`faker`) was used to generate realistic streaming service data  
 ⏺ CSV files were formatted before conversion to JSON  
 ⏺ IP Whitelisting was essential for MongoDB Atlas access  

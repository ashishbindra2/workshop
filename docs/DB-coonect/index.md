# Overview

## What is SQL?

SQL, which stands for Structured Query Language, is a domain-specific programming language

- That is commonly used for tasks such as inserting, updating, querying, and deleting data within a database.
- QL is also used to create and modify database schemas (e.g., data formatting rules, table/index structure ) as well as define database access and administration parameters.

## What is structured data?

Structured data is data that is organized in a consistent, predefined format and often consists of alphanumeric characters. Examples include financial transactions, inventory records, or customer lists which are often stored in SQL databases (e.g., relational databases).

## Relational databases

Relational databases, or relational database management systems (RDBMSs), store data within rows and columns which are used to form tables.
A relationship between the two tables (or more) can be created using a foreign key. These foreign keys (e.g., unique identifiers) maintain predefined relationships that exist between the tables.
Examples of SQL databases
There are a variety of different SQL database examples, including:

Oracle: Oracle Database is a relational database management system (RDBMS) developed and marketed by Oracle Corporation and is one of the most commonly used enterprise database systems in the world.
MySQL: MySQL is a commonly used, open-source, relational database management system used for creating and administering databases. Developed and distributed by Oracle Corporation, MySQL is known for ease of use, extensive community support, and reliability.
MSSQL: MSSQL, which stands for Microsoft SQL Server, is a relational database management system developed by Microsoft. This database platform is commonly used in large enterprise environments to support high-volume transaction processing, business intelligence, and analytics applications.
SQLite: Unlike other examples in this list, SQLite is actually a software library that provides an RDBMS. Unlike the other RDBMSs in this list, SQLite is serverless and self-contained with zero configuration. This is because it is embedded within the application using SQLite and, as a result, doesn't need a separate server.

Relational databases, such as MySQL and PostgreSQL, have been the default for decades. They offer strong consistency, well-understood query languages, and battle-tested reliability. However, as systems scale and use cases diversify, traditional SQL starts to exhibit problems.
That’s where NoSQL enters the picture with a flexible schema design, horizontal scalability, and models tailored to specific access patterns. The promise is to scale fast and iterate freely. However, there are trade-offs in consistency, structure, and operations.

## Types of NoSQL Databases

What is unstructured data?
Unstructured data is data that doesn't have a predefined data model or consistent organization. In addition, unstructured data, such as social media posts, can update and change rapidly while structured data, such as bank transactions, have a much lower rate of change. Examples of unstructured data include pictures, audio files, videos, and maps.

What is a NoSQL database?
NoSQL databases are databases that utilize a flexible schema that accommodates unstructured data and semi-structured data while also utilizing a non-tabular data storage method.

The use of a flexible schema enables NoSQL databases to ingest unstructured data in its native format (e.g., .txt, .JPG, MP3), which is not possible with SQL databases due to the requirement that all data align to a predefined format. Further, when NoSQL databases store data, flexible data models are employed so that unstructured data files can have different data structures and still be stored within the same collection.

NoSQL databases handle large volumes of unstructured and semi-structured data, offering the scalability and flexibility today’s diverse workloads demand.

## Types of NoSQL Database

NoSQL databases can be classified into four main types, based on their data storage and retrieval methods:

1. Document-based databases
2. Key-value stores
3. Column-oriented databases
4. Graph-based databases

---

### 1. Document-Based Database

- The document-based database is a nonrelational database.
- Instead of storing the data in rows and columns (tables), it uses the documents to store the data in the database.
- A document database stores data in JSON, BSON
- Collections are the group of documents that store documents that have similar contents.
- document databases have a flexible schema.

Key features of document database:

- Flexible schema: Documents in the database has a flexible schema. It means the documents in the database need not be the same schema.
- Faster creation and maintenance: the creation of documents is easy and minimal maintenance is required once we create the document.
- Open formats: To build a document we use XML, JSON, and others.

Popular Document Databases & Use Cases

- MongoDB : Content management, product catalogs, user profiles
- CouchDB       : Offline applications, mobile synchronization
- Firebase Firestore : Real-time apps, chat applications

### 2. Key-Value Stores

- Every data element in the database is stored in key-value pairs.
- The data can be retrieved by using a unique key allotted to each element in the database.
- The values can be simple data types like strings, numbers or complex objects
- key-value store is like a relational database with only two columns which is the key and the value.

Key features of the key-value store:
Simplicity: Data retrieval is extremely fast due to direct key access.
Scalability: Designed for horizontal scaling and distributed storage.
Speed: Ideal for caching and real-time applications.

Popular Key-Value Databases & Use Cases

- Redis : Caching, real-time leaderboards, session storage
- Memcached : High-speed in-memory caching

- Amazon DynamoDB: Cloud-based scalable applications

### 3. Column Oriented Databases

- stores the data in columns instead of rows.

- we want to run analytics on a small number of columns, we can read those columns directly without consuming memory with the unwanted data.

- Columnar databases are designed to read data more efficiently and retrieve the data with greater speed.
- A columnar database is used to store a large amount of data.

Key features of Columnar Oriented Database
High Scalability: Supports distributed data processing.
Faster Query Performance: Best for analytical queries.

Apache Cassandra : Real-time analytics, IoT applications
HBase :Hadoop ecosystem, distributed storage
Google Bigtable : Large-scale machine learning, time-series data

### 4. Graph-Based Databases

- It stores the data in the form of nodes in the database.
- The connections between the nodes are called links or relationships, making them ideal for complex relationship-based queries.
- Data is represented as nodes (objects) and edges (connections).
- Fast graph traversal algorithms help retrieve relationships quickly.
- Used in scenarios where relationships are as important as the data itself.

Key features of Graph Database

Relationship-Centric Storage: Perfect for social networks, fraud detection, recommendation engines.
Real-Time Query Processing: Queries return results almost instantly.
Schema Flexibility: Easily adapts to evolving relationship structures

Popular Graph Databases & Use Cases
Neo4j : Fraud detection, social networks
Amazon Neptune : Knowledge graphs, AI recommendations
ArangoDB : Multi-model database, cybersecurity

## In-Memory Database

An in-memory database is a purpose-built database that relies primarily on internal memory for data storage

- It enables minimal response times by eliminating the need to access standard disk drives (SSDs).
- In-memory databases are ideal for applications that require microsecond response times or have large spikes in traffic, such as gaming leaderboards, session stores, and real-time data analytics.
- The terms main memory database (MMDB), in-memory database system (IMDS), and real-time database system (RTDB) also refer to in-memory databases.

### What are the advantages of in-memory databases

Low latency, providing real time responses

- Latency is the lag between the request to access data and the application's response
- In-memory databases deliver low latency regardless of scale.
- They deliver microsecond read latency, single-digit millisecond write latency, and high throughput

Example:

- Imagine a toll booth:
- Latency is how long it takes for one car to pass.
- Throughput is how many cars can pass per minute.
- Bandwidth → how wide the road is (how many lanes are available for cars to pass at once)
So, in databases:

- Low latency means each query or transaction is processed quickly.
- High throughput means the database can process many queries at the same time efficiently.
- High bandwidth means the system can transfer or handle large amounts of data simultaneously.

As a result, in-memory storage allows enterprises to make data-based decisions in real-time.

For example, in-memory computing of sensor data from self-driving vehicles can give the desired split-second response time for emergency braking.

### High throughput

- In-memory databases are known for their high throughput.
- Throughput refers to the number of read (read throughput) or write (write throughput) operations over a given period of time.
- Examples include bytes/minute or transactions per second.

### High scalability

You can scale your in-memory database to meet fluctuating application demands. Both write and read scaling is possible without adversely impacting performance. The database stays online and supports read-and-write operations during resizing.

### Caching

Caching allows you to reuse previously retrieved or computed data efficiently. In-memory data storage works well for faster access to cached data. Caching trades off durability for response time.

Response time is faster because data is retrieved from memory, but caching doesn't protect against the loss of data in memory. This is why caching is often used in combination with a disk-based durable database.
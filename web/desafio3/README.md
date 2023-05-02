# Desafio 3 : Database implementation using MySQL

In this "Desafio" you have to create a database for the 'contatos' page in the site.

## Quickstart

---

>Requirements:

- Python
- MySQL80
  - Python Connector

[//]: # (breaklist)

### Creating the database

After installing MySQL and starting the MySQL console type:

    create database unes;
    use unes;

    create table contatos(
        email varchar(60) not null unique,
        assunto varchar(60) not null,
        descricao varchar(255)
    );

Then go in app.py and change PASSWORD_HERE to your local  mySQL password :

    app.config["MYSQL_PASSWORD"] = "PASSWORD_HERE" 

Within the repository directory put in the CMD console:

    pip install -r requirements.txt

    flask run

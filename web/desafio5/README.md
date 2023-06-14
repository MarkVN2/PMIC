# Desafio 5 : Responsivity

In this "Desafio" you have to add responsivity to the site, making it usable in cellphones and other devices of smaller dimensions.

## Quickstart

---

>Requirements:

- Python
- MySQL80
  - Python Connector
  
[//]: # (breaklist)

### Creating the database and running the site

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

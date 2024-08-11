# Multi DB Script Generator for SSMS

This python script will generate an SQL script that will run in SQL Server Management Studio to execute multiple script files in multiple DBs.

# How to use it

You need to have python installed with PyYAML

[Download script with config file.](https://raw.githubusercontent.com/AnthonyStiles/MultiDBScriptGenerator/master/GenerateMultiDBScript.zip)

Ensure the config file is in the same directory as the script.

Change the contents of the config file based on your requirements.

Run the script.

It should generate a file in the same directory as the script.

Open the script in SQL Server Management Studio and run using SQLCMD Mode.
create table data (
PassengerId int,
Survived int,
Pclass int,
Name varchar(100),
Sex varchar(100),
Age int,
SibSp int,
Parch int,
Ticket varchar(100),
Fare float,
Cabin varchar(100),
Embarked varchar(100)
);

separator ","
.import train.csv data;

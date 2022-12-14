/* PFFAFFMANN EXAMPLE
create table movies (
      id         INT NOT NULL UNIQUE,
      title      CHAR NOT NULL,
      year       INT NOT NULL,
      length     INT NOT NULL,
      studioId    INT NOT NULL,
      cost       INT NOT NULL         );
*/

/* Internet Example
CREATE TABLE Orders (
    OrderID int NOT NULL,
    OrderNumber int NOT NULL,
    PersonID int,
    PRIMARY KEY (OrderID),
    FOREIGN KEY (PersonID) REFERENCES Persons(PersonID)
);
*/


create table student (
    lnumber             INT NOT NULL UNIQUE,
    hallid              INT NOT NULL,
    firstname           CHAR NOT NULL,
    lastname            CHAR NOT NULL,
    middlename          CHAR,
    classyear           INT NOT NULL,
    degree              CHAR NOT NULL,
    major               CHAR NOT NULL,
    email               CHAR NOT NULL,
    phonenumber         INT NOT NULL,
    adress              INT NOT NULL,
    dob                 DATE NOT NULL,
    pobox               INT NOT NULL,
    emergencycontact    INT NOT NULL,
    mealplan            INT NOT NULL,
    notes               CHAR,
    PRIMARY KEY (lnumber),
    FOREIGN KEY (hallid) REFERENCES residencehall(hallid)
);


create table residencehall (
    hallid              INT NOT NULL UNIQUE,
    hallname            CHAR NOT NULL,
    location            CHAR NOT NULL,
    floors              INT NOT NULL,
    tier                INT NOT NULL,
    capacity            INT NOT NULL,
    cost                INT NOT NULL,
    oncampus            BOOLEAN NOT NULL,
    PRIMARY KEY (hallid)
);

create table class (
    classnumber         INT NOT NULL UNIQUE,
    department          CHAR NOT NULL,
    name                CHAR NOT NULL,
    description         CHAR,
    PRIMARY KEY (classnumber)
);

create table classinstance (
    
);

create table outcome (

);

create table prerequisite (

);

create table staff (

);

create table jobtype (

);


/*Links student with their respective residence hall*/
create table studenttoresidencehall (

);


/*Links student to their respective class instance*/
create table studenttoclassinstance (

);

create table librarybooks (

);
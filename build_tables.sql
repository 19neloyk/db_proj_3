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
    crn                 INT NOT NULL UNIQUE,
    classnumber         INT NOT NULL,
    professorid         INT NOT NULL,
    semester            CHAR NOT NULL,
    section             INT NOT NULL,
    location            CHAR NOT NULL,
    enrollmentlimit     INT NOT NULL,
    enrollmentlimit     INT NOT NULL,
    PRIMARY KEY (classinstance),
    FOREIGN KEY (classnumber) REFERENCES class(classnumber),
    FOREIGN KEY (professorid) REFERENCES staff(staffid)
);

create table outcome (
    classnumber         INT NOT NULL,
    outcomenumber       INT NOT NULL,
    FOREIGN KEY (classnumber) REFERENCES class(classnumber)
);

create table prerequisite (
    classnumber         INT NOT NULL,
    prerequisite        INT NOT NULL,
    FOREIGN KEY (classnumber) REFERENCES class(classnumber),
    FOREIGN KEY (prerequisite) REFERENCES class(classnumber),
);

create table staff (
    staffid             INT NOT NULL UNIQUE,
    jobid               INT NOT NULL,
    firstname           CHAR NOT NULL,
    middlename          CHAR,
    lastname            CHAR NOT NULL,
    yearsworked         INT NOT NULL,
    tenure              CHAR NOT NULL,
    PRIMARY KEY (staffid),
    FOREIGN KEY (jobid) REFERENCES job(jobid),
);

create table jobtype (
    jobid               INT NOT NULL UNIQUE,
    jobname             CHAR NOT NULL UNIQUE,
    salary              INT NOT NULL,
    hours               INT NOT NULL,
    location            CHAR NOT NULL,
    PRIMARY KEY (jobid)
);

/*Links student to their respective class instance*/
create table studenttoclassinstance (
    crn                 INT NOT NULL,
    lnumber             INT NOT NULL,
    status              INT NOT NULL, /*Number representing if withdrawn, in-progress, or if taken already*/
    grade               CHAR /*Can be null if still in progress or withdrawn*/,
    FOREIGN KEY (crn),
    FOREIGN KEY (lnumber)
);

create table librarybooks (
    bookid              INT NOT NULL UNIQUE,
    bookname            CHAR NOT NULL,
    author              CHAR NOT NULL,
    PRIMARY KEY (bookid)
);
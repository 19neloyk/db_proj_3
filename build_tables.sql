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

create table residencehall (
    hallid              INT NOT NULL UNIQUE,
    hallname            CHAR NOT NULL,
    location            CHAR NOT NULL,
    floors              INT NOT NULL,
    tier                INT NOT NULL,
    capacity            INT NOT NULL,
    oncampus            BOOLEAN NOT NULL,
    PRIMARY KEY (hallid)
);

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

create table course (
    courseid             INT NOT NULL UNIQUE, /* Arbitrary unique identifier */
    coursenumber         INT NOT NULL,   /* This represents the 320 in "CS320" */       
    department          CHAR NOT NULL,  /* This represents the "CS" in "CS320" */
    name                CHAR NOT NULL,
    description         CHAR,
    PRIMARY KEY (coursenumber)
);

create table jobtype (
    jobid               INT NOT NULL UNIQUE,
    jobname             CHAR NOT NULL UNIQUE,
    hours               INT NOT NULL,
    PRIMARY KEY (jobid)
);

create table staff (
    staffid             INT NOT NULL UNIQUE,
    jobid               INT NOT NULL,
    firstname           CHAR NOT NULL,
    middlename          CHAR,
    lastname            CHAR NOT NULL,
    yearsworked         INT NOT NULL,
    tenure              BOOLEAN NOT NULL,
    location            CHAR NOT NULL,
    salary              INT NOT NULL,
    PRIMARY KEY (staffid),
    FOREIGN KEY (jobid) REFERENCES jobtype(jobid)
);

create table classinstance (
    crn                 INT NOT NULL UNIQUE,
    coursenumber             INT NOT NULL,
    professorid         INT NOT NULL,
    section             INT NOT NULL,
    semester            CHAR NOT NULL, /* Either Fall, Winter, Spring, or Summer (I know Winter and Summer are not technically semesters) */
    year                INT NOT NULL,
    location            CHAR NOT NULL,
    enrollmentlimit     INT NOT NULL, /* We don't need current enrollment number since we can just run a COUNT query for that to check for it */
    PRIMARY KEY (crn),
    FOREIGN KEY (coursenumber) REFERENCES course(coursenumber),
    FOREIGN KEY (professorid) REFERENCES staff(staffid)
);

create table outcome (
    coursenumber        INT NOT NULL,
    outcometype         CHAR NOT NULL, /* Outcomes can be GM1, GM2, H, V, W, SS, NS, FYS */
    FOREIGN KEY (coursenumber) REFERENCES course(coursenumber)
);

create table prerequisite (
    coursenumber             INT NOT NULL,
    prerequisite        INT NOT NULL,
    FOREIGN KEY (coursenumber) REFERENCES course(coursenumber),
    FOREIGN KEY (prerequisite) REFERENCES course(coursenumber)
);

/*Links student to their respective class instance*/
create table studenttoclassinstance (
    lnumber             INT NOT NULL,
    crn                 INT NOT NULL,
    status              CHAR NOT NULL, /*Number representing if withdrawn, in-progress, or if taken already*/
    grade               CHAR, /*Can be null if still in progress or withdrawn*/
    FOREIGN KEY (lnumber) REFERENCES student(lnumber),
    FOREIGN KEY (crn) REFERENCES classinstance(crn)
);

create table librarybooks (
    bookid              INT NOT NULL UNIQUE,
    bookname            CHAR(100) NOT NULL,
    author              CHAR(100) NOT NULL,
    PRIMARY KEY (bookid)
);



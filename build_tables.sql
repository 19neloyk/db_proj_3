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
    classid             INT NOT NULL UNIQUE, /* Arbitrary unique identifier */
    classnumber         INT NOT NULL,   /* This represents the 320 in "CS320" */       
    department          CHAR NOT NULL,  /* This represents the "CS" in "CS320" */
    name                CHAR NOT NULL,
    description         CHAR,
    PRIMARY KEY (classnumber)
);

create table classinstance (
    crn                 INT NOT NULL UNIQUE,
    classid             INT NOT NULL,
    professorid         INT NOT NULL,
    semester            CHAR NOT NULL,
    section             INT NOT NULL,
    location            CHAR NOT NULL,
    enrollmentlimit     INT NOT NULL,
    enrollment          INT NOT NULL,
    PRIMARY KEY (classinstance),
    FOREIGN KEY (classid) REFERENCES class(classid),
    FOREIGN KEY (professorid) REFERENCES staff(staffid)
);

create table outcome (
    classid             INT NOT NULL,
    outcomenumber       INT NOT NULL,
    FOREIGN KEY (classid) REFERENCES class(classid)
);

create table prerequisite (
    classid             INT NOT NULL,
    prerequisite        INT NOT NULL,
    FOREIGN KEY (classid) REFERENCES class(classid),
    FOREIGN KEY (prerequisite) REFERENCES class(classid),
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
    FOREIGN KEY (jobid) REFERENCES job(jobid),
);

create table jobtype (
    jobid               INT NOT NULL UNIQUE,
    jobname             CHAR NOT NULL UNIQUE,
    hours               INT NOT NULL,
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


/* Import database in csv format example
.separator ","
.mode csv
.import "00_build_db/movies.csv"  movies
.import "00_build_db/stars.csv"   stars
.import "00_build_db/studios.csv" studios
.import "00_build_db/starIn.csv"  starIn

*/

.separator ","
.mode csv
.import "db_proj_3/librarybooks.csv"  librarybooks
.import "db_proj_3/jobtype.csv"  jobtype
.import "db_proj_3/staff.csv"  staff
.import "db_proj_3/class.csv"  class
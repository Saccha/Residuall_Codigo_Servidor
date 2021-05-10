CREATE TABLE Validacao(
    ID              int    primary key      NOT NULL,
    email_adress    varchar                 NOT NULL,
    domain          varchar                 NOT NULL,
    valid_syntax    boolean                 NOT NULL
)

CREATE TABLE Validacao3(
    ID              int     primary key     NOT NULL,
    email_adress    varchar                 NOT NULL,
    domain          VARCHAR                 NOT NULL,
    valid_syntax    boolean                 NOT NULL,
    disposable      boolean                 NOT NULL,
    webmail         boolean                 NOT NULL,
    deliverable     boolean                 NOT NULL,
    catch_all       boolean                 NOT NULL,
    gibberish       boolean                 NOT NULL
)

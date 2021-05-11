CREATE TABLE ValidacaoV1 (
ID int IDENTITY(1,1) NOT NULL,
email_address varchar(50) NULL,
domain varchar(50) NULL,
valid_syntax bit NULL,
 CONSTRAINT [PK__ValidacaoV1] PRIMARY KEY CLUSTERED
(
ID ASC
)
)

CREATE TABLE ValidacaoV3(
ID int IDENTITY(1,1) NOT NULL,
email_address varchar(50) NULL,
domain varchar(50) NULL,
valid_syntax bit NULL,
disposable bit NULL,
webmail bit NULL,
deliverable bit NULL,
catch_all bit NULL,
gibberish bit NULL,
 CONSTRAINT [PK__ValidacaoV3] PRIMARY KEY CLUSTERED
(
ID ASC
)
)

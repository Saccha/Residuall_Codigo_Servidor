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

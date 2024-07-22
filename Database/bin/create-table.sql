CREATE TABLE eAS (
    itemID varchar(40),
    title varchar(160),
    price double precision,
    condition varchar(40),
    itemDescription varchar(10000),
    UNIQUE (itemID)
);
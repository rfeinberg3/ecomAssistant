CREATE TABLE items (
    SKU varchar(20),
    name varchar(160),
    price double precision,
    description varchar(10000),
    UNIQUE (SKU)
);
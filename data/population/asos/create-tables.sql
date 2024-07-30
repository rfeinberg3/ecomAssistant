CREATE TABLE clothing (
    sku VARCHAR(20),
    name TEXT,
    price DOUBLE PRECISION,
    description TEXT,
    UNIQUE (sku)
);
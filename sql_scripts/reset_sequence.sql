-- reset_sequence.sql
DELETE FROM bitcoin_prices;
ALTER SEQUENCE bitcoin_prices_id_seq RESTART WITH 1;

CREATE extension IF NOT EXISTS pg_trgm;

CREATE EXTENSION IF NOT EXISTS "vector";

ALTER SYSTEM
SET
    pg_trgm.word_similarity_threshold = 0.6;

DROP SCHEMA IF EXISTS global CASCADE;

CREATE SCHEMA global;

CREATE TABLE global.people (
    id TEXT PRIMARY KEY,
    name TEXT NOT NULL,
    description TEXT NOT NULL,
    bm25_id SERIAL
);

CREATE INDEX people_name ON global.people USING GIN (name gin_trgm_ops);

CREATE INDEX people_description ON global.people USING GIN (description gin_trgm_ops);

-- CALL paradedb.create_bm25 (
--     index_name => 'people_search',
--     table_name => 'people',
--     key_field => 'bm25_id',
--     schema_name => 'global',
--     text_fields => '{
--     description: {}, name: {}
--   }'
-- );
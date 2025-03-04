CREATE EXTENSION IF NOT EXISTS postgis;

CREATE SCHEMA IF NOT EXISTS nyc;

CREATE TABLE IF NOT EXISTS nyc.collisions (
    collision_id INTEGER PRIMARY KEY,
    crash_datetime TIMESTAMPTZ NOT NULL,
    borough TEXT,
    zip_code TEXT,
    location GEOMETRY(Point, 4326),
    on_street_name TEXT,
    off_street_name TEXT,
    cross_street_name TEXT,
    number_of_persons_injured INTEGER NOT NULL,
    number_of_persons_killed INTEGER NOT NULL,
    number_of_pedestrians_injured INTEGER NOT NULL,
    number_of_pedestrians_killed INTEGER NOT NULL,
    number_of_cyclist_injured INTEGER NOT NULL,
    number_of_cyclist_killed INTEGER NOT NULL,
    number_of_motorist_injured INTEGER NOT NULL,
    number_of_motorist_killed INTEGER NOT NULL,
    contributing_factor_vehicle_1 TEXT,
    contributing_factor_vehicle_2 TEXT,
    contributing_factor_vehicle_3 TEXT,
    contributing_factor_vehicle_4 TEXT,
    contributing_factor_vehicle_5 TEXT,
    vehicle_type_code1 TEXT,
    vehicle_type_code2 TEXT,
    vehicle_type_code3 TEXT,
    vehicle_type_code4 TEXT,
    vehicle_type_code5 TEXT
);

CREATE INDEX idx_location ON nyc.collisions USING GIST(location);
CREATE INDEX idx_crash_datetime ON nyc.collisions (crash_datetime DESC);
CREATE INDEX idx_borough ON nyc.collisions (borough);
CREATE INDEX idx_number_of_persons_injured ON nyc.collisions (number_of_persons_injured);
CREATE INDEX idx_borough_crash_date ON nyc.collisions (borough, crash_datetime);

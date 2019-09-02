CREATE TABLE IF NOT EXISTS cars_table
(
    name VARCHAR(255) NOT NULL,
    price integer NOT NULL,
    abtest VARCHAR(255) NOT NULL,
	vehicleType VARCHAR(255) NOT NULL,
	yearOfRegistration VARCHAR(4) NOT NULL,
	gearbox VARCHAR(255) NOT NULL,
	powerPS integer NOT NULL,
	model VARCHAR(255) NOT NULL,
	kilometer integer NOT NULL,
	monthOfRegistration integer NOT NULL,
	fuelType VARCHAR(255) NOT NULL,
	brand VARCHAR(255) NOT NULL,
	notRepairedDamage VARCHAR(255) NOT NULL,
	dateCreated DATE NOT NULL,
	postalCode VARCHAR(255) NOT NULL
);
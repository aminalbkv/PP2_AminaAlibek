CREATE OR REPLACE PROCEDURE upsert_contact(
    p_name VARCHAR,
    p_phone VARCHAR
)
LANGUAGE plpgsql
AS $$
BEGIN
    IF EXISTS (
        SELECT 1
        FROM contacts
        WHERE first_name = p_name
    ) THEN
        UPDATE contacts
        SET phone = p_phone
        WHERE first_name = p_name;
    ELSE
        INSERT INTO contacts (first_name, phone)
        VALUES (p_name, p_phone);
    END IF;
END;
$$;


CREATE OR REPLACE PROCEDURE bulk_insert_contacts(
    IN p_names TEXT[],
    IN p_phones TEXT[],
    OUT invalid_data TEXT[]
)
LANGUAGE plpgsql
AS $$
DECLARE
    i INTEGER;
BEGIN
    invalid_data := ARRAY[]::TEXT[];

    IF array_length(p_names, 1) IS DISTINCT FROM
       array_length(p_phones, 1) THEN
        RAISE EXCEPTION 'Names and phones count must match';
    END IF;

    FOR i IN 1..COALESCE(array_length(p_names, 1), 0) LOOP
        IF p_phones[i] ~ '^[78][0-9]{10}$' THEN
            INSERT INTO contacts (first_name, phone)
            VALUES (p_names[i], p_phones[i]);
        ELSE
            invalid_data := array_append(
                invalid_data,
                p_names[i] || ': ' || COALESCE(p_phones[i], 'NULL')
            );
        END IF;
    END LOOP;
END;
$$;



CREATE OR REPLACE PROCEDURE delete_contact(
    p_value TEXT
)
LANGUAGE plpgsql
AS $$
BEGIN
    DELETE FROM contacts
    WHERE first_name = p_value
       OR phone = p_value;
END;
$$;

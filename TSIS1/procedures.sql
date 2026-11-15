
-- TSIS 1: PhoneBook
-- Task 3.4: Stored Procedures and Functions


-- ==========================================
-- 1. PROCEDURE: ADD PHONE
-- ==========================================

CREATE OR REPLACE PROCEDURE add_phone(
    p_contact_name VARCHAR,
    p_phone VARCHAR,
    p_type VARCHAR
)
LANGUAGE plpgsql
AS $$
DECLARE
    v_contact_id INTEGER;
BEGIN
    SELECT id INTO v_contact_id
    FROM contacts
    WHERE first_name = p_contact_name;

    IF v_contact_id IS NULL THEN
        RAISE EXCEPTION 'Contact not found';
    END IF;

    INSERT INTO phones (contact_id, phone, type)
    VALUES (v_contact_id, p_phone, p_type);
END;
$$;


-- ==========================================
-- 2. PROCEDURE: MOVE TO GROUP
-- ==========================================

CREATE OR REPLACE PROCEDURE move_to_group(
    p_contact_name VARCHAR,
    p_group_name VARCHAR
)
LANGUAGE plpgsql
AS $$
DECLARE
    v_contact_id INTEGER;
    v_group_id INTEGER;
    v_count INTEGER;
BEGIN
    SELECT COUNT(*), MIN(id)
    INTO v_count, v_contact_id
    FROM contacts
    WHERE first_name = p_contact_name;

    IF v_count = 0 THEN
        RAISE EXCEPTION 'Contact not found: %', p_contact_name;
    ELSIF v_count > 1 THEN
        RAISE EXCEPTION 'Multiple contacts found: %', p_contact_name;
    END IF;

    IF p_group_name IS NULL OR TRIM(p_group_name) = '' THEN
        RAISE EXCEPTION 'Group name cannot be empty';
    END IF;

    INSERT INTO groups (name)
    VALUES (p_group_name)
    ON CONFLICT (name) DO NOTHING;

    SELECT id INTO v_group_id
    FROM groups
    WHERE name = p_group_name;

    UPDATE contacts
    SET group_id = v_group_id
    WHERE id = v_contact_id;
END;
$$;


-- ==========================================
-- 3. FUNCTION: SEARCH CONTACTS
-- ==========================================

-- Remove the old Practice 8 function
-- because its return type is different.

DROP FUNCTION IF EXISTS search_contacts(TEXT);

CREATE OR REPLACE FUNCTION search_contacts(p_query TEXT)
RETURNS TABLE (
    contact_id INTEGER,
    contact_name VARCHAR(100),
    email VARCHAR(100),
    birthday DATE,
    group_name VARCHAR(50)
)
LANGUAGE plpgsql
AS $$
BEGIN
    RETURN QUERY
    SELECT
        c.id,
        c.first_name,
        c.email,
        c.birthday,
        g.name
    FROM contacts c
    LEFT JOIN groups g
        ON c.group_id = g.id
    WHERE
        c.first_name ILIKE '%' || p_query || '%'
        OR c.email ILIKE '%' || p_query || '%'
        OR EXISTS (
            SELECT 1
            FROM phones p
            WHERE p.contact_id = c.id
              AND p.phone ILIKE '%' || p_query || '%'
        )
    ORDER BY c.id;
END;
$$;

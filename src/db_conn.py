import psycopg2


class DBConnection(object):
    def __init__(self):
        self.session = psycopg2.connect(dbname="easypay_db", user="postgres",
                                        password="postgres", host="localhost")
        self.cursor = None

    def __enter__(self):
        self.cursor = self.session.cursor()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.session.close()

    def set_zero_values(self):
        self.cursor.execute("UPDATE counters SET old_value = 0,"
                            " current_value = 0, is_fixed = FALSE,"
                            " is_active = TRUE WHERE id = 49;")
        self.session.commit()

    def check_status_fix(self):
        self.cursor.execute("SELECT is_fixed FROM counters WHERE id=49;")
        value = self.cursor.fetchone()[0]
        return value

    def set_fixed(self):
        self.cursor.execute("UPDATE counters SET is_fixed = TRUE"
                            " WHERE id = 49;")
        self.session.commit()

    def set_unfixed(self):
        self.cursor.execute("UPDATE counters SET is_fixed = FALSE"
                            " WHERE id = 49;")
        self.session.commit()

    def set_activated(self):
        self.cursor.execute("UPDATE counters SET is_active = TRUE"
                            " WHERE id = 49;")
        self.session.commit()

    def set_deactivated(self):
        self.cursor.execute("UPDATE counters SET is_active = FALSE"
                            " WHERE id = 49;")
        self.session.commit()

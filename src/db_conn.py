import psycopg2
from src.test_data import db_counter_id, schedule_item_date, schedule_item_id


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
                            " is_active = TRUE WHERE id = %s;" % db_counter_id)
        self.session.commit()

    def get_ready_value(self):
        self.cursor.execute("UPDATE counters SET old_value = 10,"
                            " current_value = 10, is_fixed = FALSE,"
                            " is_active = TRUE WHERE id = %s;" % db_counter_id)
        self.session.commit()

    def check_status_fix(self):
        self.cursor.execute("SELECT is_fixed FROM counters WHERE id = %s;"
                            % db_counter_id)
        return self.cursor.fetchone()[0]

    def set_fixed(self):
        self.cursor.execute("UPDATE counters SET old_value = 10,"
                            " current_value = 10, is_fixed = TRUE"
                            " WHERE id = %s;" % db_counter_id)
        self.session.commit()

    def set_unfixed(self):
        self.cursor.execute("UPDATE counters SET old_value = 10,"
                            " current_value = 10, is_fixed = FALSE"
                            " WHERE id = %s;" % db_counter_id)
        self.session.commit()

    def set_activated(self):
        self.cursor.execute("UPDATE counters SET old_value = 10,"
                            " current_value = 10, is_active = TRUE"
                            " WHERE id = %s;" % db_counter_id)
        self.session.commit()

    def set_deactivated(self):
        self.cursor.execute("UPDATE counters SET old_value = 10,"
                            " current_value = 10, is_active = FALSE"
                            " WHERE id = %s;" % db_counter_id)
        self.session.commit()

    def check_status_active(self):
        self.cursor.execute("SELECT is_active FROM counters WHERE id = %s;"
                            % db_counter_id)
        return self.cursor.fetchone()[0]

    def set_schedule_item(self):
        self.cursor.execute("UPDATE schedules SET event_date='%s',"
                            " is_repeat=true, address_id=27, user_id=110 WHERE id=%s" % schedule_item_date, schedule_item_id)
        self.session.commit()
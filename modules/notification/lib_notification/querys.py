class Query:
    def get_users_create_today(self):
        sql = """
        select
                *
        from
            users
        where
            date_trunc('day', created_at) = date_trunc('day', now()) 
        ;
        """
        return sql
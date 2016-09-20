from allauth.account.adapter import DefaultAccountAdapter


class NoNewUsersAccountAdapter(DefaultAccountAdapter):

    def is_open_for_signup(self, request):
        """
        Checks whether or not the site is open for signups.

        Next to simply returnt True/False, you can also intervene the
        regular fow by raising and ImmediateHttpResponse

        """
        return False

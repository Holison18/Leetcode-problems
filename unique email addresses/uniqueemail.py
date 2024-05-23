class Solution(object):
    def UniqueEmailAddresses(self, emails):
        unique_emails = set()
        for email in emails:
            local, domain = email.split("@") 
            if "+" in local:
                local = local[:local.index("+")]  # Ignore everything after +
            local = local.replace(".", "")  # Remove all periods
            unique_emails.add(local + "@" + domain)  # Add the cleaned email to the set
        return len(unique_emails)  # Return the number of unique emails





mySoln  = Solution()
print(mySoln.UniqueEmailAddresses(["kob.by@emali.com","mary@email.com"]))
print(mySoln.UniqueEmailAddresses(["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]))
print(mySoln.UniqueEmailAddresses(["a@leetcode.com","b@leetcode.com","c@leetcode.com"]))
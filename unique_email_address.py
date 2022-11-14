class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        valid_emails = []

        for mail in emails :
            local , domain = mail.split("@")
            
            # local filter "."
            while "." in local :
                indx = local.index(".")
                local =  local[:indx] +local[indx +1 :]
                
            if "+" in local:
                plus_indx = local.index("+")
                local = local[ : plus_indx]
                
            result = "@".join([local,domain])

            # insert in vallid emails
            if result not in valid_emails :
                valid_emails.append(result)
                
        return len(valid_emails)
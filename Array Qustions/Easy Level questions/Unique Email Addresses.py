'''
Unique Email Addresses
Easy

Every valid email consists of a local name and a domain name, separated by the '@' sign. Besides lowercase letters, the email may contain one or more '.' or '+'.

For example, in "alice@leetcode.com", "alice" is the local name, and "leetcode.com" is the domain name.
If you add periods '.' between some characters in the local name part of an email address, mail sent there will be forwarded to the same address without dots in the local name. Note that this rule does not apply to domain names.

For example, "alice.z@leetcode.com" and "alicez@leetcode.com" forward to the same email address.
If you add a plus '+' in the local name, everything after the first plus sign will be ignored. This allows certain emails to be filtered. Note that this rule does not apply to domain names.

For example, "m.y+name@email.com" will be forwarded to "my@email.com".
It is possible to use both of these rules at the same time.

Given an array of strings emails where we send one email to each email[i], return the number of different addresses that actually receive mails.

 

Example 1:

Input: emails = ["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]
Output: 2
Explanation: "testemail@leetcode.com" and "testemail@lee.tcode.com" actually receive mails.
'''

class Solution:
    def numUniqueEmails(self, emails) -> int:
        # uniq_email = set()
        # for i in emails:
        #     name , domain = i.split("@")
        #     if "+" in name:
        #         name = name[:name.index("+")]
        #     name = name.replace(".","")
        #     email = name + "@" + domain
        #     uniq_email.add(email)
        # return len(uniq_email)
    
    
        # using dictionary///
        dict1 = {}
        for i in emails:
            a = i.split("@")
            local_name = a[0]
            domain_name = a[-1]
            if "+" in local_name:
                ix = local_name.index("+")
                local_name = local_name[:ix]
            local_name = local_name.replace(".","")

            if (domain_name in dict1) and (local_name not in dict1[domain_name]):
                    dict1[domain_name].append(local_name)
            else:
                dict1[domain_name] = [local_name]

        count = 0
        for i in dict1.values():
            count += len(i)
        return count

s = Solution()
s.numUniqueEmails(["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"])
          
